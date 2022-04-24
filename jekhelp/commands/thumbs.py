"""thumbs subcommand module
"""
import click
from pathlib import Path
# from shutil import copy2
from subprocess import run
import yaml

from jekhelp.config import valid_conf


@click.command()
@click.argument('source_image', nargs=-1, type=click.Path(exists=True))
@click.argument('post_md_file', nargs=1, type=click.Path(exists=True))
@click.option('--write', '-w', is_flag=True,
              help="Do the conversion. Dry-run is default.")
@click.option('--force', '-f', is_flag=True,
              help="Overwrite if existing already.")
@click.option('--gallery', '-g', type=str,
              help="Create collection markdown files for photo gallery as well.")
def thumbs(source_image, post_md_file, write, force, gallery):
    """
    Generate thumbnail and full-size pics from a list of pictures,
    rename and put them into a subfolder of a the images directory of a Jekyll
    project.
    """
    def decide_and_copy(source, target, is_thumb):
        """
        The worker function.
        """
        orig_target = f"{source} -> {target}"
        doit = False

        if is_thumb:
            convert = ['convert', '-resize', '333', orig, thumb]
        else:
            convert = ['convert', '-resize', '1280', orig, full]

        if target.exists():
            if write and force:
                task = f"Convert (force): {orig_target}"
                doit = True
            else:
                task = f"Existing: {orig_target}"
        else:
            if write:
                task = f"Convert: {orig_target}"
                doit = True
            else:
                task = f"Dry-run: {orig_target}"

        click.echo(task)
        run(convert) if doit else None


    def collection_file(coll_dir, fullsize_img_path):
        """
        Generate one collection file referencing the passed image file.
        """
        md_file = Path(collection_dir / f"{fullsize_img_path.stem}.md")
        coll_dir.mkdir() if not coll_dir.is_dir() else None
        doit = False

        if md_file.exists():
            if write and force:
                task = f"Write (force): {md_file}"
                doit = True
            else:
                task = f"Existing: {md_file}"
        else:
            if write:
                task = f"Write: {md_file}"
                doit = True
            else:
                task = f"Dry-run: {md_file}"

        click.echo(task)

        if doit:
            with open (md_file, 'w')  as md:
                yaml.dump_all(
                    [{
                        'title': fullsize_img_path.stem,
                        'image-path': fullsize_img_path.as_posix(),
                        'caption': ''
                    },
                    {}],
                    md, default_flow_style=False, allow_unicode=True,
                    explicit_start=True
                )

    post_name = Path(post_md_file).stem
    post_img_dir = Path(valid_conf.images_dir / post_name)
    post_img_dir.mkdir() if not post_img_dir.is_dir() else None

    if gallery:
        gallery = f"_{gallery}" if gallery[:1] != "_" else gallery
        collection_dir = valid_conf.site_root / gallery

    p_cnt = 1
    for image in source_image:
        orig = Path(image)
        ext = orig.suffix
        full = Path(post_img_dir / f"{p_cnt}{ext}")
        thumb = Path(post_img_dir / f"{p_cnt}-th{ext}")
        decide_and_copy(orig, full, is_thumb=False)
        decide_and_copy(orig, thumb, is_thumb=True)
        if gallery:
            collection_file(collection_dir, full)
        p_cnt += p_cnt

"""thumbs subcommand module
"""
import click
from pathlib import Path
# from shutil import copy2
import yaml
from PIL import Image

from jekhelp.config import valid_conf


@click.command()
@click.argument('source_image', nargs=-1, type=click.Path(exists=True))
@click.argument('post_md_file', nargs=1, type=click.Path(exists=True))
@click.option('--write', '-w', is_flag=True,
              help="Do the conversion. Dry-run is default.")
@click.option('--force', '-f', is_flag=True,
              help="Overwrite if existing already.")
@click.option('--gallery', '-g', type=str,
              help="Create collection markdown files for photo gallery as well.")  # noqa
@click.option('--start', '-s', type=int, default=1, show_default=True,
              help="Start naming pics and gallery files with this number.")
def thumbs(source_image, post_md_file, write, force, gallery, start):
    """ Generate a Jekyll picture gallery

    Create thumbnail and full-size pics from a list of pictures, rename
    them, file them into the project's images dir, optionally generate picture
    collection Markdown files.
    """
    def decide_and_copy(source, target, is_thumb):
        """
        The worker function.
        """
        orig_target = f"{source} -> {target}"
        doit = False

        if is_thumb:
            # convert = ['convert', '-resize', '333', orig, thumb]
            size = (333, 333)
            thumb_or_full = thumb
        else:
            # convert = ['convert', '-resize', '1280', orig, full]
            size = (1280, 1280)
            thumb_or_full = full

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

        if doit:
            with Image.open(source) as im:
                im.thumbnail(size)
                im.save(thumb_or_full, "JPEG")

    def collection_file(coll_dir, fullsize_img_path):
        """ Generate one collection file referencing the passed image file.
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
            image_path_relative = fullsize_img_path.as_posix().replace(
                valid_conf.images_dir.parent.as_posix(), ""
            )

            with open(md_file, 'w') as md:
                yaml.dump(
                    {
                        'title': fullsize_img_path.stem,
                        'image-path': image_path_relative,
                        'caption': ''
                    },
                    md, default_flow_style=False, allow_unicode=True,
                    explicit_start=True, explicit_end=True
                )

    post_name = Path(post_md_file).stem
    post_img_dir = Path(valid_conf.images_dir / post_name)
    post_img_dir.mkdir() if not post_img_dir.is_dir() else None

    if gallery:
        gallery = f"_{gallery}" if gallery[:1] != "_" else gallery
        collection_dir = valid_conf.site_root / gallery

    p_cnt = start
    for image in source_image:
        if Path(image).is_dir():
            continue
        orig = Path(image)
        ext = orig.suffix
        zfill_cnt = str(p_cnt).zfill(2)
        full = post_img_dir / f"{zfill_cnt}{ext}"
        thumb = post_img_dir / f"{zfill_cnt}-th{ext}"
        decide_and_copy(orig, full, is_thumb=False)
        decide_and_copy(orig, thumb, is_thumb=True)
        if gallery:
            collection_file(collection_dir, full)
        p_cnt += 1

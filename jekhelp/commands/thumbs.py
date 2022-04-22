"""thumbs subcommand module
"""
import click
from pathlib import Path
# from shutil import copy2
from subprocess import run

from jekhelp.config import valid_conf


@click.command()
@click.argument('source_image', nargs=-1, type=click.Path(exists=True))
@click.argument('post_md_file', nargs=1, type=click.Path(exists=True))
@click.option('--write', '-w', is_flag=True,
              help="Do the conversion. Dry-run is default.")
@click.option('--force', '-f', is_flag=True,
              help="Overwrite if existing already.")
def thumbs(source_image, post_md_file, write, force):
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

    post_name = Path(post_md_file).stem
    post_img_dir = Path(valid_conf.images_dir / post_name)
    post_img_dir.mkdir() if not post_img_dir.is_dir() else None

    p_cnt = 1
    for image in source_image:
        orig = Path(image)
        ext = orig.suffix
        full = Path(post_img_dir / f"{p_cnt}{ext}")
        thumb = Path(post_img_dir / f"{p_cnt}-th{ext}")
        decide_and_copy(orig, full, is_thumb=False)
        decide_and_copy(orig, thumb, is_thumb=True)
        p_cnt += p_cnt

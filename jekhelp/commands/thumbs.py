"""thumbs subcommand module
"""
import click
from jekhelp.config import valid_conf


@click.command()
@click.argument('name', nargs=1)
def thumbs(name):
    """
    Generate thumbnail and full-size pics from a list of pictures,
    rename and put them into a subfolder of a the images directory of a Jekyll
    project.
    """
    click.echo(f'Hello {name}')

    print("in cli thumbs command, config data:")
    print(valid_conf.site_root)
    print(valid_conf.images_dir)

import logging
import shutil
from datetime import date
from pathlib import Path

import toml
import click

from tyrannosaurus import metadata

logger = logging.getLogger(__package__)


@click.group()
def cli():
    pass


@cli.command()
@click.argument("name")
def new(name: str):
    pass


@cli.command()
def meta():
    print(metadata)


@cli.command()
def sync():
    today = str(date.today())
    path = Path(__file__).parent.parent / "pyproject.toml"
    data = toml.loads(path.read_text(encoding="utf8"))


@cli.command()
def clean():
    trash = {".egg-info", ".pytest_cache", "eggs", "__pypackages__", "build", ".tyrannosaurus"}
    for path in Path(".").iterdir():
        if path.name in trash:
            shutil.rmtree(path)
    click.echo("Done.")


if __name__ == "__main__":
    cli()

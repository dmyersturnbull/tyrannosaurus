"""
Tyrannosaurus command-line interface and processor / main code.
All of its code is here.
"""

from __future__ import annotations

import logging
import re
import shutil
from datetime import date
from pathlib import Path, PurePath
from subprocess import check_call
from typing import Any, Mapping, Union

import toml

import click

logger = logging.getLogger(__package__)


class Toml:
    """
    A thin wrapper around toml to make getting values easier.
    Example:
        ``version = Toml.read('myfile.toml')['tool.poetry.version']``
    """

    @classmethod
    def read(cls, path: Union[PurePath, str]) -> Toml:
        """
        Reads a UTF-8 TOML file and returns a new ``Toml``.
        Args:
            path: A path-like pointer to the file.
        Returns:
            A new Toml.
        """
        return Toml(toml.loads(Path(path).read_text(encoding="utf8")))

    def __init__(self, x: Mapping[str, Any]) -> None:
        """
        Constructor.
        Args:
            x: Data from ``toml.reads``.
        """
        self.x = x

    def __getitem__(self, items: str):
        """
        Gets an item from the toml.
        Example:
            ``data['tool.poetry']``
        Args:
            items: A period-separated string of nested items in the dict.
        Returns:
            The value, which could be a list, set, dict, date, datetime, int, float, or str.
        Raises:
            KeyError: If the item doesn't exist.
        """
        at = self.x
        for item in items.split("."):
            at = at[item]
        return at


@click.group()
def cli() -> None:
    """Main function for CLI."""
    pass


@cli.command()
@click.argument("name")
def new(name: str) -> None:
    """
    Creates a new project.
    Args:
        name: The name of the project, which will also be used as the path to create.
    """
    check_call("git clone https://github.com/dmyersturnbull/tyrannosaurus.git " + name)
    click.echo("Done!")


@cli.command()
@click.argument(
    "path", type=click.Path, exists=True, readable=True, writable=True, file_ok=False, dir_ok=True
)
def sync(path: str) -> None:
    """
    Syncs project metadata between configured files.
    Args:
        path: Path of the project root.
    """
    today = str(date.today())
    data = Toml.read(Path(path) / "pyproject.toml")
    targets = {k for k, v in data["tool.tyrannosaurus.targets"].items() if v}
    print("Did nothing.")


@cli.command()
@click.argument(
    "path", type=click.Path, exists=True, readable=True, writable=True, file_ok=False, dir_ok=True
)
@click.option("--aggressive", type=bool)
def clean(path: str, aggressive: bool) -> None:
    """
    Deletes temporary and unwanted files and directories.
    Args:
        path: Path of the project root.
        aggressive: Delete additional files, including .swp, .ipython_checkpoints, and dist.
    """
    trash_names = {
        ".egg-info",
        ".pytest_cache",
        "__pycache__",
        "cython_debug",
        "eggs",
        "__pypackages__",
        ".tyrannosaurus",
        "Thumbs.db",
    }
    trash_patterns = {
        re.compile(r".*\.py[cod]"),
        re.compile(r".*\$py\.class"),
        re.compile(r".*\.egg-info"),
    }
    # "docs/_build", "docs/_html",
    if aggressive:
        trash_names.update({".tox", "dist", "sdist", "build", ".ipynb_checkpoints"})
        trash_patterns.update({re.compile(r"\*\.swp")})
    for p in Path(path).glob("**/*"):
        if p.name in trash_names:
            shutil.rmtree(p)
        elif p.parent == p.parent.name == "docs" and p.name == "html":
            shutil.rmtree(p)
        else:
            for pattern in trash_patterns:
                if pattern.fullmatch(p.name):
                    shutil.rmtree(p)
                    break
    click.echo("Done.")


if __name__ == "__main__":
    cli()

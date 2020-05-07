"""
Tyrannosaurus command-line interface and processor / main code.
All of its code is here.
"""

from __future__ import annotations

import logging
import re
import shutil
from datetime import date, datetime
from pathlib import Path, PurePath
from subprocess import check_call
from typing import Any, Mapping, Union

import tomlkit
import typer

logger = logging.getLogger(__package__)
today = date.today()


class _Toml:
    """A thin wrapper around toml to make getting values easier."""

    @classmethod
    def read(cls, path: Union[PurePath, str]) -> _Toml:
        return _Toml(tomlkit.loads(Path(path).read_text(encoding="utf8")))

    def __init__(self, x: Mapping[str, Any]) -> None:
        self.x = x

    def __getitem__(self, items: str):
        at = self.x
        for item in items.split("."):
            at = at[item]
        return at


class _Source:
    @classmethod
    def parse(cls, s: str, toml: _Toml) -> str:
        if s.startswith("'") and s.endswith("'"):
            return (
                s.replace("${today}", str(today))
                .replace("${today.year}", str(today.year))
                .replace("${today.month}", str(today.month))
                .replace("${today.day}", str(today.day))
            )
        else:
            value = toml[s]
            if not isinstance(value, (str, int, float, date, datetime)):
                raise ValueError("Key {} does not refer to a string, int, etc.".format(s))
            return str(value)


cli = typer.Typer()


@cli.command()
def new(name: str) -> None:
    """
    Creates a new project.
    Args:
        name: The name of the project, which will also be used as the path to create.
    """
    check_call("git clone https://github.com/dmyersturnbull/tyrannosaurus.git " + name)
    typer.echo("Cloned but did little else!")


@cli.command()
def sync(path: Path) -> None:
    """
    Syncs project metadata between configured files.
    Args:
        path: Path of the project root.
    """
    data = _Toml.read(Path(path) / "pyproject.toml")
    options = {k for k, v in data["tool.tyrannosaurus.options"].items() if v}
    sources = {
        k: _Source.parse(v, data) for k, v in data["tool.tyrannosaurus.sources"].items() if v
    }
    targets = {k for k, v in data["tool.tyrannosaurus.targets"].items() if v}
    print("Did nothing.")


@cli.command()
def clean(path: Path, aggressive: bool) -> None:
    """
    Deletes temporary and unwanted files and directories.
    Args:
        path: Path of the project root.
        aggressive: Delete additional files, including .swp, .ipython_checkpoints, and dist.
    """
    # also add non-most-recent versions from "dist", "sdist"
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
        trash_names.update({".tox", "dist", "sdist", "build", ".ipynb_checkpoints", "poetry.lock"})
        trash_patterns.update({re.compile(r"\*\.swp")})
    for p in Path(path).glob("**/*"):
        if p.name in trash_names:
            shutil.rmtree(p)
        elif p.parent == p.parent.name == "docs" and p.name in ["html", "build"]:
            shutil.rmtree(p)
        else:
            for pattern in trash_patterns:
                if pattern.fullmatch(p.name):
                    shutil.rmtree(p)
                    break
    typer.echo("Done.")


if __name__ == "__main__":
    cli()

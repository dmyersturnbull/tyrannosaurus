"""
Tyrannosaurus command-line interface.
"""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Optional

import typer

from tyrannosaurus.context import _Context
from tyrannosaurus.helpers import _License, _Env
from tyrannosaurus.clean import Clean
from tyrannosaurus.new import New
from tyrannosaurus.sync import Sync
from tyrannosaurus.conda import Recipe, CondaEnv

logger = logging.getLogger(__package__)
cli = typer.Typer()


@cli.command()
def new(
    name: str,
    license: _License = "apache2",
    user: Optional[str] = None,
    authors: Optional[str] = None,
) -> None:
    """
    Creates a new project.
    Args:
        name: The name of the project, which will also be used as the path to create.
        license: The name of the license. One of:
                 apache2, cc0, ccby, ccbync, gpl3, lgpl3, mit
        user: Github repository user or org name
        authors: List of author names, comma-separated
    """
    e = _Env(user=user, authors=authors)
    path = Path(name)
    New(name, license_name=license, username=e.user, authors=e.authors).create(path)
    typer.echo("Done! Created a new repository under {}".format(name))
    typer.echo(
        "See https://tyrannosaurus.readthedocs.io/en/latest/guide.html#to-do-list-for-new-projects"
    )


@cli.command()
def sync(dry_run: bool = False) -> None:
    """
    Syncs project metadata between configured files.
    Args:
        dry_run: If set, does not touch the filesystem; only logs.
    """
    context = _Context(Path(os.getcwd()), dry_run=dry_run)
    typer.echo("Syncing metadata...")
    typer.echo("Currently, only targets 'init' and 'recipe' are implemented.")
    targets = Sync(context, dry_run=dry_run).sync(Path(os.getcwd()))
    typer.echo("Done. Synced to {} targets: {}.".format(len(targets), ", ".join(targets)))


@cli.command()
def env(
    path: Path = "environment.yml",
    name: Optional[str] = None,
    dev: bool = False,
    extras: bool = False,
    dry_run: bool = False,
) -> None:
    """
    Generates an Anaconda environment file.
    Args:
        path: Write tot his path
        name: The name of the environment; defaults to the project name
        dev: Include development/build dependencies
        extras: Include optional dependencies
        dry_run: If set, does not touch the filesystem; only logs.
    """
    typer.echo("Writing environment file...")
    context = _Context(Path(os.getcwd()), dry_run=dry_run)
    if name is None:
        name = context.project
    CondaEnv(name, dev=dev, extras=extras, dry_run=dry_run).create(context, path)
    typer.echo("Wrote environment {}".format(path))


@cli.command()
def recipe(dry_run: bool = False) -> None:
    """
    Generates a Conda recipe using grayskull.
    Args:
        dry_run: If set, does not touch the filesystem; only logs.
    """
    context = _Context(Path(os.getcwd()), dry_run=dry_run)
    output_path = context.path / "recipes"
    output_path = Recipe(dry_run=dry_run).create(context, output_path)
    typer.echo("Generated a new recipe at {}".format(output_path))


"""
@cli.command()
def update(dry_run: bool = False) -> None:
    updates, dev_updates = Update(dry_run=dry_run).update(Path(os.getcwd()))
    typer.echo("Main updates:")
    for pkg, (old, up) in updates.items():
        typer.echo("    {}:  {} --> {}".format(pkg, old, up))
    typer.echo("Dev updates:")
    for pkg, (old, up) in dev_updates.items():
        typer.echo("    {}:  {} --> {}".format(pkg, old, up))
    if not dry_run:
        logger.error("Auto-fixing is not supported yet!")
"""


@cli.command()
def clean(
    dists: bool = False, aggressive: bool = False, hard_delete: bool = False, dry_run: bool = False
) -> None:
    """
    Removes unwanted files.
    Deletes the contents of ``.tyrannosaurus``.
    Then trashes temporary and unwanted files and directories to a tree under ``.tyrannosaurus``.
    Args:
        dists: Remove dists
        aggressive: Delete additional files, including .swp, .ipython_checkpoints, and dist.
        hard_delete: If true, call shutil.rmtree instead of moving to .tyrannosaurus
        dry_run: If set, does not touch the filesystem; only logs.
    """
    trashed = Clean(dists, aggressive, hard_delete, dry_run).clean(Path(os.getcwd()))
    typer.echo("Trashed {} paths.".format(len(trashed)))


@cli.command()
def info() -> None:
    """
    Prints Tyrannosaurus info.
    """
    from tyrannosaurus import __version__, __date__

    typer.echo("Tyrannosaurus version {} ({})".format(__version__, __date__))


class Commands:
    new = new
    sync = sync
    recipe = recipe
    clean = clean
    info = info


if __name__ == "__main__":
    cli()


__all__ = [Commands]

# SPDX-License-Identifier Apache-2.0
# Source: https://github.com/dmyersturnbull/tyranno
"""
CLI for Tyranno.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

import typer

from tyranno.model.context import Context

logger = logging.getLogger(__package__)


class Msg:
    @classmethod
    def success(cls, msg: str) -> None:
        msg = typer.style(msg, fg=typer.colors.BLUE, bold=True)
        typer.echo(msg)

    @classmethod
    def info(cls, msg: str) -> None:
        typer.echo(msg)

    @classmethod
    def failure(cls, msg: str) -> None:
        msg = typer.style(msg, fg=typer.colors.RED, bold=True)
        typer.echo(msg)

    @classmethod
    def write_info(cls):
        from tyranno import ProjectInfo

        Msg.info(f"Tyranno v{ProjectInfo.version} ({ProjectInfo.date})")


@dataclass(frozen=True, repr=True)
class CliState:
    dry_run: bool = False
    verbose: bool = False

    def __post_init__(self):
        if self.verbose:
            logger.setLevel(logging.DEBUG)


cli = typer.Typer(add_completion=True)


class CliCommands:
    """
    Commands for Tyranno.
    """

    @staticmethod
    @cli.command()
    def new(
        name: str = typer.Argument("name", help="org/name"),
        track: bool = typer.Option(False, help="Track a remote repo"),
        prompt: bool = typer.Option(False, help="Prompt for info"),
        verbose: bool = typer.Option(False, "verbose", help="Output more info"),
    ) -> None:
        CliState(verbose=verbose)
        Msg.success(f"Done! Created a new repository under {name}")
        Msg.success("See https://tyranno.readthedocs.io/en/latest/guide.html")

    @staticmethod
    @cli.command()
    def sync(
        dry_run: bool = typer.Option(False, help="Don't write; just output"),
        verbose: bool = typer.Option(False, help="Output more info"),
    ) -> None:
        """
        Sync project metadata between configured files.
        """
        CliState(dry_run=dry_run, verbose=verbose)
        # context = Context(Path(os.getcwd()), dry_run=state.dry_run)
        Msg.info("Syncing metadata...")
        Msg.info("Currently, only targets 'init' and 'recipe' are implemented.")
        # targets = Sync(context).sync()
        # Msg.success(f"Done. Synced to {len(targets)} targets: {targets}")

    @staticmethod
    @cli.command()
    def env(
        path: Path = typer.Option("environment.yaml", help="Write to this path"),
        name: str = typer.Option("${.name}", help="Name of the environment"),
        dependency_groups: list[str] = typer.Option([], help="Poetry dependency groups to include"),
        dependency_extras: list[str] = typer.Option(
            [], help="Poetry extra dependencies to include"
        ),
        dry_run: bool = typer.Option(False, help="Don't write; just output"),
        verbose: bool = typer.Option(False, help="Output more info"),
    ) -> None:
        CliState(dry_run=dry_run, verbose=verbose)
        typer.echo("Writing environment file...")
        Msg.success(f"Wrote environment file {path}")

    @staticmethod
    @cli.command()
    def recipe(
        dry_run: bool = typer.Option(False, help="Don't write; just output"),
        verbose: bool = typer.Option(False, help="Output more info"),
    ) -> None:
        CliState(dry_run=dry_run, verbose=verbose)

    @staticmethod
    @cli.command()
    def reqs(
        dry_run: bool = typer.Option(False, help="Don't write; just output"),
        verbose: bool = typer.Option(False, help="Output more info"),
    ) -> None:
        state = CliState(verbose=verbose)
        Context(Path.cwd())
        # updates, dev_updates = Update(context).update()
        updates = None
        Msg.info("Main updates:")
        for pkg, (old, up) in updates.items():
            Msg.info(f"    {pkg}:  {old} --> {up}")

    @staticmethod
    @cli.command(help="Removes unwanted files")
    def clean(
        dry_run: bool = typer.Option(False, help="Don't write; just output"),
        verbose: bool = typer.Option(False, help="Output more info"),
    ) -> None:
        CliState(verbose=verbose, dry_run=dry_run)
        # trashed = Clean(dists, aggressive, hard_delete, dry_run).clean(Path(os.getcwd()))
        # Msg.info(f"Trashed {len(trashed)} paths.")


if __name__ == "__main__":
    cli()

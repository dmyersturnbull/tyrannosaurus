# SPDX-License-Identifier Apache-2.0
# Source: https://github.com/dmyersturnbull/tyranno
"""
CLI for Tyranno.
"""
from __future__ import annotations

import inspect
import logging
import os
from dataclasses import dataclass
from pathlib import Path

import typer

from tyranno.model.context import Context

logger = logging.getLogger(__package__)


def flag(name: str, desc: str, **kwargs) -> typer.Option:
    """Generates a flag-like Typer Option."""
    return typer.Option(False, "--" + name, help=desc, show_default=False, **kwargs)


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


def tyranno_main(
    version: bool = flag("version", "Write version and exit"),
    info: bool = flag("info", "Write info and exit (same as 'tyranno info')"),
):
    """
    Tyranno.
    Tyranno can create new modern Python projects from a template
    and synchronize metadata across the project.
    """
    if version or info:
        Msg.write_info()
        raise typer.Exit()


cli = typer.Typer(callback=tyranno_main, add_completion=True)


class CliCommands:
    """
    Commands for Tyranno.
    """

    @staticmethod
    @cli.command()
    def new(
        name: str = typer.Argument("name", help="org/name"),
        track: bool = flag("track", "Track an empty remote repo"),
        tyranno: str = typer.Option(
            "current",
            help=inspect.cleandoc(
                """
                Tyranno version to use as the template.
                Choices: an exact version, 'current' (this version), 'stable', or 'latest'.
                """
            ),
        ),
        prompt: bool = flag("prompt", "Prompt for info"),
        verbose: bool = flag("verbose", "Output more info"),
    ) -> None:  # pragma: no cover
        """
        Create a new project.
        """
        CliState(verbose=verbose)
        Msg.success(f"Done! Created a new repository under {name}")
        Msg.success("See https://tyranno.readthedocs.io/en/latest/guide.html")

    @staticmethod
    @cli.command()
    def sync(
        dry_run: bool = flag("dry-run", "Don't write; just output"),
        verbose: bool = flag("verbose", "Output more info"),
    ) -> None:  # pragma: no cover
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
        path: Path = typer.Option(help="Write to this path"),
        name: str
        | None = typer.Option(
            None, help="Name of the environment. [default: project name]", show_default=False
        ),
        dev: bool = flag("dev", "Include dev/build dependencies"),
        extras: bool = flag("extras", "Include optional dependencies"),
        dry_run: bool = flag("dry-run", "Don't write; just output"),
        verbose: bool = flag("verbose", "Output more info"),
    ) -> None:  # pragma: no cover
        """
        Generate an Anaconda environment file.
        """
        CliState(dry_run=dry_run, verbose=verbose)
        typer.echo("Writing environment file...")
        Msg.success(f"Wrote environment file {path}")

    @staticmethod
    @cli.command()
    def recipe(
        dry_run: bool = flag("dry-run", "Don't write; just output"),
        verbose: bool = flag("verbose", "Output more info"),
    ) -> None:  # pragma: no cover
        """
        Generate a Conda recipe using grayskull.
        """
        CliState(dry_run=dry_run, verbose=verbose)

    @staticmethod
    @cli.command()
    def update(
        auto_fix=flag("auto-fix", "Update dependencies in place (not supported yet)", hidden=True),
        verbose: bool = flag("verbose", "Output more information"),
    ) -> None:  # pragma: no cover
        """
        Find and list dependencies that could be updated.

        Args:
            auto_fix: Update dependencies in place (not supported yet)
            verbose: Output more information
        """
        state = CliState(verbose=verbose)
        Context(Path.cwd(), dry_run=not auto_fix)
        # updates, dev_updates = Update(context).update()
        updates = None
        Msg.info("Main updates:")
        for pkg, (old, up) in updates.items():
            Msg.info(f"    {pkg}:  {old} --> {up}")
        if not state.dry_run:
            Msg.failure("Auto-fixing is not supported yet!")

    @staticmethod
    @cli.command()
    def clean(
        dists: bool = flag("dists", "Remove dists"),
        aggressive: bool = flag(
            "aggressive", "Delete additional files, including .swp and .ipython_checkpoints"
        ),
        hard_delete: bool = flag("hard-delete", "Use shutil.rmtree instead of moving to .tyranno"),
        dry_run: bool = flag("dry-run", "Don't write; just output"),
        verbose: bool = flag("verbose", "Output more information"),
    ) -> None:  # pragma: no cover
        """
        Remove unwanted files.
        Deletes the contents of ``.tyranno``.
        Then trashes temporary and unwanted files and directories to a tree under ``.tyranno``.
        """
        CliState(verbose=verbose, dry_run=dry_run)
        # trashed = Clean(dists, aggressive, hard_delete, dry_run).clean(Path(os.getcwd()))
        # Msg.info(f"Trashed {len(trashed)} paths.")

    @staticmethod
    @cli.command()
    def info() -> None:  # pragma: no cover
        """
        Print Tyranno info.
        """
        Msg.write_info()


if __name__ == "__main__":
    cli()

"""
Command-line interface.

Original source: https://github.com/dmyersturnbull/tyrannosaurus
Copyright 2020–2021 Douglas Myers-Turnbull
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0
"""
from __future__ import annotations

import inspect
import logging
import os
import re
from pathlib import Path
from dataclasses import dataclass
from subprocess import check_call  # nosec
from typing import Optional, Sequence

import typer
from typer.models import ArgumentInfo, OptionInfo

from tyrannosaurus.clean import Clean
from tyrannosaurus.recipes import Recipe
from tyrannosaurus.envs import CondaEnv
from tyrannosaurus.context import Context
from tyrannosaurus.enums import DevStatus, License
from tyrannosaurus.helpers import _Env
from tyrannosaurus.new import New
from tyrannosaurus.sync import Sync
from tyrannosaurus.update import Update

logger = logging.getLogger(__package__)


def flag(name: str, desc: str, **kwargs) -> typer.Option:
    return typer.Option(False, "--" + name, help=desc, show_default=False, **kwargs)


class _DevNull:  # pragma: no cover
    """Pretends to write but doesn't."""

    def write(self, msg):
        pass

    def flush(self):
        pass

    def close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


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
        # avoid importing above, just in case a user runs --version, --info, or info on an improperly installed version
        from tyrannosaurus import __date__, __version__

        Msg.info(f"Tyrannosaurus v{__version__} ({__date__})")


@dataclass(frozen=True, repr=True)
class CliState:
    dry_run: bool = False
    verbose: bool = False

    def __post_init__(self):
        if self.verbose:
            logger.setLevel(logging.DEBUG)


def tyranno_main(
    version: bool = flag("version", "Write version and exit"),
    info: bool = flag("info", "Write info and exit (same as 'tyrannosaurus info')"),
):
    """
    Tyrannosaurus.
    Tyrannosaurus can create new modern Python projects from a template
    and synchronize metadata across the project.
    """
    if version or info:
        Msg.write_info()
        raise typer.Exit()


cli = typer.Typer(callback=tyranno_main, add_completion=True)


class CliCommands:
    """
    Commands for Tyrannosaurus.
    """

    @classmethod
    def commands(cls):
        return [cls.new, cls.sync, cls.env, cls.recipe, cls.update, cls.clean, cls.info, cls.build]

    _APACHE2 = typer.Option(License.apache2)
    _ENV_YAML = Path("environment.yml")

    @staticmethod
    @cli.command()
    def new(
        name: str = typer.Argument(
            "project", help="The name of the project, including any dashes or capital letters"
        ),
        license: str = typer.Option(
            "apache2", help=f"License name. One of {', '.join(s.name for s in License)}"
        ),
        user: Optional[str] = typer.Option(None, help="GitHub user or org"),
        authors: Optional[str] = typer.Option(None, help="Author names, comma-separated"),
        desc: str = typer.Option("A Python project", help="Short project description"),
        keywords: str = typer.Option(
            "", help="List of <6 keywords, comma-separated", show_default=False
        ),
        version: str = typer.Option("0.1.0", help="Your project's semantic version"),
        status: Optional[str] = typer.Option(
            None,
            help=inspect.cleandoc(
                rf"""
                PyPi classifier for dev status.
                One of: {", ".join(DevStatus)}
                [default: chosen by 'version']
                """
            ),
            show_choices=False,
        ),
        track: bool = flag("track", "Track an empty remote repo"),
        extras: bool = flag("extras", "Include uncommon files like codemeta.json"),
        tyranno: str = typer.Option(
            "current",
            help=inspect.cleandoc(
                r"""
                Tyrannosaurus version to use as the template.
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
        state = CliState(verbose=verbose)
        if version.startswith("v"):
            version = version[1:]
        if status is None:
            status = DevStatus.guess_from_version(version)
        else:
            status = DevStatus[status]
        if prompt:
            name = typer.prompt("name", type=str, default=name)
            description = typer.prompt("description", type=str, default="A new project")
            version = typer.prompt("version", type=str, default="0.1.0")
            if version.startswith("v"):
                version = version[1:]
            if status is None:
                status = DevStatus.guess_from_version(version)
            status = typer.prompt("status", type=DevStatus, default=status)
            license = typer.prompt("license", type=License, default="apache2").lower()
            user = typer.prompt(
                "user", type=str, prompt_suffix=" [default: from 'git config']", default=user
            )
            authors = typer.prompt(
                "authors",
                type=str,
                prompt_suffix=" [comma-separated; default: from 'git config']",
                default=authors,
            )
            description = typer.prompt("description", type=str, default=description)
            keywords = typer.prompt(
                "keywords", type=str, prompt_suffix=" [comma-separated]", default=keywords
            )
            track = typer.prompt("track", type=bool, default=track)
            tyranno = typer.prompt(
                "tyranno",
                type=str,
                prompt_suffix=" ['current', 'stable', 'latest', or a version]",
                default=tyranno,
            )
        e = _Env(user=user, authors=authors)
        keywords = keywords.split(",")
        path = Path(name)
        New(
            name,
            license_name=license,
            username=e.user,
            authors=e.authors,
            description=desc,
            keywords=keywords,
            version=version,
            status=status,
            should_track=track,
            tyranno_vr=tyranno.strip(" \r\n\t"),
            extras=extras,
            debug=state.verbose,
        ).create(path)
        Msg.success(f"Done! Created a new repository under {name}")
        Msg.success(
            "See https://tyrannosaurus.readthedocs.io/en/latest/guide.html#to-do-list-for-new-projects"
        )
        if track:
            repo_to_track = f"https://github.com/{e.user}/{name.lower()}.git"
            Msg.info(f"Tracking {repo_to_track}")
            Msg.info("Checked out branch main tracking origin/main")

    @staticmethod
    @cli.command()
    def sync(
        dry_run: bool = flag("dry-run", "Don't write; just output"),
        verbose: bool = flag("verbose", "Output more info"),
    ) -> None:  # pragma: no cover
        """
        Sync project metadata between configured files.
        """
        state = CliState(dry_run=dry_run, verbose=verbose)
        context = Context(Path(os.getcwd()), dry_run=state.dry_run)
        Msg.info("Syncing metadata...")
        Msg.info("Currently, only targets 'init' and 'recipe' are implemented.")
        targets = Sync(context).sync()
        Msg.success(f"Done. Synced to {len(targets)} targets: {targets}")

    @staticmethod
    @cli.command()
    def env(
        path: Path = typer.Option(_ENV_YAML, help="Write to this path"),
        name: Optional[str] = typer.Option(
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
        state = CliState(dry_run=dry_run, verbose=verbose)
        typer.echo("Writing environment file...")
        context = Context(Path(os.getcwd()), dry_run=state.dry_run)
        if name is None:
            name = context.project
        CondaEnv(name, dev=dev, extras=extras).create(context, path)
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
        state = CliState(dry_run=dry_run, verbose=verbose)
        dry_run = state.dry_run
        context = Context(Path(os.getcwd()), dry_run=dry_run)
        output_path = context.path / "recipes"
        Recipe(context).create(output_path)
        Msg.success(f"Generated a new recipe under {output_path}")

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
        context = Context(Path(os.getcwd()), dry_run=not auto_fix)
        updates, dev_updates = Update(context).update()
        Msg.info("Main updates:")
        for pkg, (old, up) in updates.items():
            Msg.info(f"    {pkg}:  {old} --> {up}")
        Msg.info("Dev updates:")
        for pkg, (old, up) in dev_updates.items():
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
        hard_delete: bool = flag(
            "hard-delete", "Use shutil.rmtree instead of moving to .tyrannosaurus"
        ),
        dry_run: bool = flag("dry-run", "Don't write; just output"),
        verbose: bool = flag("verbose", "Output more information"),
    ) -> None:  # pragma: no cover
        """
        Remove unwanted files.
        Deletes the contents of ``.tyrannosaurus``.
        Then trashes temporary and unwanted files and directories to a tree under ``.tyrannosaurus``.
        """
        state = CliState(verbose=verbose, dry_run=dry_run)
        dry_run = state.dry_run
        trashed = Clean(dists, aggressive, hard_delete, dry_run).clean(Path(os.getcwd()))
        Msg.info(f"Trashed {len(trashed)} paths.")

    @staticmethod
    @cli.command()
    def info() -> None:  # pragma: no cover
        """
        Print Tyrannosaurus info.
        """
        Msg.write_info()

    @staticmethod
    @cli.command()
    def build(
        bare: bool = flag("bare", "Don't use tox or virtualenv."),
        dry_run: bool = flag(
            "dry-run", "Don't run; just output. Useful for making a script template."
        ),
        verbose: bool = flag("verbose", "Output more info"),
    ) -> None:  # pragma: no cover
        """
        Syncs, builds, and tests your project.

        If ``bare`` is NOT set, runs:
            - tyrannosaurus sync
            - poetry lock
            - tox
            - tyrannosaurus clean

        ---------------------------------------------------------------

        If the ``bare`` IS set:
        Runs the commands without tox and without creating a new virtualenv.
        This can be useful if you're using Conda and have a dependency only available through Anaconda.
        It's also often faster.
        This command is for convenience and isn't very customizable.
        In this case, runs:
            - tyrannosaurus sync
            - poetry lock
            - pre-commit run check-toml
            - pre-commit run check-yaml
            - pre-commit run check-json
            - poetry check
            - poetry build
            - poetry install -v
            - poetry run pytest --cov
            - poetry run flake8 tyrannosaurus
            - poetry run flake8 docs
            - poetry run flake8 --ignore=D100,D101,D102,D103,D104,S101 tests
            - sphinx-build -b html docs docs/html
            - tyrannosaurus clean
            - pip install .

        ---------------------------------------------------------------
        """
        state = CliState(dry_run=dry_run, verbose=verbose)
        CliCommands.build_internal(bare=bare, dry=state.dry_run)

    @staticmethod
    def build_internal(bare: bool = False, dry: bool = False) -> Sequence[str]:
        split = CliCommands.build.__doc__.split("-" * 40)
        cmds = [
            line.strip(" -")
            for line in split[1 if bare else 0].splitlines()
            if line.strip().startswith("- ")
        ]
        if not dry:
            for cmd in cmds:
                Msg.info("Running: " + cmd)
                check_call(cmd.split(" "))  # nosec
        return cmds


def _fix_docstrings(commands):
    for f in commands:
        if "Args:" in [q.strip() for q in f.__doc__.splitlines()]:
            continue
        f.__doc__ += "\n" + " " * 8 + "Args:\n"
        for p in inspect.signature(f).parameters.values():
            arg = p.default
            if arg is not None:
                d = arg.default
                if isinstance(d, (OptionInfo, ArgumentInfo)) and hasattr(d, "default"):
                    d = d.default
                try:
                    h = re.compile(" +").sub(arg.help.replace("\n", "").strip(), " ")
                    f.__doc__ += " " * 12 + p.name + ": " + h + "\n"
                    if d is not False:
                        f.__doc__ += " " * (12 + 1 + len(p.name)) + f" [default: {str(d)}]\n"
                except (AttributeError, TypeError):
                    f.__doc__ += " " * 12 + p.name + " "


if __name__ == "__main__":
    cli()
# else:
# _fix_docstrings(CliCommands.commands())
# _fix_docstrings([tyranno_main])

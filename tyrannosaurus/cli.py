"""
Tyrannosaurus command-line interface.
"""

from __future__ import annotations

import logging
import os
import re
import shutil
from pathlib import Path
from subprocess import check_call
from typing import Optional, Union, Sequence
from typing import Tuple as Tup

import typer
from grayskull.base.factory import GrayskullFactory

from tyrannosaurus.context import _LiteralParser, _Context
from tyrannosaurus.helpers import (
    _SyncHelper,
    _TrashList,
    _License,
    _Env,
    _InitTomlHelper,
    _EnvHelper,
    _fast_scandir,
)

logger = logging.getLogger(__package__)
cli = typer.Typer()


def _new(
    name: str, license_name: Union[str, _License], username: str, authors: Sequence[str]
) -> None:
    if isinstance(license_name, str):
        license_name = _License[license_name.lower()]
    if Path(name).exists():
        raise FileExistsError("Path {} already exists".format(name))
    logger.info("Running git clone...")
    check_call(["git", "clone", "https://github.com/dmyersturnbull/tyrannosaurus.git", name])
    logger.info("Got git checkout. Fixing...")
    context = _Context(Path(os.getcwd()) / name)
    path = context.path
    toml_path = path / "pyproject.toml"
    parser = _LiteralParser(name, "0.1.0", username, authors)
    # remove tyrannosaurus-specific files
    # TODO permissionerror
    # os.chmod(str(path/'.git'), stat.S_IWRITE)
    # shutil.rmtree(str(path/'.git'))
    check_call(["rm", "-rf", str(path / ".git")])
    shutil.rmtree(str(path / "docs"))
    shutil.rmtree(str(path / "recipes"))
    # fix toml settings
    lines = toml_path.read_text(encoding="utf8").splitlines()
    env = _Env(user=username, authors=authors)
    new_lines = _InitTomlHelper(name, env.authors, license_name, env.user).fix(lines)
    toml_path.write_text("\n".join(new_lines), encoding="utf8")
    # copy license
    license_file = path / "tyrannosaurus" / "resources" / ("license_" + license_name.name + ".txt")
    if license_file.exists():
        text = parser.parse(license_file.read_text(encoding="utf8"))
        Path(path / "LICENSE.txt").write_text(text, encoding="utf8")
    # copy resources, overwriting
    for source in (path / "tyrannosaurus" / "resources").iterdir():
        if not Path(source).is_file():
            continue
        resource = Path(source).name
        if not resource.startswith("license_"):
            dest = path / Path(*str(resource).split("$"))
            if dest.name.startswith("-"):
                dest = Path(*reversed(dest.parents), "." + dest.name[1:])
            dest.parent.mkdir(parents=True, exist_ok=True)
            text = parser.parse(source.read_text(encoding="utf8"))
            dest.write_text(text, encoding="utf8")
    # rename some files
    Path(path / name).mkdir()
    Path(context.path / "recipes" / name).mkdir(parents=True)
    (path / "tyrannosaurus" / "__init__.py").rename(Path(path / name / "__init__.py"))
    shutil.rmtree(str(path / "tyrannosaurus"))


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
    env = _Env(user=user, authors=authors)
    _new(name, license, env.user, env.authors)
    typer.echo("Done! Created a new repository under {}".format(name))
    typer.echo(
        "See https://tyrannosaurus.readthedocs.io/en/latest/guide.html#to-do-list-for-new-projects"
    )


def _sync(path: Path, dry_run: bool) -> Sequence[str]:
    context = _Context(path, dry_run=dry_run)
    helper = _SyncHelper(context, dry_run)
    helper.fix_init()
    helper.fix_recipe()
    return [str(s) for s in context.targets]


@cli.command()
def sync(dry_run: bool = False) -> None:
    """
    Syncs project metadata between configured files.
    Args:
        dry_run: If set, does not touch the filesystem; only logs.
    """
    typer.echo("Syncing metadata...")
    typer.echo("Currently, only targets 'init' and 'recipe' are implemented.")
    targets = _sync(Path(os.getcwd()), dry_run)
    typer.echo("Done. Synced to {} targets: {}.".format(len(targets), ", ".join(targets)))


def _get_deps(name: str, dev: bool, extras: bool, dry_run: bool) -> Sequence[str]:
    context = _Context(os.getcwd(), dry_run=dry_run)
    path = Path(name + ".yml")
    if path.exists():
        context.back_up(path)
    deps = dict(context.deps)
    if dev:
        deps.update(context.dev_deps)
    return deps


def _env(path: Path, name: str, dev: bool, extras: bool, dry_run: bool) -> Sequence[str]:
    deps = _get_deps(name, dev, extras, dry_run)
    lines = _EnvHelper().process(name, deps, extras)
    path.write_text("\n".join(lines), encoding="utf8")
    return lines


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
    context = _Context(os.getcwd(), dry_run=dry_run)
    if name is None:
        name = context.project
    deps = _get_deps(name, dev, extras, dry_run)
    typer.echo("Writing environment with {} dependencies to {} ...".format(len(deps), path))
    lines = _EnvHelper().process(name, deps, extras)
    path.write_text("\n".join(lines), encoding="utf8")
    typer.echo("Wrote environment {}".format(path))


def _recipe(path: Path, dry_run: bool) -> Path:
    context = _Context(path, dry_run=dry_run)
    output_path = context.path / "recipes"
    if output_path.exists():
        context.trash(output_path, False)
    if (output_path / context.project).exists():
        (output_path / context.project).rmdir()
    (output_path / context.project).mkdir(parents=True)
    skull = GrayskullFactory.create_recipe("pypi", context.poetry("name"), "")
    skull.generate_recipe(str(output_path), mantainers=context.source("maintainers").split(","))
    logger.debug("Generated a new recipe at {}".format(output_path))
    helper = _SyncHelper(context, dry_run)
    helper.fix_recipe()
    logger.debug("Fixed recipe at {}".format(output_path))
    return output_path


@cli.command()
def recipe(dry_run: bool = False) -> None:
    """
    Generates a Conda recipe using grayskull.
    Args:
        dry_run: If set, does not touch the filesystem; only logs.
    """
    # grayskull pypi ${yourprojectname} --maintainers ${maintainers} --output recipes/
    output_path = _recipe(Path(os.getcwd()), dry_run)
    typer.echo("Generated a new recipe at {}".format(output_path))


def _clean(
    path: Path, dists: bool, aggressive: bool, hard_delete: bool, dry_run: bool
) -> Sequence[Tup[Path, Optional[Path]]]:
    context = _Context(path, dry_run=dry_run)
    logger.info("Clearing .tyrannosaurus")
    trashed = []
    destroyed = context.destroy_tmp()
    if destroyed:
        trashed.append(context.tmp_path)
    trash = _TrashList(dists, aggressive)
    # we're going to do these in order to save time overall
    for p in trash.get_list():
        tup = context.trash(p, hard_delete)
        if tup[0] is not None:
            trashed.append(tup)
    for p in _fast_scandir(path, trash):
        if trash.should_delete(p):
            tup = context.trash(p, hard_delete)
            if tup[0] is not None:
                trashed.append(tup)
    return trashed


@cli.command()
def clean(
    dists: bool = False, aggressive: bool = False, hard_delete: bool = False, dry_run: bool = False
) -> None:
    """
    Deletes the contents of ``.tyrannosaurus``, then moves temporary and unwanted
    files and directories to a tree under ``.tyrannosaurus``.
    Args:
        dists: Remove dists
        aggressive: Delete additional files, including .swp, .ipython_checkpoints, and dist.
        hard_delete: If true, call shutil.rmtree instead.
        dry_run: If set, does not touch the filesystem; only logs.
    """
    trashed = _clean(Path(os.getcwd()), dists, aggressive, hard_delete, dry_run)
    typer.echo("Trashed {} paths.".format(len(trashed)))


def _info() -> Sequence[str]:
    from tyrannosaurus import metadata, __version__, __date__

    return ["Tyrannosaurus version {} ({})".format(__version__, __date__)]


@cli.command()
def info() -> None:
    """
    Prints Tyrannosaurus info.
    """
    for line in _info():
        typer.echo(line)


class Commands:
    new = _new
    sync = _sync
    recipe = _recipe
    info = _info
    clean = _clean


if __name__ == "__main__":
    cli()

__all__ = [Commands]

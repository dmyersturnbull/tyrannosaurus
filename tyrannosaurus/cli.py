"""
Tyrannosaurus command-line interface.
"""

from __future__ import annotations

import logging
import os
import enum
import shutil
from pathlib import Path
from subprocess import check_call
from typing import Optional, Union, Sequence, Mapping
from typing import Tuple as Tup

import typer
from grayskull.base.factory import GrayskullFactory

from tyrannosaurus.context import _LiteralParser, _Context
from tyrannosaurus.helpers import _SyncHelper, _TrashList

logger = logging.getLogger(__package__)
cli = typer.Typer()


class _License(enum.Enum):
    apache2 = "apache2"
    cc0 = "cc0"
    ccby = "cc-by"
    ccbync = "cc-by-nc"
    gpl3 = "gpl3"
    lgpl3 = "lgpl3"
    mit = "mit"

    def full_name(self) -> str:
        return dict(apache2="Apache-2.0", mit="MIT",).get(self.name, "")


def _set_lines(lines: Sequence[str], prefixes: Mapping[str, Union[int, str]]):
    new_lines = []
    set_val = set()
    for line in lines:
        new_line = line
        for key, value in prefixes.items():
            if isinstance(value, str):
                value = '"' + value + '"'
            if line.startswith(key + " = ") and key not in set_val:
                new_line = key + " = " + value
                set_val.add(key)
        new_lines.append(new_line)
    return new_lines


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
    # fix toml settings
    lines = toml_path.read_text(encoding="utf8").splitlines()
    new_lines = _set_lines(
        lines,
        dict(
            name=name,
            version="0.1.0",
            description="A new project",
            authors=str(authors),
            maintainers=str(authors),
            license=license_name.full_name(),
            keywords=str(["a new", "python project"]),
            homepage="https://github.com/{}/{}".format(username, name),
            repository="https://github.com/{}/{}".format(username, name),
            documentation="https://{}.readthedocs.io".format(name),
            build="https://github.com/{}/{}/actions".format(username, name),
            issues="https://github.com/{}/{}/issues".format(username, name),
            source="https://github.com/{}/{}".format(username, name),
        ),
    )
    # this one is fore tool.tyrannosaurus.sources
    # this is a hack
    new_lines = _set_lines(new_lines, dict(maintainers=username))
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
    Path(context.path / "recipes" / name).mkdir()
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
    if user is None:
        user = os.environ.get("USERNAME")
    if authors is None:
        authors = os.environ.get("USERNAME")
    _new(name, license, user, authors.split(","))
    typer.echo("Done! Created a new repository under {}".format(name))
    typer.echo("Make sure to modify your pyproject.toml and README.md.")
    typer.echo("Also consider adding 'tyrannosaurus sync' in tox.ini.")


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


def fast_scandir(topdir, trash):
    subdirs = [Path(f.path) for f in os.scandir(topdir) if Path(f).is_dir()]
    for dirname in list(subdirs):
        if (
            dirname.is_dir()
            and dirname.name
            not in {".tox", ".pytest_cache", ".git", ".idea", "docs", "__pycache__"}
            and dirname.name not in {str(s) for s in trash.get_list()}
        ):
            subdirs.extend(fast_scandir(dirname, trash))
    return subdirs


def _clean(
    path: Path, aggressive: bool, hard_delete: bool, dry_run: bool
) -> Sequence[Tup[Path, Optional[Path]]]:
    context = _Context(path, dry_run=dry_run)
    trash = _TrashList(aggressive)
    trashed = []
    # we're going to do these in order to save time overall
    for p in trash.get_list():
        tup = context.trash(p, hard_delete)
        trashed.append(tup)
    for p in fast_scandir(path, trash):
        if trash.should_delete(p):
            tup = context.trash(p, hard_delete)
            trashed.append(tup)
    return trashed


@cli.command()
def clean(aggressive: bool = False, hard_delete: bool = False, dry_run: bool = False) -> None:
    """
    Deletes the contents of ``.tyrannosaurus``, then moves temporary and unwanted
    files and directories to a tree under ``.tyrannosaurus``.
    Args:
        aggressive: Delete additional files, including .swp, .ipython_checkpoints, and dist.
        hard_delete: If true, call shutil.rmtree instead.
        dry_run: If set, does not touch the filesystem; only logs.
    """
    trashed = _clean(Path(os.getcwd()), aggressive, hard_delete, dry_run)
    typer.echo("Trashed {} paths.".format(len(trashed)))


def _reqs() -> Sequence[str]:
    from tyrannosaurus import metadata, __version__, __date__

    rex = []
    on = False
    for line in str(metadata["description"]).splitlines():
        if ".++++++++++++." in line:
            on = True
        if line.strip() == "```":
            on = False
        if on:
            rex.append(line)
    return ["Tyrannosaurus version {} ({})".format(__version__, __date__), *rex]


@cli.command()
def reqs() -> None:
    """
    Prints Tyrannosaurus info.
    """
    for line in _reqs():
        typer.echo(line)


if __name__ == "__main__":
    cli()

__all__ = ["new", "sync", "recipe", "reqs"]

"""
Context for Tyrannosaurus.
"""

from __future__ import annotations

import enum
import logging
import os
import shutil
from datetime import date, datetime
from pathlib import Path, PurePath
from typing import Any, Mapping, Optional, Sequence
from typing import Tuple as Tup
from typing import Union

import tomlkit

logger = logging.getLogger(__package__)
today = date.today()
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")


class DevStatus(enum.Enum):
    planning = 1
    pre_alpha = 2
    alpha = 3
    beta = 4
    production = 5
    mature = 6
    inactive = 7

    @property
    def true_name(self) -> str:
        """
        A nice name, like "pre-alpha".
        """
        return self.name.replace("_", "-")

    @property
    def description(self) -> str:
        """
        A fragment like "a production state" or "an alpha state"
        """
        name = self.true_name
        article = "an" if name[0] in ["a", "e", "i", "o", "u", "h"] else "a"
        return f"{article} {name} state"

    @property
    def pypi(self) -> str:
        """
        A string that is recognized as a PyPi classifier.
        """
        name = self.name.replace("_", " ").title().replace(" ", "-")
        return f"{self.value} - {name}"

    @property
    def dunder(self) -> str:
        """
        A string that works for __status__
        """
        return "Production" if self.value >= 5 else "Development"

    @classmethod
    def guess_from_version(cls, vr: str) -> DevStatus:
        """
        Makes a really rough guess for the status from a semantic version string::

            - Guesses planning for 0.0.x (these are not semantic versions).
            - Guesses alpha for pre-1.0
            - Guesses production for 1.0+

        Arguments:
            vr: A semantic version like "0.1.x"; can also start with 0.0.
        """
        if vr.startswith("v"):
            vr = vr[1:]
        if vr.startswith("0.0."):
            return DevStatus.planning
        elif vr.startswith("1."):
            return DevStatus.production
        else:
            return DevStatus.alpha


class Toml:
    """A thin wrapper around toml to make getting values easier."""

    @classmethod
    def read(cls, path: Union[PurePath, str]) -> Toml:
        return Toml(tomlkit.loads(Path(path).read_text(encoding="utf8")))

    def __init__(self, x: Mapping[str, Any]) -> None:
        self.x = x

    def __getitem__(self, items: str):
        if not isinstance(items, str):
            raise AssertionError(f"Failed with '{items}'")
        if "." not in items:
            return self.x[items]
        at = self.x
        for item in items.split("."):
            at = at[item]
        if isinstance(at, dict):
            return Toml(at)
        return at

    def __contains__(self, items):
        if not isinstance(items, str):
            raise AssertionError(f"Failed with '{items}'")
        if "." not in items:
            return items in self.x
        at = self.x
        for item in items.split("."):
            if item not in at:
                return False
            at = at[item]
        return True

    def get(self, items: str, default: Any = None) -> Optional[Any]:
        try:
            return self[items]
        except KeyError:
            return default

    def items(self):
        return self.x.items()

    def keys(self):
        return self.x.keys()

    def __str__(self):
        return f"{self.__class__.__name__} ({repr(self.x)})"

    def __repr__(self):
        return f"{self.__class__.__name__} ({repr(self.x)})"

    def __eq__(self, other):
        return isinstance(other, Toml) and self.x == other.x


class TomlBuilder:
    def __init__(self):
        self._dict = {}

    def add(self, key: str, value: Any):
        at = self._dict
        if "." in key:
            for k in key.split(".")[:-1]:
                if k not in at:
                    at[k] = {}
                at = at[k]
        at[key.split(".")[-1]] = value
        return self

    def build(self) -> Toml:
        return Toml(self._dict)


class LiteralParser:
    def __init__(
        self,
        project: str,
        user: Optional[str],
        authors: Optional[Sequence[str]],
        description: str,
        keywords: Sequence[str],
        version: str,
        status: DevStatus,
        license_name: str,
        tyranno_vr: str,
    ):
        self.project = project.lower()
        # TODO doing this in two places
        self.pkg = project.replace("_", "").replace("-", "").replace(".", "").lower()
        self.user = user
        self.authors = authors
        self.description = description
        self.keywords = keywords
        self.version = version
        self.status = status
        self.license = str(license_name)
        self.license_official = dict(
            apache2="Apache-2.0",
            cc0="CC0-1.0",
            ccby="CC-BY-4.0",
            ccybync="CC-BY-NC-4.0",
            gpl2="GPL-2.0-or-later",
            gpl3="GPL-3.0-or-later",
            mit="MIT",
        ).get(str(license_name), "TODO:fix:" + str(license_name))
        self.license_name = dict(
            apache2="Apache 2.0",
            cc0="CC0 1.0",
            ccby="CC BY 4.0",
            ccybync="CC BY NC 4.0",
            gpl2="GPL 2.0",
            gpl3="GPL 3.0",
            mit="MIT",
        ).get(str(license_name), "TODO:fix:" + str(license_name))
        self.tyranno_vr = tyranno_vr

    def parse(self, s: str) -> str:
        s = (
            s.replace("${today}", str(today))
            .replace("${today.year}", str(today.year))
            .replace("${today.month}", str(today.month))
            .replace("${today.Month}", today.strftime("%B"))
            .replace("${today.day}", str(today.day))
            .replace("${now}", timestamp)
            .replace("${now.hour}", str(now.hour))
            .replace("${now.minute}", str(now.minute))
            .replace("${now.second}", str(now.second))
            .replace("${project}", self.project.lower())
            .replace("${Project}", self.project.capitalize())
            .replace("${PROJECT}", self.project.upper())
            .replace("${pkg}", self.pkg)
            .replace("${license}", self.license)
            .replace("${license.official}", self.license_official)
            .replace("${license.name}", self.license_name)
            .replace("${version}", self.version)
            .replace("${status.Name}", self.status.name.capitalize())
            .replace("${status.name}", self.status.name)
            .replace("${status.pypi}", self.status.pypi)
            .replace("${status.dunder}", self.status.dunder)
            .replace("${status.Description}", self.status.description.capitalize())
            .replace("${status.description}", self.status.description)
            .replace("${Description}", self.description.capitalize())
            .replace("${description}", self.description)
            .replace("${keywords}", str(self.keywords))
            .replace("${keywords.yaml0}", "\n- ".join(self.keywords) + "\n")
            .replace("${keywords.yaml2}", "\n  - ".join(self.keywords) + "\n")
            .replace("${keywords.yaml4}", "\n    - ".join(self.keywords) + "\n")
            .replace("${KEYWORDS}", str([k.upper() for k in self.keywords]))
            .replace("${tyranno.version}", self.tyranno_vr)
        )
        if self.user is not None:
            s = s.replace("${user}", self.user)
        if self.authors is not None:
            s = s.replace("${authors}", str(self.authors))
            s = s.replace("${authors.str}", ", ".join(self.authors))
        return s


class Source:
    @classmethod
    def parse(cls, s: str, toml: Toml) -> Union[str, Sequence]:
        from tyrannosaurus import __version__ as global_tyranno_vr

        project = toml["tool.poetry.name"]
        version = toml["tool.poetry.version"]
        description = toml["tool.poetry.description"]
        authors = toml["tool.poetry.authors"]
        keywords = toml["tool.poetry.keywords"]
        license_name = toml["tool.poetry.license"]
        status = DevStatus.guess_from_version(version)
        if isinstance(s, str) and s.startswith("'") and s.endswith("'"):
            return (
                LiteralParser(
                    project=project,
                    user=None,
                    authors=authors,
                    description=description,
                    keywords=keywords,
                    version=version,
                    status=status,
                    license_name=license_name,
                    tyranno_vr=global_tyranno_vr,
                )
                .parse(s)
                .strip("'")
            )
        elif isinstance(s, str):
            value = toml[s]
            return str(value)
        else:
            # TODO not great
            return list(s)


class Context:
    def __init__(self, path: Union[Path, str], data=None, dry_run: bool = False):
        self.path = Path(path).resolve()
        if data is None:
            data = Toml.read(Path(self.path) / "pyproject.toml")
        self.data = data
        self.options = {k for k, v in data.get("tool.tyrannosaurus.options", {}).items() if v}
        self.targets = {k for k, v in data.get("tool.tyrannosaurus.targets", {}).items() if v}
        self.sources = {
            k: Source.parse(v, data)
            for k, v in data.get("tool.tyrannosaurus.sources", {}).items()
            if v
        }
        self.tmp_path = self.path / ".tyrannosaurus"
        self.dry_run = dry_run

    @property
    def project(self) -> str:
        return str(self.data["tool.poetry.name"])

    @property
    def version(self) -> str:
        return str(self.data["tool.poetry.version"])

    @property
    def deps(self) -> Mapping[str, str]:
        return self.data["tool.poetry.dependencies"]

    @property
    def dev_deps(self) -> Mapping[str, str]:
        return self.data["tool.poetry.dev-dependencies"]

    @property
    def extras(self) -> Mapping[str, str]:
        return self.data["tool.poetry.extras"]

    def destroy_tmp(self) -> bool:
        if not self.dry_run:
            if self.tmp_path.exists():
                shutil.rmtree(str(self.tmp_path))
                return True
        return False

    def back_up(self, path: Union[Path, str]) -> None:
        path = Path(path)
        self.check_path(path)
        bak = self.get_bak_path(path)
        if not self.dry_run:
            bak.parent.mkdir(exist_ok=True, parents=True)
            shutil.copyfile(str(path), str(bak))
            logger.debug(f"Generated backup of {path} to {bak}")

    def trash(self, path: str, hard_delete: bool) -> Tup[Optional[Path], Optional[Path]]:
        return self.delete_exact_path(self.path / path, hard_delete=hard_delete)

    def delete_exact_path(
        self, path: Path, hard_delete: bool
    ) -> Tup[Optional[Path], Optional[Path]]:
        if not path.exists():
            return None, None
        self.check_path(path)
        if hard_delete:
            if not self.dry_run:
                shutil.rmtree(path)
            logger.debug(f"Deleted {path}")
            return path, None
        else:
            bak = self.get_bak_path(path)
            bak.parent.mkdir(exist_ok=True, parents=True)
            if not self.dry_run:
                os.rename(str(path), str(bak))
            logger.debug(f"Trashed {path} to {bak}")
            return path, bak

    def get_bak_path(self, path: Union[Path, str]):
        if not str(path).startswith(str(self.path)):
            path = self.path / path
        path = Path(path).resolve()
        suffix = path.suffix + "." + timestamp + ".bak"
        return self.tmp_path / path.relative_to(self.path).with_suffix(suffix)

    def check_path(self, path: Union[Path, str]) -> None:
        # none of these should even be possible, but let's be 100% sure
        path = Path(path)
        if path.resolve() == self.path.resolve():
            raise ValueError(f"Cannot touch {path.resolve()}: identical to {self.path.resolve()}")
        if not path.exists():
            raise FileNotFoundError(f"Path {path} does not exist")
        for parent in path.resolve().parents:
            if parent.resolve() == self.path.resolve():
                return
        raise ValueError(
            f"Cannot touch {path.resolve()}: not under the parent dir {self.path.resolve()}"
        )

    def item(self, key: str):
        return self.data[key]

    def poetry(self, key: str):
        return self.data["tool.poetry." + key]

    def has_opt(self, key: str):
        return key in self.options

    def source(self, key: str):
        return self.sources[key]

    def path_source(self, key: str) -> Path:
        output_path = self.path
        for s in str(self.source(key)).split("/"):
            output_path /= s
        return output_path

    def has_target(self, key: str) -> bool:
        return key in self.targets


__all__ = ["DevStatus", "Toml", "TomlBuilder", "LiteralParser", "Context"]

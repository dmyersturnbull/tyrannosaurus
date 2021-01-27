"""
Original source: https://github.com/dmyersturnbull/tyrannosaurus
Copyright 2020–2021 Douglas Myers-Turnbull
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0

Small support classes.
"""

from __future__ import annotations
import enum
from pathlib import PurePath, Path
from typing import Union, Mapping, Any, Optional

import requests
import tomlkit


class DevStatus(str, enum.Enum):
    planning = "planning"
    pre_alpha = "pre-alpha"
    alpha = "alpha"
    beta = "beta"
    production = "production"
    mature = "mature"
    inactive = "inactive"

    @property
    def true_name(self) -> str:
        """
        A nice name, like "pre-alpha".
        """
        return self.name.replace("_", "-")

    @property
    def true_value(self) -> int:
        """
        1 for planning, 2 for pre-alpha, ... .
        Same as for PyPi classifiers.
        """
        return dict(
            planning=1,
            pre_alpha=2,
            alpha=3,
            beta=4,
            production=5,
            mature=6,
            inactive=7,
        )[self.name]

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
        return f"{self.true_value} - {name}"

    @property
    def dunder(self) -> str:
        """
        A string that works for __status__
        """
        return "Production" if self.true_value >= 5 else "Development"

    @classmethod
    def guess_from_version(cls, version: str) -> DevStatus:
        """
        Makes a really rough guess for the status from a semantic version string::

            - Guesses planning for 0.0.x (these are not semantic versions).
            - Guesses alpha for pre-1.0
            - Guesses production for 1.0+

        Arguments:
            version: A semantic version like "0.1.x"; can also start with 0.0.
        """
        if version.startswith("v"):
            version = version[1:]
        if version.startswith("0.0."):
            return DevStatus.planning
        elif version.startswith("1."):
            return DevStatus.production
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


class License(str, enum.Enum):
    agpl3 = "agpl3"
    apache2 = "apache2"
    cc0 = "cc0"
    ccby = "ccby"
    ccbync = "ccbync"
    gpl3 = "gpl3"
    lgpl3 = "lgpl3"
    mit = "mit"
    mpl2 = "mpl2"

    @classmethod
    def of(cls, value: Union[str, License]) -> License:
        if isinstance(value, License):
            return value
        for v in list(License):
            if v.spdx == value:
                return v
            if v.name == value:
                return v
            if v.full_name == value:
                return v
        raise LookupError(f"Could not find {value}")

    @property
    def url(self) -> str:
        return f"https://spdx.org/licenses/{self.spdx}.html"

    @property
    def spdx(self) -> str:
        return dict(
            agpl3="AGPL-3.0-or-later",
            apache2="Apache-2.0",
            cc0="CC0-1.0",
            ccby="CC-BY-4.0",
            ccbync="CC-BY-NC-4.0",
            gpl2="GPL-2.0-or-later",
            gpl3="GPL-3.0-or-later",
            lgpl3="LGPL-3.0-or-later",
            mit="MIT",
            mpl2="MPL-2.0",
        )[self.name]

    @property
    def full_name(self) -> str:
        return dict(
            apache2="Apache License 2.0",
            cc0="CC0 1.0",
            ccby="CC BY 4.0",
            ccbync="CC BY NC 4.0",
            gpl2="GNU General Public License 2.0",
            gpl3="GNU General Public License 3.0",
            lgpl3="GNU Lesser General Public License 3.0",
            mit="MIT License",
            mpl2="Mozilla Public License 2.0",
            agpl3="GNU Affero General Public License 3.0",
        )[self.name]

    @property
    def family(self) -> str:
        return dict(
            apache2="Apache",
            cc0="CC",
            ccby="CC",
            ccbync="CC",
            gpl2="GPL",
            gpl3="GPL",
            lgpl3="GPL",
            mit="MIT",
            mpl2="Mozilla",
            agpl3="GPL",
        )[self.name]

    def download_license(self) -> str:
        return self._read_url(self.license_url)

    def download_header(self) -> str:
        if self is License.mit:
            return ""
        return self._read_url(self.header_url)

    def _read_url(self, url: str) -> str:
        response = requests.get(url)
        if response.status_code > 400:
            raise ValueError(f"Status code {response.status_code} for url {url}")
        return response.text

    @property
    def license_url(self) -> str:
        return self.header_url.replace("-header", "")

    @property
    def header_url(self) -> str:
        name = dict(
            apache2="apache",
            ccby="cc_by",
            ccbync="cc_by_nc",
            gpl3="gpl3",
            lgpl3="lgpl",
            mit="mit",
            mpl2="mpl",
        )[self.name]
        return f"https://raw.githubusercontent.com/licenses/license-templates/master/templates/{name}-header.txt"


__all__ = ["DevStatus", "License", "Toml", "TomlBuilder"]

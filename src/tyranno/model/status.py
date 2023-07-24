# SPDX-License-Identifier: Apache-2.0
# Source: https://github.com/dmyersturnbull/tyranno
"""

"""
import enum
import re
from inspect import cleandoc
from typing import TYPE_CHECKING, Self

_PATTERN = re.compile(
    cleandoc(
        r"""
        ^
        (?P<major>0|[1-9]\d*)
        \.(?P<minor>0|[1-9]\d*)
        \.(?P<patch>0|[1-9]\d*)
        (?:-(?P<pre>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?
        (?:\+(?P<meta>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?
        $
        """,
    ),
)


class DevStatus(enum.Enum):
    planning = 1
    pre_alpha = 2
    alpha = 3
    beta = 4
    production = 5
    mature = 6
    inactive = 7

    @property
    def name(self) -> str:
        """
        A nice name, like "pre-alpha".
        """
        return self.name.replace("_", "-")

    @property
    def pypi_classifier(self) -> str:
        """
        A string that is recognized as a PyPi classifier.
        """
        name = self.name.replace("_", " ").title().replace(" ", "-")
        return f"{self.value} - {name}"

    @classmethod
    def guess_from_version(cls, version: str) -> Self:
        """
        Makes a really rough guess for the status from a semantic version string.
        """
        if m := _PATTERN.fullmatch(version) is None:
            return DevStatus.planning
        match m.groups():
            case ("0", "0", "0", _, _):
                return DevStatus.planning
            case ("0", "0", _, _):
                return DevStatus.pre_alpha
            case (_, _, _, pre, _) if pre.startswith("alpha"):
                return DevStatus.alpha
            case (_, _, _, pre, _) if pre.startswith("beta"):
                return DevStatus.beta
            case ("0", _, _, _, _):
                return DevStatus.alpha
            case ("1", _, _, _, _):
                return DevStatus.production
            case _:
                return DevStatus.mature

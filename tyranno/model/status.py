# SPDX-License-Identifier Apache-2.0
# Source: https://github.com/dmyersturnbull/tyranno
"""

"""
import enum
from typing import Self


class DevStatus(enum.Enum):
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
        return {
            "planning": 1,
            "pre_alpha": 2,
            "alpha": 3,
            "beta": 4,
            "production": 5,
            "mature": 6,
            "inactive": 7,
        }[self.name]

    @property
    def description(self) -> str:
        """
        A fragment like "a production state" or "an alpha state".
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
        A string that works for ``__status__``.
        """
        return "Production" if self.true_value >= 5 else "Development"

    @classmethod
    def guess_from_version(cls, version: str) -> Self:
        """
        Makes a really rough guess for the status from a semantic version string.

        Behavior::

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

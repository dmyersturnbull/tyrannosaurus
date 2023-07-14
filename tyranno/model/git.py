# SPDX-License-Identifier Apache-2.0
# Source: https://github.com/dmyersturnbull/tyranno
"""

"""
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Self

from loguru import logger


@dataclass(frozen=True, eq=True)
class GitDescription:
    """
    Data collected from running ``git describe --long --dirty --broken --abbrev=40 --tags``.
    """

    tag: str
    commits: str
    hash: str
    is_dirty: bool
    is_broken: bool

    @classmethod
    def call(cls, repo_dir: Path) -> Self:
        cmd = "git describe --long --dirty --broken --abbrev=40 --tags".split(" ")
        text = subprocess.check_output(cmd, cwd=repo_dir, encoding="utf-8")  # noqa: S603,S607
        pat = re.compile(r"([\d.]+)-(\d+)-g([0-9a-h]{40})(?:-([a-z]+))?")
        # ex: 1.8.6-43-g0ceb89d3a954da84070858319f177abe3869752b-dirty
        if m := pat.fullmatch(text):
            return cls(
                m.group(1),
                m.group(2),
                m.group(3),
                m.group(4) == "dirty",
                m.group(4) == "broken",
            )
        raise ValueError(f"Bad git describe string {text}")


@dataclass(frozen=True)
class GitConfig:
    user: str
    email: str

    @classmethod
    def call(cls) -> Self:
        return cls(
            subprocess.check_output(
                ["git", "config", "user.name"], encoding="utf8"
            ).strip(),  # noqa: S603,S607
            subprocess.check_output(
                ["git", "config", "user.email"], encoding="utf8"
            ).strip(),  # noqa: S603,S607
        )


@dataclass(frozen=True)
class GitClone:
    repo_url: str
    repo_path: Path

    @classmethod
    def call(cls, repo_url: str, repo_path: Path) -> Self:
        cmd = ["git", "clone", repo_url]
        result = subprocess.check_output(
            cmd, cwd=repo_path, encoding="utf8"
        ).strip()  # noqa: S603,S607
        for line in result.splitlines():
            logger.debug(line)
        return cls(repo_url, repo_path)


__all__ = ["GitDescription", "GitConfig"]

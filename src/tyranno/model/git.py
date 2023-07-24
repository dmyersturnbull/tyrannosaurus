# SPDX-License-Identifier: Apache-2.0
# Source: https://github.com/dmyersturnbull/tyranno
"""

"""
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Self

from loguru import logger

# ex: 1.8.6-43-g0ceb89d3a954da84070858319f177abe3869752b-dirty
_GIT_DESC_PATTERN = re.compile(r"([\d.]+)-(\d+)-g([0-9a-h]{40})(?:-([a-z]+))?")


def _call(cmd: list[str], cwd: Path = Path.cwd()) -> str:
    return subprocess.check_output(cmd, cwd=cwd, encoding="utf-8").strip()  # noqa: S603,S607


@dataclass(frozen=True, eq=True)
class GitDescription:
    """
    Data collected from running `git describe --long --dirty --broken --abbrev=40 --tags`.
    """

    tag: str
    commits: str
    hash: str
    is_dirty: bool
    is_broken: bool

    @classmethod
    def call(cls, repo_dir: Path) -> Self:
        cmd = "git describe --long --dirty --broken --abbrev=40 --tags".split(" ")
        text = _call(cmd, cwd=repo_dir)
        if m := _GIT_DESC_PATTERN.fullmatch(text) is None:
            msg = f"Bad git describe string {text}"
            raise ValueError(msg)
        return cls(
            m.group(1),
            m.group(2),
            m.group(3),
            m.group(4) == "dirty",
            m.group(4) == "broken",
        )


@dataclass(frozen=True)
class GitConfig:
    user: str
    email: str

    @classmethod
    def call(cls) -> Self:
        return cls(
            _call(["git", "config", "user.name"]),
            _call(["git", "config", "user.email"]),
        )


@dataclass(frozen=True)
class GitClone:
    repo_url: str
    repo_path: Path

    @classmethod
    def call(cls, repo_url: str, repo_path: Path) -> Self:
        result = _call(["git", "clone", repo_url], cwd=repo_path)
        for line in result.splitlines():
            logger.debug(line)
        return cls(repo_url, repo_path)


__all__ = ["GitDescription", "GitConfig"]

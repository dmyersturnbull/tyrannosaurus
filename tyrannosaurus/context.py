"""
Original source: https://github.com/dmyersturnbull/tyrannosaurus
Copyright 2020–2021 Douglas Myers-Turnbull
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0

Holds a "context" of metadata that was read from a pyproject.toml.
"""

from __future__ import annotations

import logging
import os
import re
import shutil
from pathlib import Path
from typing import Mapping, Optional, Sequence
from typing import Tuple as Tup
from typing import Union

from tyrannosaurus import TyrannoInfo
from tyrannosaurus.enums import DevStatus, Toml, License
from tyrannosaurus.parser import LiteralParser

logger = logging.getLogger(__package__)


class Source:
    @classmethod
    def parse(cls, s: str, toml: Toml) -> Union[str, Sequence]:
        from tyrannosaurus import TyrannoInfo

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
                    tyranno_vr=TyrannoInfo.version,
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
    def description(self) -> str:
        return str(self.data["tool.poetry.description"])

    @property
    def license(self) -> License:
        return License.of(self.data["tool.poetry.license"])

    @property
    def build_sys_reqs(self) -> Mapping[str, str]:
        pat = re.compile(r" *^([A-Za-z][A-Za-z0-9-_.]*) *(.*)$")
        dct = {}
        for entry in self.data["build-system.requires"]:
            match = pat.fullmatch(entry)
            dct[match.group(1)] = match.group(2)
        return dct

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
        suffix = path.suffix + "." + TyrannoInfo.timestamp + ".bak"
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


__all__ = ["Context"]

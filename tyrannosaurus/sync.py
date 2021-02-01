"""
Original source: https://github.com/dmyersturnbull/tyrannosaurus
Copyright 2020–2021 Douglas Myers-Turnbull
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0

Module that syncs metadata from pyproject.toml.
"""
from __future__ import annotations

import logging
import re
import textwrap
from pathlib import Path
from typing import Mapping, Optional, Sequence, Union

from tyrannosaurus.context import Context
from tyrannosaurus.envs import CondaEnv

logger = logging.getLogger(__package__)


class Sync:
    def __init__(self, context: Context):
        self.context = context

    def sync(self) -> Sequence[str]:  # pragma: no cover
        self.fix_init()
        self.fix_dockerfile()
        self.fix_pyproject()
        self.fix_recipe()
        self.fix_env()
        self.fix_codemeta()
        self.fix_citation()
        return [str(s) for s in self.context.targets]

    def has(self, key: str):
        return self.context.has_target(key)

    def fix_dockerfile(self) -> Sequence[str]:  # pragma: no cover
        dockerfile = self.context.path / "Dockerfile"
        if not self.has("dockerfile") or not dockerfile.exists():
            return []
        oci_vr = "org.opencontainers.image.version"
        oci_desc = "org.opencontainers.image.description"
        vr = self.context.version
        desc = self.context.description
        return self._replace_substrs(
            dockerfile,
            {
                "LABEL version=": f'LABEL version="{vr}"',
                f"LABEL {oci_vr}=": f'LABEL {oci_vr}="{vr}"',
                f"LABEL {oci_desc}=": f'LABEL {oci_desc}="{desc}"',
            },
        )

    def fix_init(self) -> Sequence[str]:  # pragma: no cover
        if self.has("init"):
            return self.fix_init_internal(self.context.path / self.context.project / "__init__.py")
        return []

    def fix_init_internal(self, init_path: Path) -> Sequence[str]:
        status = self.context.source("status")
        cright = self.context.source("copyright")
        dadate = self.context.source("date")
        return self._replace_substrs(
            init_path,
            {
                "__status__ = ": f'__status__ = "{status}"',
                "__copyright__ = ": f'__copyright__ = "{cright}"',
                "__date__ = ": f'__date__ = "{dadate}"',
            },
        )

    def fix_pyproject(self) -> Sequence[str]:
        if not self.has("pyproject"):
            return []
        version = self.context.version
        cz_version = self.context.data.get("tool.commitizen.version")
        version_from = self.context.data.get("tool.tyrannosaurus.sources.version")
        if cz_version is not None and cz_version != version:
            logger.error(f"Commitizen version {cz_version} != {version_from} version {version}")
        return []  # TODO: lying

    def fix_citation(self) -> Sequence[str]:
        path = self.context.path / "CITATION.cff"
        if not self.has("citation") and path.exists():
            return []
        vr = self.context.version
        desc = self.context.description
        return self._replace_substrs(
            path,
            {
                "version:": f"version: {vr}",
                "^abstract:": f"abstract: {desc}",
            },
        )

    def fix_codemeta(self) -> Sequence[str]:
        path = self.context.path / "codemeta.json"
        if not self.has("codemeta") and path.exists():
            return []
        vr = self.context.version
        desc = self.context.description
        return self._replace_substrs(
            path,
            {
                '    "version" *: *"': f'"version":"{vr}"',
                '    "description" *: *"': f'"description":"{desc}"',
            },
        )

    def fix_recipe(self) -> Sequence[str]:
        if self.has("recipe") and self.context.path_source("recipe"):
            return self.fix_recipe_internal(self.context.path_source("recipe"))
        return []

    def fix_env(self) -> Sequence[str]:
        if self.has("environment") and self.context.path_source("environment").exists():
            creator = CondaEnv(self.context.project, dev=True, extras=True)
            return creator.create(self.context, self.context.path)
        return []

    def fix_recipe_internal(self, recipe_path: Path) -> Sequence[str]:
        # TODO this is all quite bad
        # Well, I guess this is still an alpha release
        python_vr = self.context.deps["python"]
        pat = re.compile(r"github:([a-z\d](?:[a-z\d]|-(?=[a-z\d])){0,38})")
        summary = self._careful_wrap(self.context.poetry("description"))
        if "long_description" in self.context.sources:
            long_desc = self._careful_wrap(self.context.source("long_description"))
        else:
            long_desc = summary
        poetry_vr = self.context.build_sys_reqs["poetry"]
        maintainers = self.context.source("maintainers")
        maintainers = [m.group(1) for m in pat.finditer(maintainers)]
        maintainers = "\n    - ".join(maintainers)
        # the pip >= 20 gets changed for BOTH test and host; this is OK
        # The same is true for the poetry >=1.1,<2.0 line: it's added to both sections
        vr_strp = poetry_vr.replace(" ", "")
        lines = self._replace_substrs(
            recipe_path,
            {
                "{% set version = ": '{% set version = "' + str(self.context.version) + '" %}',
                "    - python >=": f"    - python {vr_strp}",
                re.compile("^ {4}- pip *$"): f"    - pip >=20\n    - poetry {vr_strp}",
            },
        )
        new_lines = self._until_line(lines, "about:")
        last_section = f"""
about:
  home: {self.context.poetry("homepage")}
  summary: |
    {summary}
  license_family: {self.context.license.family}
  license: {self.context.license.spdx}
  license_file: LICENSE.txt
  description: |
    {long_desc}
  doc_url: {self.context.poetry("documentation")}
  dev_url: {self.context.poetry("repository")}

extra:
  recipe-maintainers:
    - {maintainers}
"""
        final_lines = [*new_lines, *last_section.splitlines()]
        final_lines = [x.rstrip(" ") for x in final_lines]
        final_str = "\n".join(final_lines)
        final_str = re.compile(r"\n\s*\n").sub("\n\n", final_str)
        if not self.context.dry_run:
            recipe_path.write_text(final_str, encoding="utf8")
        logger.debug(f"Wrote to {recipe_path}")
        return final_str.split("\n")

    def _until_line(self, lines: Sequence[str], stop_at: str):
        new_lines = []
        for line in lines:
            if line.startswith(stop_at):
                break
            new_lines.append(line)
        return new_lines

    def _careful_wrap(self, s: str, indent: int = 4) -> str:
        txt = " ".join(s.split())
        width = self._get_line_length()
        # TODO: I don't know why replace_whitespace=True, drop_whitespace=True isn't sufficient
        return textwrap.fill(
            txt,
            width=width,
            subsequent_indent=" " * indent,
            break_long_words=False,
            break_on_hyphens=False,
            replace_whitespace=True,
            drop_whitespace=True,
        )

    def _replace_substrs(
        self,
        path: Path,
        replace: Mapping[Union[str, re.Pattern], str],
    ) -> Sequence[str]:
        if not self.context.dry_run:
            self.context.back_up(path)
        new_lines = "\n".join(
            [self._fix_line(line, replace) for line in path.read_text(encoding="utf8").splitlines()]
        )
        if not self.context.dry_run:
            path.write_text(new_lines, encoding="utf8")
        logger.debug(f"Wrote to {path}")
        return new_lines.splitlines()

    def _fix_line(self, line: str, replace: Mapping[Union[str, re.Pattern], str]) -> str:
        for k, v in replace.items():
            replace = self._replace(line, k, v)
            if replace is not None:
                return replace
        else:
            return line

    def _replace(self, line: str, k: Union[str, re.Pattern], v: str) -> Optional[str]:
        if isinstance(k, re.Pattern):
            try:
                if k.fullmatch(line) is not None:
                    return k.sub(line, v)
            except re.error:
                logger.error(f"Failed to process '{line}' with pattern '{k}")
                raise
        elif line.startswith(k):
            return v
        return None

    def _get_line_length(self) -> int:
        if "linelength" in self.context.sources:
            return int(self.context.source("linelength"))
        elif "tool.black.line-length" in self.context.data:
            return int(self.context.data["tool.black.line-length"])
        return 100


__all__ = ["Sync"]

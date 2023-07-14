# SPDX-License-Identifier Apache-2.0
# Source: https://github.com/dmyersturnbull/tyranno
"""

"""
import httpx
import orjson
from loguru import logger


class PyPiHelper:
    def new_versions(self, pkg_versions: Mapping[str, str]) -> Mapping[str, tuple[str, str]]:
        logger.warning("Making a best effort to find new versions. Correctness is not guaranteed.")
        updated = {}
        for pkg, version in pkg_versions.items():
            if pkg == "python":
                continue
            logger.debug(f"Searching pypi for package {pkg} (current version: {type(version)})")
            version = self._extract_version(version)
            if version is None:
                logger.error(f"Failed to extract version from {version} for package {pkg}")
                continue
            try:
                new = self.get_version(pkg)
            except ValueError:
                logger.error(f"Did not find package {pkg}", exc_info=True)
            except LookupError:
                logger.error(f"Failed extracting new version for pypi package {pkg}")
                logger.debug(f"Version error for {pkg}", exc_info=True)
            else:
                if new != version:
                    updated[pkg] = version, new
        return updated

    def _extract_version(self, version: str) -> str | None:
        version = str(version)
        matches = re.compile(r"([0-9]+[^ ,]+)").finditer(version)
        matches = list(matches)
        if len(matches) == 0 or len(matches) > 2:
            return None
        # assume the last one will be the max if there are two
        return matches[-1].group(1)

    def _func_pypi_data(self, obj: dict[str, str]) -> dict:
        name, version = obj["name"], obj["version"]
        response = httpx.get(f"https://pypi.org/pypi/${name}/json")
        if 200 <= response.status_code <= 300:
            return orjson.loads(response.text)
        else:
            raise OSError(f"Failed with {response}")

    def get_version(self, name: str) -> str:
        # lowercase 'sphinx' is allowed in pip & poetry, but will not work for the raw URL request
        if name == "sphinx":
            name = "Sphinx"
        pat = re.compile('"package-header__name">[ \n\t]*' + name + " ([0-9a-zA-Z_.-]+)")
        try:
            try:
                r = httpx.get(f"https://pypi.org/project/{name}")
            except OSError:
                logger.debug(f"Failed fetching PyPi vr for package {name}", exc_info=True)
                r = None
            if r is None or r.status_code > 400:
                # thanks to Sphinx and a couple of others
                r = httpx.get(f"https://pypi.org/project/{name.capitalize()}")
                if r.status_code > 400:
                    raise LookupError(f"Status code {r.status_code} from pypi for package {name}")
        except OSError:
            logger.error(
                f"Failed fetching {name} from pypi.org.",
                exc_info=True,
            )
            raise
        matches = {m.group(1).strip() for m in pat.finditer(r.content.decode(encoding="utf8"))}
        if len(matches) != 1:
            raise LookupError(
                f"Failed to extract version from pypi for package {name} (matches: {matches})"
            )
        return next(iter(matches))

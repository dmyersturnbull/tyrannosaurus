# SPDX-License-Identifier Apache-2.0
# Source: https://github.com/dmyersturnbull/tyranno
"""

"""
from datetime import datetime
from typing import Any
from zoneinfo import ZoneInfo

import httpx
import orjson
from jmespath import functions

NOW_LOCAL = datetime.now().astimezone()
NOW_UTC = NOW_LOCAL.astimezone(ZoneInfo("Etc/UTC"))
LOCAL_TIMESTAMP = NOW_LOCAL.isoformat(timespec="microseconds")
UTC_TIMESTAMP = NOW_UTC.isoformat(timespec="microseconds").replace("+00:00", "Z")


class TyrannoFunctions(functions.Functions):
    @functions.signature({"types": ["list"]})
    def _func_semver_max(self, versions: list[str] | str) -> str:
        return max(versions)  # TODO

    @functions.signature({"types": ["list"]})
    def _func_semver_min(self, versions: list[str] | str) -> str:
        return max(versions)  # TODO

    @functions.signature({"types": ["list"]})
    def _func_semver_minor(self, versions: list[str] | str) -> list[str]:
        return list(versions)  # TODO

    @functions.signature({"types": ["list"]})
    def _func_semver_major(self, versions: list[str] | str) -> list[str]:
        return list(versions)  # TODO

    @functions.signature({"types": ["list"]})
    def _func_semver_patch(self, versions: list[str] | str) -> list[str]:
        return list(versions)  # TODO

    @functions.signature({"types": ["string"]})
    def _func_pep508(self, versions: list[str] | str) -> str:
        return str(versions)  # TODO

    @functions.signature({"types": ["string"]})
    def _func_tox_env_list(self, spec: str) -> str:
        return spec  # TODO

    @functions.signature({"types": ["boolean", "array", "object", "null", "string"]})
    def _func_yaml(self, data: Any) -> str:
        return str(data)  # TODO

    @functions.signature({"types": ["string"]})
    def _func_spdx_license(self, short: str) -> dict[str, str]:
        return {"id": short, "name": short}  # TODO

    @functions.signature({"types": ["string"]})
    def _func_spdx_license(self, short: str) -> dict[str, str]:
        return {"id": short, "name": short}  # TODO

    @functions.signature({"types": []})
    def _func_now_local(self) -> str:
        return LOCAL_TIMESTAMP

    @functions.signature({"types": []})
    def _func_now_utc(self) -> str:
        return UTC_TIMESTAMP

    @functions.signature({"types": ["string"]}, {"types": ["string"]})
    def _func_format_datetime(self, dt: str, fmt: str) -> str:
        return datetime.fromisoformat(dt.replace("Z", "+00:00")).strftime(fmt)

    @functions.signature({"types": ["string"]})
    def _func_year(self, dt: str) -> str:
        return datetime.fromisoformat(dt.replace("Z", "+00:00")).strftime("%Y")

    @functions.signature({"types": ["string"]})
    def _func_date(self, dt: str) -> str:
        return datetime.fromisoformat(dt.replace("Z", "+00:00")).strftime("%Y-%m-%d")

    @functions.signature({"types": ["dict"]})
    def _func_pypi_data(self, obj: dict[str, str]) -> dict:
        name, version = obj["name"], obj["version"]
        response = httpx.get(f"https://pypi.org/pypi/${name}/json")
        if 200 <= response.status_code <= 300:
            return orjson.loads(response.text)
        raise OSError(f"Failed with {response}")

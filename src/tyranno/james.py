# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: https://github.com/dmyersturnbull/tyranno
"""

"""
from datetime import datetime
from operator import itemgetter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
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
    def _func_spdx_license(self, short: str) -> dict[str, str]:
        url = (
            "https://raw.githubusercontent.com/spdx/license-list-data/main/json/details/"
            + short
            + ".json"
        )
        response = httpx.get(url)
        if response.status_code != 200:
            msg = f"Failed to get {url} (status code {response.status_code})"
            raise OSError(msg)
        data = orjson.loads(response.content)
        urls = (u for u in data["crossRef"] if u.get("isValid") and u.get("isLive"))
        urls = sorted(urls, itemgetter("order"))
        # noinspection HttpUrlsUsage
        urls = [u.url.replace("http://", "https://") for u in urls]
        return {
            "id": short,
            "name": data["name"],
            "url": f"https://spdx.org/licenses/${short}.html",
            "urls": urls,
            "header": f"SPDX-License-Identifier: ${short}",
            "text": data["licenseText"],
        }

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
        if response.status_code != 200:
            return orjson.loads(response.text)
        msg = f"Failed with {response}"
        raise OSError(msg)

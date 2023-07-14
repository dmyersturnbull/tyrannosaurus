# SPDX-License-Identifier Apache-2.0
# Source: https://github.com/dmyersturnbull/tyranno
"""

"""
from tyranno.model import TYRANNO_CACHE

EXPIRE_SEC = 24 * 60 * 60


class License:
    def __init__(self, name: str):
        self._path = TYRANNO_CACHE / "licenses" / name
        self._url = f"https://raw.githubusercontent.com/spdx/license-list-data/main/json/details/${name}.json"

    @property
    def id(self) -> str:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def text(self) -> str:
        ...

    @property
    def family(self) -> str:
        ...

    @property
    def header(self) -> str:
        ...

    def get_header(self, **kwargs) -> str:
        ...

    @property
    def header_template(self) -> str:
        ...

    @property
    def is_fsf_libre(self) -> bool:
        ...

    @property
    def is_osi_approved(self) -> bool:
        ...

    @property
    def url(self) -> str:
        # TODO: fix http://
        ...

    @property
    def see_also(self) -> list[str]:
        # TODO: fix http://
        ...


class LicenseList:
    def __init__(self):
        self._path = TYRANNO_CACHE / "licenses.json"
        self._url = (
            "https://raw.githubusercontent.com/spdx/license-list-data/main/json/licenses.json"
        )
        # TODO: fix http://

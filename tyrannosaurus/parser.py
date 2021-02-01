from typing import Any, Optional, Sequence, Union

from tyrannosaurus import TyrannoInfo
from tyrannosaurus.enums import DevStatus, License


class LiteralParser:
    def __init__(
        self,
        project: str,
        user: Optional[str],
        authors: Optional[Sequence[str]],
        description: str,
        keywords: Sequence[str],
        version: str,
        status: DevStatus,
        license_name: Union[str, License],
        tyranno_vr: str,
    ):
        self.project = project.lower()
        # TODO doing this in two places
        self.pkg = project.replace("_", "").replace("-", "").replace(".", "").lower()
        self.user = user
        self.authors = authors
        self.description = description
        self.keywords = keywords
        self.version = version
        self.status = status
        self.license = License.of(license_name)
        self.tyranno_vr = tyranno_vr

    def parse(self, s: str) -> str:
        today, now, now_utc = TyrannoInfo.today, TyrannoInfo.now, TyrannoInfo.now_utc
        timestamp, utc_stamp = (
            TyrannoInfo.pretty_timestamp_with_offset,
            TyrannoInfo.pretty_timestamp_utc,
        )
        reps = {
            "today": str(today),
            "today.str": today.strftime("%Y-%m-%d"),
            "today.year": str(today.year),
            "today.month": str(today.month),
            "today.Month": today.strftime("%B"),
            "today.day": str(today.day),
            "now": timestamp,
            "now.utc": utc_stamp,
            "now.iso": now.replace(microsecond=0).isoformat(),
            "now.utciso": now_utc.replace(microsecond=0).isoformat(),
            "now.hour": str(now.hour),
            "now.minute": str(now.minute),
            "now.second": str(now.second),
            "project": self.project.lower(),
            "Project": self.project.capitalize(),
            "PROJECT": self.project.upper(),
            "pkg": self.pkg,
            "Pkg": self.pkg.title(),
            "user": "<<TODO:user>>" if self.user is None else self.user,
            "authors": self._pretty(self.authors),
            "authors.list": self._list(self.authors),
            "version": self.version,
            "status.Name": self.status.name.capitalize(),
            "status.name": self.status.name,
            "status.pypi": self.status.pypi,
            "status.dunder": self.status.dunder,
            "status.Description": self.status.description.capitalize(),
            "status.Description.": self._sentence(self.status.description),
            "status.description": self.status.description,
            "Description": self.description.capitalize(),
            "description": self.description,
            "Description.": self._sentence(self.description),
            "keywords": self._pretty(self.keywords),
            "keywords.list": self._list(self.keywords),
            "license": self.license.name,
            "license.name": self.license.full_name,
            "license.spdx": self.license.spdx,
            "license.official": self.license.spdx,
            "license.family": self.license.family,
            "license.header": self.download_license_template(header=True),
            "license.full": self.download_license_template(header=False),
            "license.url": self.license.url,
            "tyranno.version": self.tyranno_vr,
        }
        for k, v in reps.items():
            s = s.replace("$${" + k + "}", v)
        return s

    def download_license_template(self, header: bool) -> str:
        text = self.license.download_header() if header else self.license.download_license()
        return (
            text.replace("{{ organization }}", ", ".join(self.authors))
            .replace("{{ year }}", str(TyrannoInfo.today.year))
            .replace("{{ project }}", self.project)
        )

    def _sentence(self, v: str) -> str:
        return v.capitalize().strip(".") + "."

    def _pretty(self, v: Optional[Sequence[Any]]) -> str:
        if v is None:
            v = []
        return ", ".join(['"' + str(k) + '"' for k in v])

    def _list(self, v: Optional[Sequence[Any]]) -> str:
        if v is None:
            v = []
        return "[" + ", ".join(['"' + str(k) + '"' for k in v]) + "]"


__all__ = ["LiteralParser"]

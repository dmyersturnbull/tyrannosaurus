from typing import Optional, Sequence, Union

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
        today, now, timestamp = TyrannoInfo.today, TyrannoInfo.now, TyrannoInfo.timestamp
        s = (
            s.replace("${today}", str(today))
            .replace("${today.str}", today.strftime("%Y-%m-%d"))
            .replace("${today.year}", str(today.year))
            .replace("${today.month}", str(today.month))
            .replace("${today.Month}", today.strftime("%B"))
            .replace("${today.day}", str(today.day))
            .replace("${now}", timestamp)
            .replace("${now.hour}", str(now.hour))
            .replace("${now.minute}", str(now.minute))
            .replace("${now.second}", str(now.second))
            .replace("${project}", self.project.lower())
            .replace("${Project}", self.project.capitalize())
            .replace("${PROJECT}", self.project.upper())
            .replace("${pkg}", self.pkg)
            .replace("${license}", self.license.name)
            .replace("${license.name}", self.license.full_name)
            .replace("${license.spdx}", self.license.spdx)
            .replace("${license.official}", self.license.spdx)
            .replace("${license.header}", self.download_license_template(header=True))
            .replace("${LICENSE.HEADER}", self.download_license_template(header=True))
            .replace("${license.full}", self.download_license_template(header=False))
            .replace("${LICENSE.FULL}", self.download_license_template(header=False))
            .replace("${license.url}", self.license.url)
            .replace("${version}", self.version)
            .replace("${status.Name}", self.status.name.capitalize())
            .replace("${status.name}", self.status.name)
            .replace("${status.pypi}", self.status.pypi)
            .replace("${status.dunder}", self.status.dunder)
            .replace("${status.Description}", self.status.description.capitalize())
            .replace(
                "${status.Description.}", self.status.description.capitalize().strip(".") + "."
            )
            .replace("${status.description}", self.status.description)
            .replace("${Description}", self.description.capitalize())
            .replace("${description}", self.description)
            .replace("${keywords}", str(self.keywords))
            .replace("${keywords.yaml0}", "\n- ".join(self.keywords) + "\n")
            .replace("${keywords.yaml2}", "\n  - ".join(self.keywords) + "\n")
            .replace("${keywords.yaml4}", "\n    - ".join(self.keywords) + "\n")
            .replace("${KEYWORDS}", str([k.upper() for k in self.keywords]))
            .replace("${tyranno.version}", self.tyranno_vr)
        )
        if self.user is not None:
            s = s.replace("${user}", self.user)
        if self.authors is not None:
            s = s.replace("${authors}", str(self.authors))
            s = s.replace("${authors.str}", ", ".join(self.authors))
        return s

    def download_license_template(self, header: bool) -> str:
        text = self.license.download_header() if header else self.license.download_license()
        return (
            text.replace("{{ organization }}", ", ".join(self.authors))
            .replace("{{ year }}", str(TyrannoInfo.today.year))
            .replace("{{ project }}", self.project)
        )


__all__ = ["LiteralParser"]

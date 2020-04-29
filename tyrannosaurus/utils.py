from dataclasses import dataclass
from pathlib import Path, PurePath
from typing import Generator, Iterable, Optional, Sequence
from typing import Tuple as Tup
from typing import Union


@dataclass
class ConsoleScript:
    cmd: str
    module: str
    function: str


class Utils:

    min_supportable_python = 3.6

    statuses = {
        v.lower(): "{} - {}".format(i + 1, v)
        for i, v in enumerate(
            ["Planning", "Pre-Alpha", "Alpha", "Beta", "Production/Stable", "Mature", "Inactive"]
        )
    }

    known_formats = {
        ".md": "text/markdown",
        ".rst": "text/x-rst",
        ".txt": "text/plain",
        "": "text/plain",
    }

    @classmethod
    def version_range(cls, minimum: float, maximum: float) -> Sequence[float]:
        if not 3.0 <= cls.min_supportable_python < 3.0 <= 4.0:
            raise ValueError("This function only handles Python 3!")
        if maximum < minimum:
            raise ValueError("Version {}–{} range is reversed".format(minimum, maximum))
        if minimum < cls.min_supportable_python or maximum < cls.min_supportable_python:
            raise ValueError("This doesn't support Python < 3.6. You need to modify this source.")
        return [v / 10 for v in range(int(10 * minimum), int(10 * maximum), 1)]

    @classmethod
    def status_full_name(cls, name: str) -> str:
        return cls.statuses[name.lower()]

    @classmethod
    def guess_format(cls, s):
        return cls.known_formats.get(Path(s).suffix)

    @classmethod
    def find_file(cls, stubs: Iterable[Union[str, PurePath]]):
        for stub in stubs:
            for suffix, fmt in cls.known_formats.items():
                p = Path(str(stub) + suffix)
                if p.is_file() and p.exists():
                    return p, fmt
        return None, None

    @classmethod
    def list_doc_files(cls, under: Union[str, PurePath]) -> Generator[Tup[Path, str], None, None]:
        for f in Path(under).iterdir():
            if f.is_file():
                path, fmt = Utils.find_file(f.name)
                if path is not None:
                    yield path, fmt

    @classmethod
    def read_readme(cls, under: Union[str, PurePath]) -> Tup[Optional[str], Optional[str]]:
        path, fmt = Utils.find_file([under / "README"])
        if path is None:
            return None, None
        return path.read_text(encoding="utf8"), fmt

    @classmethod
    def read_changelog(cls, under: Union[str, PurePath]) -> Tup[Optional[str], Optional[str]]:
        path, fmt = Utils.find_file([under / "CHANGES", under / "CHANGELOG", under / "HISTORY"])
        if path is None:
            return None, None
        return path.read_text(encoding="utf8"), fmt

    def __repr__(self):
        return self.__class__.__name__

    def __str__(self):
        return self.__class__.__name__

    def __eq__(self, other):
        return type(self) == type(other)


__all__ = ["Utils", "ConsoleScript"]

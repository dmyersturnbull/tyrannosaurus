import pytest

from tyrannosaurus.context import Context
from tyrannosaurus.update import Update

from . import TestResources


class TestUpdate:
    def test_update(self):
        with TestResources.temp_dir("fake") as path:
            # TODO use a fake pypi getter
            context = Context(path, dry_run=True)
            update = Update(context)
            pkgs, devs = update.update()
            # cheat flake8 here:
            assert [x for x in sorted(pkgs.keys())] == ["requests", "tomlkit", "typer"]
            assert list(devs) == ["pytest"]


if __name__ == "__main__":
    pytest.main()

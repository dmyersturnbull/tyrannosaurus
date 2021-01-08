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
            assert len(pkgs) == 5
            assert "grayskull" in pkgs
            assert len(devs) >= 6
            assert "pytest" in devs
            # assert "sphinx" in devs or "Sphinx" in devs


if __name__ == "__main__":
    pytest.main()

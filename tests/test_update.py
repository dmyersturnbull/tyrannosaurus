from pathlib import Path

import pytest

from tyrannosaurus.context import Context
from tyrannosaurus.update import Update


class TestUpdate:
    def test_update(self):
        # TODO use a fake pypi getter
        path = (Path(__file__).parent / "resources" / "fake").resolve()
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

from pathlib import Path
import tempfile
from datetime import datetime

import pytest

# noinspection PyProtectedMember
from tyrannosaurus.context import _Context
from tyrannosaurus.new import New


class TestNew:
    def test_new(self):
        project = "tempted2temp"
        path = (
            Path(tempfile.gettempdir())
            / "tyrannosaurus-test"
            / datetime.now().strftime("%Y-%m-%d.%H%M%S")
            / project
        )
        New(
            project,
            "apache2",
            "user",
            ["Author 1"],
            "A description",
            ["some", "keywords"],
            "0.1.0",
            newest=True,
        ).create(path)
        assert (path / "pyproject.toml").exists()
        context = _Context(path, dry_run=True)
        assert context.project == project


if __name__ == "__main__":
    pytest.main()

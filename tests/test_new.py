from pathlib import Path
import shutil

import pytest

# noinspection PyProtectedMember
from tyrannosaurus.context import _Context
from tyrannosaurus.new import New


class TestNew:
    def test_new(self):
        path = Path("resources", "tmp", "tmptyr")
        New("tmptyr", "apache2", "user", "Author 1").create(path)
        assert (path / "pyproject.toml").exists()
        context = _Context(path, dry_run=True)
        assert context.project == "tmptyr"
        shutil.rmtree(str(path))


if __name__ == "__main__":
    pytest.main()

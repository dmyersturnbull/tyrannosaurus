from pathlib import Path
import shutil

import pytest

# noinspection PyProtectedMember
from tyrannosaurus import __date__, __version__

# noinspection PyProtectedMember
from tyrannosaurus.context import _Context

# noinspection PyProtectedMember
from tyrannosaurus.cli import _clean, _new, _recipe, _reqs, _sync


class TestCli:
    def test_new(self):
        _new("tmptyr", "apache2", "user", ["Author 1"])
        assert Path("tmptyr", "pyproject.toml").exists()
        context = _Context("tmptyr", dry_run=True)
        assert context.project == "tmptyr"
        shutil.rmtree("tmptyr")

    def test_reqs(self):
        reqs = _reqs()
        assert len(reqs) > 0
        assert reqs[0] == "Tyrannosaurus version {} ({})".format(__version__, __date__)
        assert ".++++++++++++." in [r.strip() for r in reqs]
        assert "```" not in [r.strip() for r in reqs]

    def test_clean(self):
        root = Path(__file__).parent.parent
        trashed = _clean(root, False, False, True)
        st = {k.name for k, v in trashed}
        # TODO this requires them to exist
        assert "eggs" in st
        assert "tyrannosaurus.egg-info" in st
        assert "tyrannosaurus" not in st
        assert "docs" not in st
        assert "recipes" not in st
        assert ".tox" not in st
        assert [v is not None for k, v in trashed]

    def test_clean_aggressive(self):
        root = Path(__file__).parent.parent
        trashed = _clean(root, True, False, True)
        st = {k.name for k, v in trashed}
        assert ".tox" in st


if __name__ == "__main__":
    pytest.main()

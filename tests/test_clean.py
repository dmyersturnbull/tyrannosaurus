from pathlib import Path

import pytest

from tyrannosaurus.clean import Clean

from tests import TestResources


class TestClean:
    def test_clean(self):
        root = TestResources.resource("fake")
        self._make_list("__pycache__", "eggs", "cython_debug", root=root)
        cleaner = Clean(dists=False, aggressive=False, hard_delete=False, dry_run=True)
        trashed = cleaner.clean(root)
        st = {k.name for k, v in trashed}
        assert "__pycache__" in st
        assert "eggs" in st
        assert "cython_debug" in st
        assert "tyrannosaurus" not in st
        assert "docs" not in st
        assert "recipes" not in st
        assert ".tox" not in st

    def test_clean_aggressive(self):
        root = TestResources.resource("fake")
        self._make_list("eggs", ".ipynb_checkpoints", ".tox", ".tyrannosaurus", root=root)
        cleaner = Clean(dists=False, aggressive=True, hard_delete=False, dry_run=True)
        trashed = cleaner.clean(root)
        st = {k.name for k, v in trashed}
        assert "eggs" in st
        assert ".ipynb_checkpoints" in st
        assert ".tox" in st

    def _make_list(self, *paths: str, root: Path):
        made = []
        for p in paths:
            if not (root / p).exists():
                (root / p).mkdir()
            made.append(root / p)
        return made


if __name__ == "__main__":
    pytest.main()

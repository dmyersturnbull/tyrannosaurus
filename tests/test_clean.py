from pathlib import Path

import pytest

from tyrannosaurus.clean import Clean


class TestClean:
    def test_clean(self):
        root = Path(__file__).parent / "resources" / "fake"
        made = []
        try:
            if not (root / "__pycache__").exists():
                (root / "__pycache__").mkdir()
                made.append(root / "__pycache__")
            if not (root / "eggs").exists():
                (root / "eggs").mkdir()
                made.append(root / "eggs")
            if not (root / "cython_debug").exists():
                (root / "cython_debug").mkdir()
                made.append(root / "cython_debug")
            trashed = Clean(dists=False, aggressive=False, hard_delete=False, dry_run=True).clean(
                root
            )
            st = {k.name for k, v in trashed}
            assert "__pycache__" in st
            assert "eggs" in st
            assert "cython_debug" in st
            assert "tyrannosaurus" not in st
            assert "docs" not in st
            assert "recipes" not in st
            assert ".tox" not in st
        finally:
            for p in made:
                try:
                    p.rmdir()
                except OSError:
                    pass

    def test_clean_aggressive(self):
        root = Path(__file__).parent / "resources" / "fake"
        made = []
        try:
            if not (root / "eggs").exists():
                (root / "eggs").mkdir()
                made.append(root / "eggs")
            if not (root / ".ipynb_checkpoints").exists():
                (root / ".ipynb_checkpoints").mkdir()
                made.append(root / ".ipynb_checkpoints")
            if not (root / ".tox").exists():
                (root / ".tox").mkdir()
                made.append(root / ".tox")
            trashed = Clean(dists=False, aggressive=True, hard_delete=False, dry_run=True).clean(
                root
            )
            st = {k.name for k, v in trashed}
            assert "eggs" in st
            assert ".ipynb_checkpoints" in st
            assert ".tox" in st
        finally:
            for p in made:
                try:
                    p.rmdir()
                except OSError:
                    pass


if __name__ == "__main__":
    pytest.main()

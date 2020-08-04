from pathlib import Path

import pytest

from tyrannosaurus.clean import Clean


class TestClean:
    def test_clean(self):
        root = Path(__file__).parent / "resources" / "fake"
        trashed = Clean(False, False, False, False).clean(root)
        st = {k.name for k, v in trashed}
        # TODO this requires them to exist
        assert "tyrannosaurus" not in st
        assert "docs" not in st
        assert "recipes" not in st
        assert ".tox" not in st

    """
    # TODO we can't run this without creating a fake context
    def test_clean_aggressive(self):
        root = Path(__file__).parent.parent
        trashed = Clean(True, True, False, False).clean(root)
        st = {k.name for k, v in trashed}
    """


if __name__ == "__main__":
    pytest.main()

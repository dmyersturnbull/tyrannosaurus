from datetime import date
from pathlib import Path

import pytest

# noinspection PyProtectedMember
from tyrannosaurus.context import _Context
from tyrannosaurus.sync import Sync


class TestSync:
    def test_fix_init(self):
        path = (Path(__file__).parent / "resources" / "fake").resolve()
        context = _Context(path, dry_run=True)
        sync = Sync(context)
        lines = sync.fix_init()
        assert len(lines) == 3
        assert lines[0] == f'__copyright__ = "Copyright {date.today().year}"'
        assert lines[1] == f'__date__ = "{date.today()}"'
        assert lines[2] == f'__status__ = "Development"'


if __name__ == "__main__":
    pytest.main()

import shutil
import tempfile
from datetime import datetime
from pathlib import Path

import pytest

# noinspection PyProtectedMember
from tyrannosaurus.context import Context
from tyrannosaurus.new import New


class TestNew:
    def test_new_latest(self):
        self._test_it(tyranno_vr="latest")

    def test_new_version(self):
        self._test_it(tyranno_vr="0.8.1")

    def test_new_latest_track(self):
        self._test_it(should_track=True)

    def _test_it(self, should_track=False, tyranno_vr="latest"):
        path = None
        try:
            project = "tempted2temp"
            path = (
                Path(tempfile.gettempdir())
                / "tyrannosaurus-test"
                / datetime.now().strftime("%Y-%m-%d.%H%M%S")
                / project
            )
            New(
                name=project,
                license_name="apache2",
                username="user",
                authors=["Author 1"],
                description="A description",
                keywords=["some", "keywords"],
                version="0.1.0",
                should_track=should_track,
                tyranno_vr=tyranno_vr,
            ).create(path)
            assert (path / "pyproject.toml").exists()
            context = Context(path, dry_run=True)
            assert context.project == project
        finally:
            if path is not None and path.exists():
                try:
                    shutil.rmtree(str(path))
                except OSError:
                    pass  # TODO warning?


if __name__ == "__main__":
    pytest.main()

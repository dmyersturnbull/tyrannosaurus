import pytest

# noinspection PyProtectedMember
from tyrannosaurus.context import DevStatus, Context
from tyrannosaurus.new import New

from tests import TestResources


class TestNew:
    def test_new_latest(self):
        self._test_it(tyranno_vr="latest")

    def test_new_version(self):
        self._test_it(tyranno_vr="0.8.4")

    def test_new_latest_track(self):
        self._test_it(should_track=True)

    def _test_it(self, should_track=False, tyranno_vr="latest"):
        project = "tempted2temp"
        with TestResources.temp_dir() as parent:
            path = parent / project
            New(
                name=project,
                license_name="apache2",
                username="user",
                authors=["Author 1"],
                description="A description",
                keywords=["some", "keywords"],
                version="0.1.0",
                status=DevStatus.alpha,
                should_track=should_track,
                tyranno_vr=tyranno_vr,
            ).create(path)
            assert (path / "pyproject.toml").exists()
            context = Context(path, dry_run=True)
            assert context.project == project


if __name__ == "__main__":
    pytest.main()

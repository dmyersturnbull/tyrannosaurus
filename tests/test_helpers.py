from pathlib import Path

import pytest

# noinspection PyProtectedMember
from tyrannosaurus.helpers import CondaForgeHelper, PyPiHelper, _Env, TrashList


class TestHelpers:
    def test_trash(self):
        assert TrashList(False, False).should_delete(Path("eggs"))
        assert TrashList(False, False).should_delete(Path("OMG.egg-info"))
        assert not TrashList(False, False).should_delete(Path("dists"))
        assert TrashList(True, False).should_delete(Path("dists"))
        assert not TrashList(False, True).should_delete(Path("dists"))
        assert TrashList(False, True).should_delete(Path(".tox"))
        assert not TrashList(True, False).should_delete(Path(".tox"))

    def test_env(self):
        _Env(None, None)
        # env = _Env(None, None)
        # TODO run in test mode
        # assert '<<' not in env.user
        # assert len(env.authors) == 1 and '<<' not in env.authors[0]

    def test_forge(self):
        helper = CondaForgeHelper()
        assert helper.has_pkg("rdkit")
        assert not helper.has_pkg("4we6y4w5ydzfhsfgjkyu")

    def test_pypi(self):
        helper = PyPiHelper()
        np_version = helper.get_version("grayskull")
        assert np_version is not None


if __name__ == "__main__":
    pytest.main()

import pytest

# noinspection PyProtectedMember
from tyrannosaurus.helpers import _CondaForgeHelper, _Env, _PyPiHelper


class TestHelpers:
    def test_env(self):
        _Env(None, None)
        # env = _Env(None, None)
        # TODO run in test mode
        # assert '<<' not in env.user
        # assert len(env.authors) == 1 and '<<' not in env.authors[0]

    def test_forge(self):
        helper = _CondaForgeHelper()
        assert helper.has_pkg("rdkit")
        assert not helper.has_pkg("4we6y4w5ydzfhsfgjkyu")

    def test_pypi(self):
        helper = _PyPiHelper()
        np_version = helper.get_version("grayskull")
        assert np_version is not None


if __name__ == "__main__":
    pytest.main()

import pytest

# noinspection PyProtectedMember
from tyrannosaurus.helpers import _Env


class TestHelpers:
    def test_env(self):
        env = _Env(None, None)
        # TODO run in test mode
        # assert '<<' not in env.user
        # assert len(env.authors) == 1 and '<<' not in env.authors[0]

    """
    def test_pypi(self):
        helper = _PyPiHelper()
        np_version = helper.get_version("peewee")
        assert np_version == "1.18"
    """


if __name__ == "__main__":
    pytest.main()

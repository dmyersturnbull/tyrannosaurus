import pytest

# noinspection PyProtectedMember
from tyrannosaurus.helpers import _Env, _PyPiHelper


class TestHelpers:
    def test_env(self):
        env = _Env(None, None)
        # assert env.user is not None
        # assert env.authors is not None

    """
    def test_pypi(self):
        helper = _PyPiHelper()
        np_version = helper.get_version("peewee")
        assert np_version == "1.18"
    """


if __name__ == "__main__":
    pytest.main()

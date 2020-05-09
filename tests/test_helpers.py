import pytest

# noinspection PyProtectedMember
from tyrannosaurus.helpers import _Env


class TestHelpers:
    def test_env(self):
        env = _Env()
        # assert env.user is not None
        # assert env.authors is not None


if __name__ == "__main__":
    pytest.main()

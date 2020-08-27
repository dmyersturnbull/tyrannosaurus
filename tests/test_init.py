import pytest


class TestInit:
    def test_env(self):
        from tyrannosaurus import __version__, metadata

        assert metadata is not None
        assert __version__ is not None


if __name__ == "__main__":
    pytest.main()

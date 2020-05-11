from pathlib import Path

import pytest

# noinspection PyProtectedMember
from tyrannosaurus.context import _Context
from tyrannosaurus.conda import CondaEnv


class TestConda:
    def test_env(self):
        path = Path(__file__).parent / "resources" / "fake"
        output_path = Path(__file__).parent / "resources" / "tmp" / "fakeenv.yml"
        context = _Context(path, dry_run=True)
        CondaEnv("fakeenv", False, False, False).create(context, output_path)
        assert output_path.exists()
        text = output_path.read_text(encoding="utf8")
        assert "name: fakeenv" in text
        assert "grayskull" in text
        assert "pip:" not in text
        assert "sphinx" not in text


if __name__ == "__main__":
    pytest.main()

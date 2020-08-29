import tempfile
from datetime import datetime
from pathlib import Path

import pytest

from tyrannosaurus.conda import CondaEnv, Recipe

# noinspection PyProtectedMember
from tyrannosaurus.context import Context


class TestConda:
    def test_env(self):
        path = Path(__file__).parent / "resources" / "fake"
        output_env_path = path / "fakeenv.yml"
        context = Context(path, dry_run=True)
        env = CondaEnv("fakeenv", False, False)
        txt = "\n".join(env.create(context, output_env_path))
        assert "name: fakeenv" in txt
        assert "grayskull" in txt
        assert "pip:" not in txt
        assert "sphinx" not in txt

    def test_recipe(self):
        output_path = Path(tempfile.gettempdir()) / (
            "trash-tmpdir-" + datetime.now().strftime("%Y-%m-%d.%H%M%S")
        )
        path = Path(__file__).parent / "resources" / "fake"
        context = Context(path, dry_run=True)
        lines = Recipe(context).create(output_path)
        assert len(lines) > 20
        assert "    - fakeorg" in lines


if __name__ == "__main__":
    pytest.main()

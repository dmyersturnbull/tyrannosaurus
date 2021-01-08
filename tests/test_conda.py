import pytest

from tyrannosaurus.conda import CondaEnv, Recipe

# noinspection PyProtectedMember
from tyrannosaurus.context import Context
from tests import TestResources


class TestConda:
    def test_env(self):
        with TestResources.temp_dir(copy_resource="fake") as path:
            context = Context(path, dry_run=True)
            output_env_path = path / "fakeenv.yml"
            env = CondaEnv("fakeenv", False, False)
            txt = "\n".join(env.create(context, output_env_path))
            assert "name: fakeenv" in txt
            assert "grayskull" in txt
            assert "pip:" not in txt
            assert "sphinx" not in txt

    def test_recipe(self):
        with TestResources.temp_dir(copy_resource="fake") as path:
            # FYI dry run is impossible because of grayskull
            context = Context(path, dry_run=True)
            lines = Recipe(context).create(path / "recipes")
            assert len(lines) > 20
            assert "    - fakeorg" in lines


if __name__ == "__main__":
    pytest.main()

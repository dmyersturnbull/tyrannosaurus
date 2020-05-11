from pathlib import Path

import pytest

# noinspection PyProtectedMember
from tyrannosaurus.context import _Context, _Source, _TomlBuilder, timestamp


class TestContext:
    def test_toml(self):
        toml = (
            _TomlBuilder()
            .add("simple", "is simple")
            .add("tool.poetry.name", "project")
            .add("tool.poetry.version", "version 1")
            .build()
        )
        assert "simple" in toml.x
        assert toml["simple"] == "is simple"
        assert "tool" in toml
        assert "poetry" in toml["tool"]
        assert "version" in toml["tool"]["poetry"]
        assert toml["tool.poetry.name"] == "project"
        assert toml["tool.poetry.version"] == "version 1"

    def test_source(self):
        toml = (
            _TomlBuilder()
            .add("simple", "is simple")
            .add("tool.poetry.name", "project")
            .add("tool.poetry.version", "version 1")
            .build()
        )
        source = _Source().parse("'a value'", toml)
        assert source == "a value"
        source = _Source().parse("tool.poetry.name", toml)
        assert source == "project"

    def test_context(self):
        root = Path(__file__).parent.parent
        context = _Context(root)
        assert context.path == root
        assert context.has_opt("align")
        assert context.has_target("init")
        assert context.source("linelength") == "100"
        assert str(context.get_bak_path("pyproject.toml")) == str(
            Path(root / ".tyrannosaurus" / "pyproject.toml.{}.bak".format(timestamp))
        )


if __name__ == "__main__":
    pytest.main()

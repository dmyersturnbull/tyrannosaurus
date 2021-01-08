from pathlib import Path

import pytest

# noinspection PyProtectedMember
from tyrannosaurus.context import Context, Source, TomlBuilder, timestamp


class TestContext:
    def test_toml(self):
        toml = (
            TomlBuilder()
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
            TomlBuilder()
            .add("simple", "is simple")
            .add("tool.poetry.name", "project")
            .add("tool.poetry.version", "version 1")
            .add("tool.poetry.authors", ["auth", "ors"])
            .add("tool.poetry.description", "A description")
            .add("tool.poetry.license", "A license")
            .add("tool.poetry.keywords", ["key", "words"])
            .build()
        )
        source = Source().parse("'a value'", toml)
        assert source == "a value"
        source = Source().parse("tool.poetry.name", toml)
        assert source == "project"

    def test_context(self):
        # TODO: This weird test operates on tyrannosaurus itself
        root = Path(__file__).parent.parent.resolve()
        context = Context(root)
        assert context.path == root
        assert context.has_opt("align")
        assert context.has_target("init")
        assert context.source("linelength") == "100"
        assert str(context.get_bak_path("pyproject.toml")) == str(
            Path(root / ".tyrannosaurus" / f"pyproject.toml.{timestamp}.bak")
        )


if __name__ == "__main__":
    pytest.main()

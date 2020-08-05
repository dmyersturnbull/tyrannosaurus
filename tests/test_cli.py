import pytest

from tyrannosaurus.cli import CliCommands


class TestCli:
    def test_build_tox(self):
        cmds = CliCommands.build_internal(dry=True)
        assert cmds == ["tyrannosaurus sync", "poetry lock", "tox", "tyrannosaurus clean"]

    def test_build_bare(self):
        cmds = CliCommands.build_internal(bare=True, dry=True)
        assert len(cmds) == 15
        assert cmds[0] == "tyrannosaurus sync"
        assert cmds[-1] == "pip install ."


if __name__ == "__main__":
    pytest.main()

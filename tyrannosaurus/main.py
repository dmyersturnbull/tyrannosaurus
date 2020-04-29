import logging
import click
from tyrannosaurus.metadata import ProjectInfo
from tyrannosaurus.generator import *
from tyrannosaurus.services import *
logger = logging.getLogger('tyrannosaurus')

class Tyrannosaurus:

    @click.command()
    def reqs(self):
        pass

    @click.command()
    def bump(self):
        pass

    @click.command()
    def find(self):
        pass

    @click.command()
    def clean(self):
        pass

    @click.command()
    def check(self):
        pass

    @click.command()
    def info(self):
        print("{}, version {} (released {})".format(ProjectInfo.name, ProjectInfo.release, ProjectInfo.current_release_date))

if __name__ == '__main__':
    pass

__all__ = ['Tyrannosaurus']

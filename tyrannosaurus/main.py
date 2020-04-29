import logging

import click

logger = logging.getLogger("tyrannosaurus")


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
        pass


if __name__ == "__main__":
    pass

__all__ = ["Tyrannosaurus"]

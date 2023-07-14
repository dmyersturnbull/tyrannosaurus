# SPDX-License-Identifier Apache-2.0
# Source: https://github.com/dmyersturnbull/tyranno
"""
Main magic for Tyranno.
"""

from tyranno.cli import cli


def __main__():
    cli()  # calls sys.exit(code) at end

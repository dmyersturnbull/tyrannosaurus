Metadata synchronization
========================

Tyrannosaurus sync
--------------------

Running Tox calls ``tyrannosaurus sync``.
This command copies some project metadata from pyproject.toml to other files and between sections.
These are the required Python versions, development requirements, and line length.
It will also warn you if other information seems inconsistent, such as
a license file not matching.

You can configure this behavior in pyproject.toml
under ``[tool.tyrannosaurus.sources]`` and ``[tool.tyrannosaurus.targets]``.
``targets`` specifies what files and directories to update.
Filename extensions and some directory names are omitted.
The information to update will be decided from the filenames.
For example, ``init`` will include the copyright statement from ``tool.tyrannosaurus.sources.copyright``.
The sources can be either literal values surrounded in single quotes,
or the names of other settings in pyproject.toml.
You can use ``${today}`` to refer to the current date and ``${datetime}`` for the datetime.
``datetime`` will be in the format ``2020-05-07 20:21``.
You can access individual fields as expected, such as ``${datetime.hour}}`` for ``'20'``.

.. note::

    Tyrannosaurus always generates backups before modifying.
    These are saved in ``.tyrannosaurus`` but are cleared on the next Tox build.


List of sync targets
--------------------

Here are most of the available synchronization targets:

- Copyright, status, and date in ``__init__.py``
- Dev dependencies between ``tool.poetry.dev-dependencies``, ``tool.poetry.extras``, and ``tox.ini``
- An ``all`` optional dependency list with all optional non-dev packages
- Dependencies for building docs in ``docs/conf.py`` and ``docs/requirements.txt``
- Code line length between ``black`` and ``pycodestyle``
- Python version in ``pyproject.toml``, ``tox.ini``, ``.travis.yml``, ``black``, and ``readthedocs.yml``
- Copyright in ``docs/conf.py``
- Poetry version in ``Dockerfile``
- Authors and year listed in the license file
- Metadata in ``CITATION.cff`` and ``codemeta.json``
- Dev versions in ``.pre-commit-config.yaml``
- ``--maintainers`` arg for Grayskull in ``tox.ini``
- ``doc_url``, ``dev_url``, and ``license_file`` in ``meta.yaml``
- Most recent version in ``CHANGELOG.md`` assuming `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_

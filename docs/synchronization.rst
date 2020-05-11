Synchronization
====================================

This page will provide detailed information about synchronization.


List of sync targets
--------------------

Here are most of the available synchronization targets:

- Copyright, status, and date in ``__init__.py``
- Dev dependencies between ``tool.poetry.dev-dependencies``, ``tool.poetry.extras``, and ``tox.ini``
- An ``all`` optional dependency list with all optional non-dev packages
- Dependencies for building docs in ``docs/conf.py`` and ``docs/requirements.txt``
- Code line length between ``isort``, ``black``, and ``pycodestyle``
- Python version in ``pyproject.toml``, ``tox.ini``, ``.travis.yml``, ``black``, and ``readthedocs.yml``
- Copyright in ``docs/conf.py``
- Poetry version in ``Dockerfile``
- Authors and year listed in the license file
- Metadata in ``CITATION.cff`` and ``codemeta.json``
- Dev versions in ``.pre-commit-config.yaml``
- ``--maintainers`` arg for Grayskull in ``tox.ini``
- ``doc_url``, ``dev_url``, and ``license_file`` in ``meta.yaml``
- Most recent version in ``CHANGELOG.md`` assuming `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_

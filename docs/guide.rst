User guide
====================================

Guide for new projects.
This may be especially helpful for users new to Python packaging.


To-do list for new projects
------------------------------

These steps are provided for reference and for new users.
Consider following them after running ``tyrannosaurus new``.

.. tip::

    First, make sure Git is configured correctly.
    Check ``git config user.name`` and ``git config user.name``.
    Make sure it knows about your GPG keys: ``git config --global user.signingkey``

1. Remove unwanted files, such as ``.travis.yml`` if unused.
2. Modify ``.github/labels.json``, ``pyproject.toml``, and ``README.md`` as needed.
3. Create an empty (non-initialized) Github repo and copy the files.
4. Run ``pre-commit install`` and ``poetry install && tyrannosaurus sync && tox``.
5. Update the changelog and commit. (If changes were needed, just run again to accept them.)
6. On `PyPi <https://pypi.org>`_, create a new repo and get a repo-specific token.
7. In your Github secrets page (under Settings), add ``PYPI_TOKEN``.
8. Tell `DockerHub <https://hub.docker.com/>`_ to track your repo.
9. Create a release on Github to publish to PyPi and Dockerhub.
10. Review `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_, `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and `Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_.

You can add ``tyrannosaurus sync`` and ``tyrannosaurus clean`` to tox.ini if desired.
You may also want to add new integrations, like `codeclimate <https://codeclimate.com/>`_ or `codacy <https://www.codacy.com/>`_.
Consider adding `shields <https://shields.io/>`_ for them.


Reference of commands
---------------------

These commands might be useful:

- ``tyrannosaurus sync`` to sync metadata and nothing else
- ``tyrannosaurus clean --aggressive`` to remove lots of temp files
- ``pre-commit install`` to configure pre-commit hooks
- ``tox`` to sync metadata, build, install, build docs, and test
- ``poetry bump`` to bump dependency versions (major or minor)
- ``tyrannosaurus recipe`` to generate a Conda recipe

And these commands are run automatically via either Tox or a Github action:

- ``poetry install`` to install and nothing more
- ``poetry build`` to build wheels and sdists
- ``poetry publish`` to upload to PyPi
- ``docker build .`` to build a docker image

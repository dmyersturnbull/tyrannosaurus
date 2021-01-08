Making a new project
====================================

You can use Tyrannosaurus to create a new project.
Run: ``tyrannosaurus new myproject --track``.

Basic usage of ``tyrannosaurus new``
------------------------------------

Internally, it clones the Tyrannosaurus repo, checks out the correct version, and fills your
new repo with the proper files. The ``--track`` flag causes it to run ``git init`` and track the
``main`` branch of the repo at ``https://github.com/{user}/myproject.git``. The user will be
guessed from your git config, but it can be set with ``--user``. It’s fine to pass the name of a
Github org, too.

But you can pass those in with ``--authors`` (comma-separated), ``--version``, ``--status``,
and ``--keywords``. You can choose a different license using ``--license``. Choices are
Apache 2, CC0, CC-BY, CC-BY-NC, GPL 3, LGPL, and MIT.
See ``tyrannosaurus new --help`` for more info.

.. note::

    Github made *main* the `default branch name <https://github.com/github/renaming>`_ for new repositories in
    October 2020. The provided workflows should work with either *main* or *master*.
    You’ll want ``git push origin main``, not ``git push origin master``, unless you renamed the branch.


Project metadata in pyproject.toml to modify
--------------------------------------------

Modify your project as needed after running ``tyrannosaurus new``.
Most of the metadata you’ll want to modify is contained in ``pyproject.toml``.
There are a bunch of comments with ``TODO:`` in this file.
Chances are, you will only need to modify those. In particular, two sections:

- *Poetry metadata* (``[tool.poetry]`` and ``[tool.poetry.urls]``)
- *Poetry build & dependencies* (``[tool.poetry.dev-dependencies]``, etc.)

.. tip::

    **Support for Python < 3.8:**
    If you need to support Python 3.7 and below, add ``importlib_metadata`` to ``pyproject.toml``
    and ``docs/requirements.txt``. Then change ``importlib.metadata`` in ``__init__.py``
    with ``importlib_metadata``.


Readme file, issue labels, etc.
-------------------------------

You may want to modify the ``.github/labels.json`` file;
when you commit, your Github labels will be replaced with these.
Chances that you want to modify the readme are also quite high :)

.. caution::

    Will replace your Github labels each time you commit.
    Either edit the ``.github/labels.json`` file or disable by deleting
    ``.github/workflows/labels.yml``.


Manual steps to configure reports
---------------------------------

You will need to set a few Github tokens and set up a few external services manually.

Coverage reports will be sent to `Coveralls <https://coveralls.io/>`_ and/or `CodeCov <codecov.io>`_.
Code quality analysis will also be performed using CodeClimate and Github’s CodeQL.
The default readme file shows shields for Coveralls, CodeCov, and Code Climate;
these always reflect what’s in your main branch.
All four of these are free for open source projects.
You probably only want *either* Coveralls or CodeCov because they do the same thing,
whereas Code Climate provides maintainability summaries, and CodeQL provides
security checks.

These analyses are run whenever you push to the main branch, handled by the workflow file
``.github/workflows/commit.yml``. Code Climate tracks your main branch on its own through
a Github push webhook.

Coveralls and CodeCov will only work if you add their tokens to your Github repo secrets.
If these tokens aren’t found or are invalid, the workflow commands will silently fail.
(This is so that you don’t have to use both, or even either.)
All of these will also need webhooks added, though they currently can do that automatically
after you authorize them on Github.

Here’s what you need to do to set these up:

- Connect CodeClimate and either Coveralls or CodeCov and to your Github account and follow their
  configuration instructions.
- Add either ``COVERALLS_REPO_TOKEN`` or ``CODECOV_TOKEN`` to your Github repo secrets.
- Code Climate assigns a url for your repo. Currently, can see it in Settings→Badges.
  For example, the badge link for Tyrannosaurus is
  ``https://api.codeclimate.com/v1/badges/5e3b38c9b9c418461dc3/maintainability``.
  Copy that URL to ``README.md``.


Manual steps to configure PyPI publishing
-----------------------------------------

To get the Github publish action working, you need to:

1. Make an account on `PyPi <https://pypi.org>`_ if you don’t have one.
2. Make a new single-repo token on PyPi.
3. In your Github secrets page, add ``PYPI_TOKEN``.
4. If you don’t want to use Github packages, remove that section of ``.github/workflows/publish.yml``.


Manual steps to configure DockerHub
-----------------------------------------

You want to tell `Dockerhub <https://hub.docker.com/>`_ to track your project.
First, tell `DockerHub <https://hub.docker.com/>`_ to track your repo with:

- source ``/v[0-9]+.*/``
- tag ``{sourceref}``

On your Github repo ⮞ Settings ⮞ Webhooks ⮞ your docker hook ⮞ Edit, check ``Releases``.
That should be it.

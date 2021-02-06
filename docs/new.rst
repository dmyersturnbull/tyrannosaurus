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
GitHub org, too.

.. tip::

	You need to create the repo on GitHub before running ``new``.
	If you didn’t do this, delete the ``.git`` dir, run ``git init --initial-branch=main``, and run ``git remote add origin https://github.com/{user}/{myproject}.git``.
	(You can also just replace the bad ``.git`` with the correct one from your GitHub repo.)

But you can pass those in with ``--authors`` (comma-separated), ``--version``, ``--status``,
and ``--keywords``. You can choose a different license using ``--license``. Choices are
Apache 2, CC0, CC-BY, CC-BY-NC, GPL 3, LGPL, and MIT.
See ``tyrannosaurus new --help`` for more info.

.. note::

    GitHub made *main* the `default branch name <https://github.com/github/renaming>`_ for new repositories in
    October 2020. The provided workflows should work with either *main* or *master*.
    You’ll want ``git push origin main``, **not** ``git push origin master``, unless you renamed the branch.
    I recommend keeping *main* as the default branch.


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
    to ``importlib_metadata``.


Readme file, issue labels, etc.
-------------------------------

You may want to modify ``.github/settings.json`` (or ``.github/labels.json``);
when you commit, your full settings (or just GitHub labels) will be replaced with these.
Chances are you’ll also want to modify the readme :)

.. caution::

    Will replace your GitHub labels each time you commit.
    Either edit the ``.github/labels.json`` file or disable by deleting
    ``.github/workflows/labels.yml``.


Manual steps to configure reports
---------------------------------

.. hint::

    Also `see the new project guide <https://tyrannosaurus.readthedocs.io/en/stable/guide.html>`_.
    It has a more complete list of steps; this doc contains more discussion and explanation.

You will need to set a few GitHub tokens and set up a few external services manually.

Coverage reports will be sent to `Coveralls <https://coveralls.io/>`_ and/or `CodeCov <codecov.io>`_.
Code quality analysis will also be performed using CodeClimate and GitHub’s CodeQL.
The default readme file shows shields for Coveralls, CodeCov, and Code Climate;
these always reflect what’s in your main branch.
All four of these are free for open source projects.
You probably only want *either* Coveralls or CodeCov because they do the same thing,
whereas Code Climate provides maintainability summaries, and CodeQL provides
security checks.

These analyses are run whenever you push to the main branch, handled by the workflow file
``.github/workflows/commit.yml``. Code Climate tracks your main branch on its own through
a GitHub push webhook.

Coveralls and CodeCov will only work if you add their tokens to your GitHub repo secrets.
If these tokens aren’t found or are invalid, the workflow commands will silently fail.
(This is so that you don’t have to use both, or even either.)
All of these will also need webhooks added, though they currently can do that automatically
after you authorize them on GitHub.

Here’s what you need to do to set these up:

- Connect CodeClimate and either Coveralls or CodeCov and to your GitHub account and follow their
  configuration instructions.
- Add ``CODECOV_TOKEN`` to your GitHub repo secrets, if needed.
- Code Climate assigns a url for your repo. Currently, can see it in Settings→Badges.
  For example, the badge link for Tyrannosaurus is:

  ``https://api.codeclimate.com/v1/badges/5e3b38c9b9c418461dc3/maintainability``.

  Copy that URL to ``README.md``.

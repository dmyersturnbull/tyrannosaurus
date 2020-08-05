Making a new project
====================================

You can use Tyrannosaurus to create a new project.
Run: ``tyrannosaurus new myproject``.
It will clone the most recent version and fill in information.
It will guess the authors and Github username from your git config.
But you can pass those in with ``--authors`` (comma-separated) and ``--user`` (single item).
You can also choose a different license using ``--license``.
Choices are Apache 2, CC0, CC-BY, CC-BY-NC, GPL 3, LGPL, and MIT.
See ``tyrannosaurus new --help`` for more info.

After, modify your project as needed,
especially by setting your metadata and dependencies in ``pyproject.toml``.
You may consider adding ``tyrannosaurus clean``, ``tyrannosaurus sync``,
and/or ``tyrannosaurus env`` to your tox config.
Finally, you may want to modify the ``.github/labels.json`` file.
When you commit, your Github labels will be replaced with these.

.. caution::

    Will replace your Github labels each time you commit.
    Either edit the ``.github/labels.json`` file or disable by deleting
    ``.github/workflows/labels.yml``.


To get the Github publish action working, you need to:

1. Make an account on pypi.org if you don’t have one.
2. Make a new single-repo token on PyPi.
3. In your Github secrets page, add ``PYPI_TOKEN``.

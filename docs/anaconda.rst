Working with Anaconda
======================

Tox uses virtualenv, typically creating a new environment for each build.
Unfortunately, `Tox does not support Anaconda <https://bitbucket.org/hpk42/tox/issues/273/support-conda-envs-when-using-miniconda>`_.
However, you can use tox on top of a Conda installation without issue.
For example, you might have a *build* environment and run tox inside it:

.. code-block::

  conda create \
    --name build \
    --channel conda-forge \
    --override-channels \
    --force \
    --yes \
    tox poetry

In addition, for `several reasons <https://dmyersturnbull.github.io/#-the-python-build-landscape>`_,
I strongly recommend using Poetry to manage dependencies instead of Anaconda.
(Also, I recommend using Miniconda and conda-forge, as I recommended to a user who
`broke their conda base <https://stackoverflow.com/questions/61624631/using-anaconda-is-a-messy-base-root-going-to-be-a-problem-in-the-long-term>`_.)

Unfortunately, you may occasionally have dependencies that are available through Anaconda but not PyPi.
One such offending package is `rdkit <https://www.rdkit.org/>`_, and there has been a lot of
`discussion about this issue <https://github.com/rdkit/rdkit/issues/1812>`_.
Aside from a handful of scientific packages, this is a rare situation.
This is a bad problem to have, but you have at least two options:

- Refactor. Extract the dependency into a new project.
  If necessary, you can have the projects `communicate over a socket <https://github.com/dmyersturnbull/service-it>`_
  and add integration tests in a third project.
- Use `tox-conda <https://github.com/tox-dev/tox-conda>`_. This project appears unmaintained as of August 2020,
  and Conda might clobber your carefully managed Poetry dependencies.


Anaconda environment file
-------------------------

You can generate an environment yml file using: ``tyrannosaurus env``.
It will check for packages on Conda-Forge and move packages not found to the ``pip:`` section.


Anaconda recipes
--------------------

This describes how to generate a Conda recipe and
[upload it to `Conda-Forge <https://conda-forge.org/#add_recipe>`_.
Your desired version must already be published on PyPi.

1. Run ``tyrannosaurus recipe``, which will run grayskull.
2. Check over your new recipe in ``recipes/projectname/meta.yaml``.
3. Fork from  `staged-recipes <https://github.com/conda-forge/staged-recipes>`_.
4. Copy your recipe from ``recipes/projectname/meta.yaml`` into the repo (keeping the path).
5. Make a pull request. If everything goes well, it will be on Conda-Forge soon!

.. tip::

    On Windows, you may need to run ``conda install m2-patch`` first.

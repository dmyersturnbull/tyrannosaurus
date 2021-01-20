Working with Anaconda
======================

Tox uses virtualenv, typically creating a new environment for each build.
Unfortunately, `Tox does not support Anaconda <https://bitbucket.org/hpk42/tox/issues/273/support-conda-envs-when-using-miniconda>`_.
However, you can use tox on top of a Conda installation without issue.
For example, you might have a *build* environment and run tox inside it:

.. code-block::

  conda create \
    --name build \
    --override-channels \
    --channel conda-forge \
    --force \
    --yes \
    python=3.9
    pip install tox poetry


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
Your desired version must already be published on PyPi, which happens shortly after you create a Github release.

Initial recipe generation
+++++++++++++++++++++++++

You will only need to do this once:

1. Run ``tyrannosaurus recipe``, which will run grayskull.
2. Check over your new recipe in ``recipes/projectname/meta.yaml``. The recipe-generation command isn’t perfect, so fix errors if there are any.
3. Fork from `staged-recipes <https://github.com/conda-forge/staged-recipes>`_. Check out that repo in a new branch named the same as your project.
4. Copy your recipe from ``recipes/projectname/meta.yaml`` into that fork (same path), along with your license file.
5. Make a pull request. Tests in Azure will be run, and a maintainer will merge your request.

.. tip::

    On Windows, you may need to run ``conda install m2-patch`` first.

If everything goes well, your package will be on Conda-Forge soon after.

Keeping the package up-to-date
++++++++++++++++++++++++++++++

A new feedstock repo will also be created. For example, see
`Tyrannosaurus’s own feedstock <https://github.com/conda-forge/tyrannosaurus-feedstock>`_.
You should receive an email that adds you to Conda-Forge. Accept it to gain write access to this feedstock.
The same goes for anyone else listed as a maintainer in the recipe under ``recipe-maintainers:``.
A little after each new release on PyPi, you will get a pull request on the feedstock that bumps the version.
Let the Azure tests pass, check over the diff – especially making sure that any changes to the dependencies are
reflected correctly – then merge. That’s it: the conda-forge package should be automatically updated.

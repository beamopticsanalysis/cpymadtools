Contributing
============

Contributions in the form of bug reports, bug fixes, documentation, enhancement proposals and more are welcome.
This page provides information on how best to contribute.

Asking for Help
---------------

If you have a question about how to use the package feel free to raise a `GitHub issue <https://github.com/fsoubelet/cpymadtools/issues/new>`_ with the ``Question`` label.

Bug Reports
-----------

If you find a bug, please raise a `GitHub issue <https://github.com/fsoubelet/cpymadtools/issues/new>`_ with the ``Bug`` label.
Please include the following items in a bug report:

1. A minimal, self-contained snippet of Python code reproducing the problem. You can
   format the code nicely using Markdown, e.g.::


    ```python
    import cpymadtools
    # your example here.
    ```

2. An explanation of why the current behaviour is wrong/not desired, and what you expect instead.

3. Information about the version of the package, along with versions of dependencies and the Python interpreter, and installation information.
   Information about other packages installed can be obtained by executing ``pip freeze`` (if using pip_) or ``conda env export`` (if using conda_) from the terminal.
   A convenience function is provided in the `~cpymadtools._version` module:
   
    .. code-block:: python
   
        >>> import cpymadtools
        >>> print(cpymadtools._version.version_info())
            cpymadtools version: 1.0.0
                   Install path: /Users/felixsoubelet/Repositories/Work/cpymadtools/cpymadtools
                 Python version: 3.10.6
          Python implementation: 3.10.6 | packaged by conda-forge | (main, Aug 22 2022, 20:38:29) [Clang 13.0.1 ]
                       Platform: macOS-12.6-arm64-arm-64bit

Enhancement Proposals
---------------------

If you have an idea about a new feature or some other improvement, please raise a `GitHub issue <https://github.com/fsoubelet/cpymadtools/issues/new>`_ with the ``Feature Request`` label first to discuss.
Ideas and suggestions for how to improve the package are welcome.

Contributing Code and/or Documentation
--------------------------------------

Forking the Repository
~~~~~~~~~~~~~~~~~~~~~~

The cpymadtools source code is hosted on GitHub at the following location:

* `https://github.com/fsoubelet/cpymadtools/ <https://github.com/fsoubelet/cpymadtools/>`_

You will need your own fork to work on the code: go to the link above and hit the **Fork** button.
Then clone your fork to your local machine::

    $ git clone git@github.com:your-user-name/cpymadtools.git
    $ cd cpymadtools
    $ git remote add upstream git@github.com:fsoubelet/cpymadtools.git

Creating a Development Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``cpymadtools`` uses Hatch_ as a package development tool, which handles the creation & management of a development environment, building, publishing, recipes and more.
However, as the **pyproject.toml** file is fully **PEP**-compliant, using ``Hatch`` is **not mandatory** for development.

Here is how to set yourself up:

    .. tabbed:: Using Hatch

        Assuming you have ``hatch`` in your ``PATH``, once in the root of the repository setting yourself up is as easy as::

            $ hatch env create

        With this, ``hatch`` will create a new virtual environment and install in there the package as well as its runtime and development dependencies.
        The installation is similar to the editable mode from ``pip``.
        You can enter the environment by running::

            $ hatch shell

        .. tip::

            Start your commands with **hatch run** to have ``hatch`` run them in the virtual environment, if you don't wish to activate it.
            For instance, getting the Python version can be as simple as::

                $ hatch run python --version

    .. tabbed:: Without Hatch

        If you want to skip using ``Hatch``, you can create a virtual environment yourself and then ``pip install`` the package in editable mode::

            $ python -m pip install -e ".[test,dev,docs]"


Creating a Branch
~~~~~~~~~~~~~~~~~

Before you do any new work or submit a pull request, please open an issue on GitHub to report the bug or propose the feature you'd like to add.

It's best to synchronize your fork with the upstream repository, then create a new, separate branch for each piece of work you want to do.
E.g.::

    $ git checkout master
    $ git fetch upstream
    $ git rebase upstream/master
    $ git checkout -b shiny-new-feature
    $ git push -u origin shiny-new-feature

This changes your working directory to the **shiny-new-feature** branch.
Keep any changes in this branch specific to one bug or feature, so it is clear what the branch brings.

To update this branch with the latest code from ``cpymadtools``, you can retrieve the changes from the master branch and perform a rebase::

    $ git fetch upstream
    $ git rebase upstream/master

This will replay your commits on top of the latest ``cpymadtools`` git master.
If this leads to merge conflicts, these need to be resolved *before* submitting a pull request.
Alternatively, you can merge the changes in from upstream/master instead of rebasing, which can be simpler::

    $ git fetch upstream
    $ git merge upstream/master

Again, any conflicts need to be resolved *before* submitting a pull request.

Running the Test Suite
~~~~~~~~~~~~~~~~~~~~~~

The repository includes a suite of unit tests you should run to check your changes.
One can run the test suite in the following way:

    .. tabbed:: Using Hatch

        The simplest way to run the test suite using ``hatch`` is::

            $ hatch run python -m pytest

    .. tabbed:: Without Hatch

        In your virtual environment, run::

            $ python -m pytest

All tests are automatically run via **GitHub Actions** for every push onto the main repository, and in every pull request.
The test suite **must** pass before code can be accepted.
Test coverage is also collected automatically via the Codecov_ service, and the target for total coverage is usually 95%, though exceptions can be made.

Code Standards
~~~~~~~~~~~~~~

All code must conform to the PEP8_ standard.
Lines up to 120 characters are allowed, although please try to keep below wherever possible.
Formatting is enforced using the ``black`` tool, and imports sorting with ``isort``.

`Type hints <https://www.python.org/dev/peps/pep-0484>`_ are required for all user-facing classes and functions.
As much as possible, types are enforced with the help of the ``mypy`` tool.
Additionally, code quality is kept in check with the ``pylint`` tool.

Documentation
~~~~~~~~~~~~~

Docstrings for user-facing classes and functions should follow the `Google <https://google.github.io/styleguide/pyguide.html#s3.8.1-comments-in-doc-strings>`_
format, including sections for Parameters and Examples.

``cpymadtools`` uses Sphinx_ to build its documentation, which is hosted on GitHub Pages.
Documentation is written in the ``RestructuredText`` markup language (**.rst** files) in the **docs** folder.
The documentation consists both of prose and API reference documentation.
All user-facing classes and functions should be included in the API documentation.

The documentation can be built locally by running::

    $ python -m sphinx -v -b html docs doc_build -d doc_build

The static HTML pages will be available in a newly created **doc_build** folder.


.. _pip: https://pip.pypa.io/en/stable/
.. _conda: https://docs.conda.io/en/latest/
.. _Codecov: https://about.codecov.io/
.. _Hatch: https://hatch.pypa.io/latest/
.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
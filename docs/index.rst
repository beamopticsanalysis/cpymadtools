Welcome to Cpymadtools's Documentation!
=======================================

This package is a lightweigth pythonic wrapper around ``cpymad``, which was extracted from the `~pyhdtoolkit` package.
It enables convenient control of MAD-X_ simulations through the cpymad_ package.

Installation
------------

``cpymadtools`` is available to install from ``PyPI`` or from VCS.
Install the package from ``PyPI``::

    python -m pip install cpymadtools

To install the latest development version of cpymadtools, you can use ``pip`` with the latest GitHub master::

    python -m pip install git+https://github.com/beamopticsanalysis/cpymadtools.git

To set up a development environment, see the :doc:`contributing instructions <contributing>`.

Contents
--------

.. toctree::
    :maxdepth: 2

    quickstart
    api
    contributing
    release
    bibliography

Citing
------

If you have a use of these codes, please consider citing them.
The repository has a DOI_ provided by Zenodo_, and all versions can be cited with the following ``BibTeX`` entry:

.. code-block:: bibtex

   @software{cpymadtools,
     author       = {Felix Soubelet},
     title        = {beamopticsanalysis/cpymadtools},
     publisher    = {Zenodo},
     doi          = {10.5281/zenodo.7339939},
     url          = {https://github.com/beamopticsanalysis/cpymadtools}
   }

Acknowledgments
---------------

This package is exctacted from ``PyhDToolkit``, which was written by :user:`Felix Soubelet <fsoubelet>`.

Others who have helped its development by contributing code, documentation, comments and/or ideas:

* :user:`Joschua Dilly <joschd>`
* :user:`Axel Poyet <apoyet>`
* :user:`Michael Hofer <mihofer>`
* :user:`Tobias Persson <tpersson>`

License
-------

The package is licensed under the `MIT license <https://github.com/beamopticsanalysis/cpymadtools/blob/master/LICENSE>`_. 

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _MAD-X: https://mad.web.cern.ch/mad/
.. _cpymad: https://hibtc.github.io/cpymad/
.. _pydantic: https://pydantic-docs.helpmanual.io/
.. _HTCondor: https://htcondor.org/
.. _DOI: https://zenodo.org/badge/latestdoi/227081702
.. _Zenodo: https://zenodo.org
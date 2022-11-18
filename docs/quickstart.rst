.. _quickstart-top:

Quickstart
==========

.. _quickstart-install:

Installation
------------

This package is tested for and supports `Python 3.8+`.
You can install it simply from ``PyPI`` in a virtual environment with:

.. prompt:: bash

    python -m pip install cpymadtools

.. tip::
    Don't know what a virtual environment is or how to set it up?
    Here is a good primer on `virtual environments <https://realpython.com/python-virtual-environments-a-primer/>`_ by `RealPython`.

To set up a development environment, see the :doc:`contributing instructions <contributing>`.

.. _quickstart-five-minutes:

5 Minutes to Cpymadtools
------------------------

One can use the library by simply importing it:

.. prompt:: python >>>

    import cpymadtools

This will include sub-packages of ``cpymadtools``.
The different sub-packages can be imported separately, depending on your needs:

.. prompt:: python >>>

    import cpymadtools.constants
    import cpymadtools.coupling
    import cpymadtools.lhc
    import cpymadtools.matching
    import cpymadtools.ptc
    import cpymadtools.track
    import cpymadtools.tune
    import cpymadtools.twiss
    import cpymadtools.utils


These sub-packages provide an ensemble of functionality to perform operations with and from `~cpymad.madx.Madx`
objects; and conveniently setup, run and analyze ``MAD-X`` simulations and their results.

All the public apis in `~cpymadtools` work in the same fashion: call them with as first argument your
`~cpymad.madx.Madx` instance, and then any `args` and `kwargs` relevant to the functionality at hand.
Let's say one has initiated their ``MAD-X`` simulation through `~cpymad.madx.Madx` as follows:

.. prompt:: python >>>

    from cpymad.madx import Madx
    madx = Madx()

Then using the `~cpymadtools` apis goes as:

.. prompt:: python >>>

    from cpymadtools.some_module import super_cool_function  # pretend these exist ;)
    super_cool_function(madx, *args, **kwargs)

In the `~pyhdtoolkit.cpymadtools` one will find modules to:

* Encompass existing ``MAD-X`` commands, such as for example :ref:`matching <cpymadtools-matching>` or :ref:`tracking <cpymadtools-track>`;
* Perform useful routines with a pythonic interface (for instance :ref:`betatron coupling  <cpymadtools-coupling>` calculation and handling or :ref:`table querying <cpymadtools-utils>`);
* Run several :ref:`(HL)LHC <cpymadtools-lhc>` specific functionality. 

One can find many examples of the `~cpymadtools` API' use in the gallery_ of the `~pyhdtoolkit` documentation.


.. _gallery: https://fsoubelet.github.io/PyhDToolkit/gallery/index.html
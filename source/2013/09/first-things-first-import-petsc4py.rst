*************************************************
First things first: import ``petsc4py`` correctly
*************************************************

`petsc4py <https://bitbucket.org/petsc/petsc4py>`_ can pass command line arguments to ``PETSc``, such as the very useful ``-log_summary``. This would typically be done by passing these arguments to ``petsc4py.init()``. However, this command must be invoked before any other ``petsc4py`` command. In other words

.. code-block:: python
    
    from petsc4py import PETSc

must be placed *after* this initialization. To sum up, a typical initialization sequence of  ``petsc4py`` should look something like

.. code-block:: python

    import sys
    import petsc4py

    petsc4py.init(sys.argv)

    from petsc4py import PETSc

It took me some time (and Lissandro's help) to figure out that switching the las two lines (although more good looking) was wrong...

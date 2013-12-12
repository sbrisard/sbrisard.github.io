****************************************************
Scientific computing under Windows 7, part 5: LAMMPS
****************************************************

From the `official website <http://lammps.sandia.gov/index.html>`_

    LAMMPS is a classical molecular dynamics code, and an acronym for Large-scale Atomic/Molecular Massively Parallel Simulator.

To install from sources, download the `tarball <http://lammps.sandia.gov/download.html#tar>`_. Extract it in e.g. ``C:\src\lammps-30Sep13`` (your version of LAMMPS might differ). Edit the file ``C:\src\lammps-30Sep13\src\Makefile``, and replace the following line::

    EXE =	$(ROOT)_$@
    
with::

    EXE =	$(ROOT)_$@.exe

Then create an appropriate ``Makefile.mingw32``, starting from ``Makefile.serial``. In the MSYS console::

    $ cd /C/src/lammps-30Sep13/src/MAKE
    $ cp Makefile.serial Makefile.mingw32

If you want to link LAMMPS against FFTW (which you must first install, see a previous post), edit the newly created file and modify the lines relating to FFT::

    FFT_INC = -DFFT_FFTW3 -I/mingw/include
    FFT_PATH = -L/mingw/lib
    FFT_LIB = -lfftw3

(assuming you have installed the static version of the library). Before you compile LAMMPS itself, you need to compile the MPI stubs, which is a dummy (serial) replacement for a true MPI library. This should normally be done by ``make stubs``, but this last command somehow does not work::

    $ cd /C/src/lammps-30Sep13/src
    make: `stubs' is up to date.

The solution is to force compilation of the stubs::

    $ cd /C/src/lammps-30Sep13/src/STUBS
    $ make

which produces a file ``libmpi_stubs.a``. You are now ready to compile::

    $ cd /C/src/lammps-30Sep13/src
    $ make mingw32

which produces an executable ``src/lmp_mingw32.exe``. To test this executable, go to the ``examples`` directory::

    $ cd /C/src/lammps-30Sep13/examples

and run one of the applications, for example::

    $ cd micelle
    $ ../../src/lmp_mingw32.exe < in.micelle

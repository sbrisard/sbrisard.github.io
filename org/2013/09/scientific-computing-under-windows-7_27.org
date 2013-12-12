.. highlight:: none

*************************************************
Scientific computing under Windows 7, part 3: MPI
*************************************************

From the `official website <http://www.mpich.org/>`_

  The goals of MPICH are:
  1. to provide an MPI implementation that efficiently supports different computation and communication platforms including commodity clusters (desktop systems, shared-memory systems, multicore architectures), high-speed networks and proprietary high-end computing systems (Blue Gene, Cray)
  2. to enable cutting-edge research in MPI through an easy-to-extend modular framework for other derived implementations

I didn't manage to compile MPICH with MinGW and had to resort to precompiled binaries, which can be downloaded from the `Microsoft website <http://www.microsoft.com/en-us/download/details.aspx?id=36045>`_ (HPC Pack 2012 MS-MPI Redistributable Package). Install this pack to e.g. ``C:\opt\Microsoft_HPC_Pack_2012``. To check that MPI indeed works, edit the following ``hello.c`` file

.. code-block:: c

  #include <stdio.h>
  #include <mpi.h>
  
  int main(int argc, char **argv) {
    int rank, size;
  
    MPI_Init (&argc, &argv);
    MPI_Comm_rank (MPI_COMM_WORLD, &rank);
    MPI_Comm_size (MPI_COMM_WORLD, &size);
    printf( "Hello world from process %d of %d\n", rank, size);
    MPI_Finalize();
    return 0;
  }

When using this precompiled library with MinGW, you might run into the following error::

  c:/opt/Microsoft_HPC_Pack_2012/Inc/mpi.h:137:1: error: unknown type name '__int64' typedef __int64 MPI_Offset;

``__int64__`` is defined in the header file ``_mingw.h``, so I just added the following line

.. code-block:: c

  #include <_mingw.h>

at the top of file ``C:\opt\Microsoft_HPC_Pack_2012\Inc\mpi.h``.

This pack does not ship with a version of ``mpicc``. Therefore, to compile, you need to specify the full path to the MPI headers and libraries::

 $ mingw32-gcc -o hello.exe hello.c -I/C/opt/Microsoft_HPC_Pack_2012/Inc -L/C/opt/Microsoft_HPC_Pack_2012/Lib/i386 -lmsmpi

Note that the program is linked against the 32 bit library, as the standard MinGW is a 32 bit system. Then run the example::

  $ /C/opt/Microsoft_HPC_Pack_2012/Bin/mpiexec.exe -np 4 hello.exe
  Hello world from process 3 of 4
  Hello world from process 1 of 4
  Hello world from process 2 of 4
  Hello world from process 0 of 4

It works!

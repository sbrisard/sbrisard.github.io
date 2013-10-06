****************************************************
Scientific computing under Windows 7, part 2: OpenMP
****************************************************
From the `official website <http://www.openmp.org/>`_

    The OpenMP API defines a portable, scalable model with a simple and flexible interface for developing parallel applications on platforms from the desktop to the supercomputer.

To use OpenMP with MinGW, you must install the following packages (using the ``mingw-get`` installer)

    - ``mingw32-pthreads-w32``,
    - ``mingw32-libgomp``.

To check that OpenMP indeed works, create the following ``hello.c`` source file

.. code-block:: c

    #include <omp.h>
    #include <stdio.h>

    int main(int argc, char argv[]) {
      int id;
    #pragma omp parallel private(id)
      {
        id = omp_get_thread_num();
        printf("%d: Hello World!\n", id);
      }
      return 0;
    }

and compile it as follows (in the MSYS console)::

    $ gcc -fopenmp -o hello hello.c

Running the resulting executable on my laptop (4 processors) leads to the following output::

    $ ./hello.exe
    2: Hello World!
    0: Hello World!
    1: Hello World!
    3: Hello World!

#include <math.h>
#include <fftw3.h>
#include <fftw3-mpi.h>

int main(int argc, char** argv) {
  const ptrdiff_t n0 = 1024;
  const ptrdiff_t n1 = 2048;

  MPI_Init(&argc, &argv);
  fftw_mpi_init();

  int rank;
  ptrdiff_t i, j, global_offset;
  ptrdiff_t local_n0, local_start, alloc_local, local_offset;
  double norm = 0., re, im;

  fftw_complex *a, *expected, *actual;
  fftw_plan p;

  a = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * n0 * n1);
  expected = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * n0 * n1);
  p = fftw_plan_dft_2d(n0, n1, a, expected, FFTW_FORWARD, FFTW_ESTIMATE);
  
  for (i = 0; i < n0; i++) {
    for (j = 0; j < n1; j++) {
      global_offset = i * n1 + j;
      double arg = M_PI * (i / (double) n0 + j / (double) n1);
      a[global_offset][0] = cos(arg);
      a[global_offset][1] = sin(arg);
    }
  }

  fftw_execute(p);
  fftw_destroy_plan(p);

  alloc_local = fftw_mpi_local_size_2d(n0, n1, MPI_COMM_WORLD,
                                       &local_n0, &local_start);
  actual = fftw_malloc(sizeof(fftw_complex) * alloc_local);
  p = fftw_mpi_plan_dft_2d(n0, n1, actual, actual, MPI_COMM_WORLD,
                           FFTW_FORWARD, FFTW_ESTIMATE);

  for (i = 0; i < local_n0; ++i) {
    for (j = 0; j < n1; j++) {
      local_offset = i * n1 + j;
      global_offset = (local_start + i) * n1 + j;
      actual[local_offset][0] = a[global_offset][0];
      actual[local_offset][1] = a[global_offset][1];
    }
  }
  
  fftw_execute(p);
  fftw_destroy_plan(p);

  for (i = 0; i < local_n0; i++) {
    for (j = 0; j < n1; j++) {
      local_offset = i * n1 + j;
      global_offset = (local_start + i) * n1 + j;
      re = expected[global_offset][0] - actual[local_offset][0];
      im = expected[global_offset][1] - actual[local_offset][1];
      norm += re * re + im * im;
    }
  }

  norm = sqrt(norm);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  printf("I'm process %d, local size is %d x %d, norm = %g\n",
         rank, local_n0, n1, norm);

  fftw_free(a);
  fftw_free(expected);
  fftw_free(actual);

  MPI_Finalize();
}

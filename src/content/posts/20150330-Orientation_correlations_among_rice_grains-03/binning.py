import functools
import os.path

import numpy as np
import skimage.io
import skimage.util

from numpy.lib.stride_tricks import as_strided

def read_slice(index):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        'original')
    filename = '{0:05d}.tif'.format(index)
    return skimage.io.imread(os.path.join(path, filename))


def write_slice(index, data):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        'bin_4x4x4')
    filename = 'rice-bin_4x4x4-{0:03d}.tif'.format(index)
    return skimage.io.imsave(os.path.join(path, filename), data)


if __name__ == '__main__':
    bin_size = 4
    num_slices = 689

    img = read_slice(0)
    old_shape = img.shape
    sum_z = np.zeros(old_shape, dtype=np.float64, order='C')
    new_shape = (tuple(ni//bin_size for ni in old_shape) + (bin_size, bin_size))
    new_strides = tuple(si*bin_size for si in sum_z.strides) + sum_z.strides
    add_to_sum_z = functools.partial(np.add, out=sum_z)

    out = np.empty((num_slices//bin_size,) +
                   tuple(ni//bin_size for ni in old_shape),
                   dtype=np.float64)
    for i in range(out.shape[0]):
        # We specify an initializer to reduce so as to force conversion of the
        # images to float64 (to avoid overflow). We must then set sum_z to 0 at
        # each iteration.
        print(i)
        sum_z[...] = 0.0
        functools.reduce(add_to_sum_z,
                         (read_slice(bin_size*i + j) for j in range(bin_size)),
                         sum_z)
        np.sum(as_strided(sum_z, shape=new_shape, strides=new_strides),
               axis=(2, 3), out=out[i])

    min_value, max_value = np.min(out), np.max(out)
    np.subtract(out, min_value, out)
    np.multiply(255.0/(max_value-min_value), out, out)
    out = out.astype(np.uint8)
    for i in range(out.shape[0]):
        write_slice(i, out[i])

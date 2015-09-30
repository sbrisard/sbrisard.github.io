import os.path

import h5py
import numpy as np
import skimage.io

if __name__ == '__main__':
    root =  os.path.join('F:\\', 'sebastien', 'experimental_data', 'navier',
                         'riz')
    input_name = os.path.join(root, 'bin_4x4x4-otsu',
                              'rice-bin_4x4x4-otsu_126-{0:03d}.tif')
    output_name = os.path.join(root, 'rice-bin_4x4x4.hdf5')
    num_slices = 172

    binary = None
    for i in range(num_slices):
        slc = skimage.io.imread(input_name.format(i))
        if binary is None:
            binary = np.zeros((num_slices,)+slc.shape, dtype=slc.dtype)
        binary[i] = slc

    with h5py.File(output_name, 'w') as f:
        dset=f.create_dataset('binary', data=binary)
        dset.attrs['description'] = np.string_('Otsu threshold 126')

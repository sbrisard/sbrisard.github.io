import os.path

import h5py
import numpy as np

from scipy import ndimage as ndi
from skimage.io import imsave

if __name__ == '__main__':
    root =  os.path.join('F:\\', 'sebastien', 'experimental_data', 'navier',
                         'riz')
    with h5py.File(os.path.join(root, 'rice-bin_4x4x4.hdf5')) as f:
        binary = np.asarray(f['binary'])

    print('Selecting markers from distance local maxima...')
    labels, num_labels = ndi.label(binary,
                                   structure=np.ones((3, 3, 3), dtype=np.int8))
    print('    ... found {} connected components'.format(num_labels))

    index = 100
    np.random.seed(20150928)
    colors = np.random.randint(255, size=(labels.max()+1, 3)).astype(np.uint8)
    colors[0] = [0, 0, 0]

    imsave('connected_components.png', colors[labels[index]])

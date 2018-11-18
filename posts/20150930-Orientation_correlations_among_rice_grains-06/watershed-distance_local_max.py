"""Watershed using local maxima of the distance map as seeds."""

import os.path

import h5py
import numpy as np

from scipy import ndimage as ndi
from skimage.feature import peak_local_max
from skimage.io import imread, imsave, imshow
from skimage.morphology import watershed

def markers_from_distance_local_max(image, distance=None, min_distance=10):
    if distance is None:
        distance = ndi.distance_transform_edt(image)
    return

if __name__ == '__main__':
    root =  os.path.join('F:\\', 'sebastien', 'experimental_data', 'navier',
                         'riz')
    with h5py.File(os.path.join(root, 'rice-bin_4x4x4.hdf5')) as f:
        binary = np.asarray(f['binary'])

    print('Computing distance transform')
    distance = ndi.distance_transform_edt(binary)

    print('Selecting markers from distance local maxima...')
    local_maxi = peak_local_max(distance, labels=binary,
                                min_distance=10,
                                indices=False)
    markers, num_seeds = ndi.label(local_maxi,
                                   structure=np.ones((3, 3, 3), dtype=np.int8))
    print('    ... found {} seeds'.format(num_seeds))

    print('Computing watershed transform')
    labels = watershed(-distance, markers, mask=binary)

    index = 100
    np.random.seed(20150929)
    colors = np.random.randint(255, size=(labels.max()+1, 3)).astype(np.uint8)
    colors[0] = [0, 0, 0]

    imsave('distance.png', distance[index]/distance.max())
    imsave('watershed-distance_local_max.png', colors[labels[index]])

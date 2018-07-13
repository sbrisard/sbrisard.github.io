"""Watershed using directional erosions."""

import os.path

import h5py
import numpy as np

from scipy import ndimage as ndi
from skimage.feature import peak_local_max
from skimage.io import imread, imsave, imshow
from skimage.morphology import watershed

from spheroid import Spheroid


def icosahedron():
    t = (1+np.sqrt(5))/2
    u = t/np.sqrt(1+t**2)
    v = 1/np.sqrt(1+t**2)
    vertices = np.array([[ u,  v,  0], [-u,  v,  0], [ u, -v,  0],
                         [-u, -v,  0], [ v,  0,  u], [ v,  0, -u],
                         [-v,  0,  u], [-v,  0, -u], [ 0,  u,  v],
                         [ 0, -u,  v], [ 0,  u, -v], [ 0, -u, -v]],
                        dtype=np.float64)
    faces = np.array([[ 0,  8,  4], [ 0,  5, 10], [ 2,  4,  9], [ 2, 11,  5],
                      [ 1,  6,  8], [ 1, 10,  7], [ 3,  9,  6], [ 3,  7, 11],
                      [ 0, 10,  8], [ 1,  8, 10], [ 2,  9, 11], [ 3, 11,  9],
                      [ 4,  2,  0], [ 5,  0,  2], [ 6,  1,  3], [ 7,  3,  1],
                      [ 8,  6,  4], [ 9,  4,  6], [10,  5,  7], [11,  7,  5]],
                     dtype=np.uint8)
    return vertices, faces


if __name__ == '__main__':
    root =  os.path.join('F:\\', 'sebastien', 'experimental_data', 'navier',
                         'riz')
    with h5py.File(os.path.join(root, 'rice-bin_4x4x4.hdf5')) as f:
        binary = np.asarray(f['binary'])

        print('Computing distance transform')
        distance = ndi.distance_transform_edt(binary)
        dset = f.create_dataset('distance', data=distance)
        dset.attrs['description'] = np.string_('distance transform of `binary`')

        print('Selecting markers from directional erosion...')
        a, c = 3.5, 9.5
        vertices  = icosahedron()[0]
        eroded = np.zeros_like(binary, dtype=np.bool)
        for v in vertices:
            spheroid = Spheroid(a, c, v).digitize()
            np.logical_or(eroded,
                          ndi.binary_erosion(binary,
                                             structure=spheroid),
                          out=eroded)
        markers, num_seeds =  ndi.label(eroded,
                                        structure=np.ones((3, 3, 3),
                                                          dtype=np.int8))
        dset = f.create_dataset('markers', data=markers)
        descr = ('`binary` image was eroded with 20 spheroids '+
                 '(a={}, c={}) '.format(a, c)+
                 'using the vertices of a icosahedron as orientations. This'+
                 'image is the logical OR of all 20 eroded images.')
        dset.attrs['description'] = np.string_(descr)
        print('    ... found {} seeds'.format(num_seeds))

        print('Computing watershed transform')
        labels = watershed(-distance, markers, mask=binary)
        dset = f.create_dataset('labels', data=labels)
        descr = 'watershed using `markers` and the opposite of `distance`.'
        dset.attrs['description'] = np.string_(descr)

    index = 100
    np.random.seed(20150924)
    colors = np.random.randint(255, size=(labels.max()+1, 3)).astype(np.uint8)
    colors[0] = [0, 0, 0]

    imsave('distance.png', distance[index]/distance.max())
    imsave('makers-directional_erosion.png', colors[markers[index]])
    imsave('watershed-directional_erosion.png', colors[labels[index]])

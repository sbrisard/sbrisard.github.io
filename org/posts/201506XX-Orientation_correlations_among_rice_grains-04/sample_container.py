import numpy as np

from scipy.signal import argrelmax

from skimage.color import gray2rgb
from skimage.draw import circle_perimeter
from skimage.feature import canny
from skimage.io import imread, imshow
from skimage.transform import hough_circle
from skimage.util import img_as_ubyte

def find_boundary(img, r_min, r_max):
    edges = canny(img, sigma=0.)
    radii = np.arange(r_min, r_max)
    h = hough_circle(edges, radii)
    h_max = np.max(h, axis=(1, 2))
    k = np.min(np.argsort(h_max)[-2:])
    h = h[k, ...]
    r, c = np.unravel_index(np.argmax(h), h.shape)
    return r, c, radii[k]

if __name__ == '__main__':
    name = 'rice-bin_4x4x4-099.tif'
    img = imread(name)
    rc, cc, radius = find_boundary(img, 190, 220)

    img_rgb = gray2rgb(img_as_ubyte(img))
    r, c = circle_perimeter(rc, cc, radius, method='andres')
    img_rgb[r, c] = (255, 0, 0)

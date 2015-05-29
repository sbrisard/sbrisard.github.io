import os.path
import numpy as np

from skimage.color import gray2rgb
from skimage.draw import circle_perimeter
from skimage.feature import canny
from skimage.io import imread, imsave
from skimage.transform import hough_circle
from skimage.util import img_as_ubyte


def find_boundary(img, min_radius, max_radius):
    edges = canny(img, sigma=0.)
    radii = np.arange(min_radius, max_radius)
    h = hough_circle(edges, radii)
    h_max = np.max(h, axis=(1, 2))
    k = np.min(np.argsort(h_max)[-2:])
    radius = radii[k]
    h = h[k, ...]
    row, col = np.unravel_index(np.argmax(h), h.shape)
    return row, col, radius


def draw_boundary(img, row, col, radius):
    img_rgb = gray2rgb(img_as_ubyte(img))
    rows, cols = circle_perimeter(row, col, radius, method='andres')
    img_rgb[rows, cols] = (255, 0, 0)
    return img_rgb


if __name__ == '__main__':
    root = os.path.join('F:', 'sebastien', 'experimental_data', 'navier', 'riz')
    input_dir = os.path.join(root, 'bin_4x4x4')
    output_dir = os.path.join(root, 'boundary')
    input_name = 'rice-bin_4x4x4-{0:03d}.tif'
    output_name = 'rice-bin_4x4x4-boundary-{0:03d}.png'
    num_slices = 172
    min_radius = 190
    max_radius = 220

    circle_params = np.zeros((num_slices, 3), dtype=np.uint16)
    for i in range(num_slices):
        img = imread(os.path.join(input_dir, input_name.format(i)))
        circle_params[i] = find_boundary(img, min_radius, max_radius)
        img = draw_boundary(img, *circle_params[i])
        imsave(os.path.join(output_dir, output_name.format(i)), img)
    np.save('./circle_params.npy', circle_params)

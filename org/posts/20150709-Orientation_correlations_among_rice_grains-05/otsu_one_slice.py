import os.path

import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
from skimage.draw import circle
from skimage.filters import threshold_otsu
from skimage.io import imread, imsave, imshow
from skimage.util import img_as_ubyte

def gaussian_mixture(x, mu0, sig0, w0, mu1, sig1, w1):
    return (w0*np.exp(-((x-mu0)/sig0)**2/2)+
            w1*np.exp(-((x-mu1)/sig1)**2/2))

if __name__ == '__main__':
    name = os.path.join('.', 'rice-bin_4x4x4-099.tif')
    img = imread(name)
    rows, cols = circle(219, 217, 208)

    t = threshold_otsu(img)
    print(t)
    t = threshold_otsu(img[rows, cols])
    print(t)
    mask = np.zeros_like(img, dtype=np.bool)
    mask[rows, cols] = True
    binary = np.logical_and(img > t, mask)
    imsave(os.path.join('.', 'rice-bin_4x4x4-otsu-099.png'),
           img_as_ubyte(binary))

    fig = plt.figure(figsize=(3, 1))
    h, bins, patches = plt.hist(img[rows, cols], bins=256, range=(0, 256))
    ax, = fig.get_axes()
    ax.set_xlabel('Gray value')
    ax.set_ylabel('Pixel count')
    ax.set_xlim(0, 250)
    plt.savefig('hist.svg', transparent=True)

    popt, pcov = curve_fit(xdata=bins[:-1], ydata=h, f=gaussian_mixture,
                           p0=[37, 1, 1, 210, 1, 1])

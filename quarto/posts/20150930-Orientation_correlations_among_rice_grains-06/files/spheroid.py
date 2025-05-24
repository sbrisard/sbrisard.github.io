import numpy as np

class Spheroid:
    def __init__(self, a, c, d=None, dim=None):
        if ((d is None) + (dim is None)) != 1:
            raise ValueError('d and dim cannot be specified simultaneously')
        self.a = a
        self.c = c
        if d is None:
            self.d = np.zeros((dim,), dtype=np.float64)
            self.d[-1] = 1.
        else:
            self.d = np.asarray(d)
            dim = len(d)
        p = np.outer(self.d, self.d)
        q = np.eye(dim, dtype=np.float64) - p
        self.Q = c**2*p+a**2*q
        self.invQ = p/c**2+q/a**2

    def __str__(self):
        return ('spheroid: a = {}, c = {3}, d = {}, ').format(tuple(self.d),
                                                              self.a,
                                                              self.c)

    def bounding_box(self):
        return np.sqrt(np.diag(self.Q))

    def criterion(self, x):
        """Ordering of points: ``x[i, ...]`` is the i-th coordinate"""
        y = np.tensordot(self.invQ, x, axes=([-1], [0]))
        np.multiply(x, y, y)
        return np.sum(y, axis=0)

    def digitize(self, h=1.0):
        bb = self.bounding_box()
        i_max = np.ceil(bb/h-0.5)
        bb = i_max*h
        shape = 2*i_max+1

        slices = [slice(-x, x, i*1j) for (x, i) in zip(bb, shape)]
        x = np.mgrid[slices]
        return self.criterion(x)<=1.0

# This is a function that implements a Whittaker smoother in Python. 
# Source: https://gist.github.com/zmeri/3c43d3b98a00c02f81c2ab1aaacc3a49

import scipy
import scipy.sparse.linalg
import numpy as np

def whittaker_filter(y, lmda=1.0):
    m = len(y)
    E = scipy.sparse.identity(m)
    d1 = -1 * np.ones((m), dtype='d')
    d2 = 3 * np.ones((m), dtype='d')
    d3 = -3 * np.ones((m), dtype='d')
    d4 = np.ones((m), dtype='d')
    D = scipy.sparse.diags([d1, d2, d3, d4], [0, 1, 2, 3], shape=(m - 3, m), format="csr")
    z = scipy.sparse.linalg.cg(E + lmda * (D.transpose()).dot(D), y)
    return z[0]

#!/Users/Juliette/miniconda2/bin/python

import numpy as np

def is_prime(nb):
    k = 2
    while k <= np.sqrt(nb):
        if nb % k == 0:
            return False
        k += 1
    return True

def find_sum(n):
    s = 0
    for nb in xrange(2,n):
        if is_prime(nb):
            s += nb
    return s

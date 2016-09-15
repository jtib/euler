#!/Users/Juliette/miniconda2/bin/python

import time

def nb_divisors(nb):
    """ returns the number of divisors of nb
    """
    nb_div = 1
    k = 2
    n = nb
    while n > 1:
        p = 1
        while n % k == 0:
            n /= k
            p += 1
        nb_div *= p
        k += 1
    return nb_div

def first_trnb_more(k):
    """ Returns the first triangular number with more than k divisors
    """
    t0 = time.clock()
    trnb = 1
    count = 2
    while nb_divisors(trnb) < k:
        print trnb
        trnb += count
        count += 1
    print "time: ",time.clock()-t0
    return trnb

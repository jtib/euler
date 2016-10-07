#!/Users/Juliette/miniconda2/bin/python

""" Longest Collatz sequence
"""

def steps(nb):
    """ returns the number of steps needed to reach 1 in a Collatz
    sequence that starts from n
    """
    n = nb
    s = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        s += 1
    return s

def max_steps(nb):
    """ returns the starting point of the longest Collatz sequence for
    numbers leq nb
    """
    cur_max = 0
    start_pt = 1
    for n in xrange(1,nb+1):
        s = steps(n)
        if steps(n) > cur_max:
            start_pt = n
            cur_max = s
    return start_pt

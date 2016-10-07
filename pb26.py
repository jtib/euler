#!/Users/Juliette/miniconda2/bin/python

def cycle_length(n):
    """
    Returns the start place and length of the cycle in the decimal
    expansion of 1/n.
    """
    d = {}
    found = False
    k = 1
    while not found:
        found = (10**k)%n in d.values()
        d[k] = (10**k)%n
        k += 1
    l = [p for p in d.keys() if (10**(k-1))%n == (10**p)%n]
    (s,t) = (l[0],l[1]-l[0])
    return (s,t)

def main():
    m = 0
    nb = 1

    for n in xrange(2,1000):
        if n%2 != 0 and n%5 != 0:
            (s,t) = cycle_length(n)
            if t > m:
                m = t
                nb = n

    print nb


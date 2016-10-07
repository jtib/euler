from numpy import sqrt
from itertools import product
from random import randint

def modular_exponentiation(a, b, n):
    c = 0
    d = 1
    binb = bin(b)[2:]
    for i in xrange(len(binb)-1,-1,-1):
        c *= 2
        d = (d*d)%n
        if binb[i] == '1':
            c += 1
            d = (d*a)%n
    return d


def witness(a, n):
    u = n - 1
    t = 0
    print "{2}-1=2**{0}*{1}".format(t,u,n)
    while u%2 == 0:
        print "loop"
        t += 1
        u /= 2
    x = list()
    x.append(modular_exponentiation(a, u, n))
    for i in xrange(1,t+1):
        x.append(x[i-1]**2 % n)
        if x[i] == 1 and x[i-1] != 1 and x[i-1] != (n-1):
            return True
    if x[t] != 1:
        return True
    return False


def is_prime(n, s):
    """
    Through Miller-Rabin
    """
    for j in xrange(1,s+1):
        a = randint(1,n)
        if witness(a, n):
            return False
    return True


def list_primes(N):
    """
    Lists all primes below N.
    """
    return [k for k in xrange(2, N) if is_prime(k)]


def len_prime_seq(a, b, N):
    """
    Returns:
    . length of the sequence of primes generated by (a, b)
    . a * b
    """
    f = lambda x: x**2 + a*x + b
    return (len([x for x in xrange(2*N) if is_prime(f(x))]), a*b)


def search_longest(N):
    """
    Returns:
        . a*b s.t. a and b form the longest prime sequence for a, b below N
        . length of that sequence
    """
    l_max = 0
    prod = 0
    prime_list = list_primes(N)
    for a, b in [p for p in product(prime_list, prime_list) if p[0]<p[1]]:
        m = max(len_prime_seq(a, b, N), len_prime_seq(-a, b, N))
        prod = (prod, a*b)[m > l_max]
        l_max = max(l_max, m)
    return (prod, l_max)



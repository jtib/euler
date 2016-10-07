#!/Users/Juliette/miniconda2/bin/python

def solution():
    amicables = {}

    for nb in xrange(1,10000):
        if nb not in amicables:
            prop_div = [i for i in xrange(1,nb/2+1) if nb%i == 0]
            d = sum(prop_div)
            if d != nb:
                prop_div_d = [i for i in xrange(1,d/2+1) if d%i == 0]
                d_d = sum(prop_div_d)
                if d_d == nb:
                    amicables[d] = nb
                    amicables[nb] = d

    print sum(amicables.keys())





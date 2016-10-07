#!/Users/Juliette/miniconda2/bin/python

#abundant = []

# find all abundant numbers below 28123 (not very efficient, but with
# addition, hard to do better)
#for nb in xrange(1,28123):
#    prop_div = [i for i in xrange(1,nb/2+1) if nb%i==0]
#    d = sum(prop_div)
#    if d > nb:
#        abundant.append(nb)
abundant = [nb for nb in xrange(1,28123) if sum([i for i in xrange(1,nb/2+1) if nb%i==0]) > nb]

# get all sum combinations and sum it
# trivially equal to (len()+1)*sum(list)
ns = sum(set(i+j for i in abundant for j in abundant if i+j<=28123))
print ns

# deduce sum of other numbers by substracting previous one from sum of all
s = sum(xrange(1,28124)) - ns
print s

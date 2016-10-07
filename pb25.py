#!/Users/Juliette/miniconda2/bin/python

def fibiter(n):
    i = 1
    j = 1
    for k in xrange(n):
        j = j+i
        i = j-i # previous number
    return j

n = 1
while len(str(fibiter(n))) < 1000:
    n += 1

print n+2
print fibiter(n)

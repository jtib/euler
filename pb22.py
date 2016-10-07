#!/Users/Juliette/miniconda2/bin/python

# Getting the list of names
with open("p022_names.txt",'r') as f:
    li = f.read()

# Sorting it in alphabetical order
li = li.split(',')
li.sort()

# Summing everything
print sum([(i+1)*(ord(li[i][j].lower())-96) for i in xrange(len(li)) for j in xrange(1,len(li[i])-1)])

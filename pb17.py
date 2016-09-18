#!/Users/Juliette/miniconda2/bin/python

import re

def fill_dict(dictionary = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,00:7}):
    for k in xrange(21,100):
        if k not in dictionary:
            first = (str(k))[0] + str(0)
            letters1 = dictionary.get(int(first))
            second = (str(k))[1]
            letters2 = dictionary.get(int(second))
            dictionary.setdefault(k,letters1+letters2)
    return dictionary


def nb_letters(n,dictionary):
    if n in dictionary:
        return dictionary.get(n)
    first = (str(n))[0] # first digit
    remaining = (str(n))[1:3] # last two digits
    letters = dictionary.get(int(first)) + dictionary.get(int(remaining))
    if remaining != "00":
        letters += 10 # hundred and
    return letters


def main():

    dictionary = fill_dict()

    s = sum(dictionary.keys())

    for k in xrange(100,1000):
        s += nb_letters(k,dictionary)

    s += 11 # for 1000 (one thousand)
    s -= 7 # for "00"
    print s

# with_regexp():
def lett():
    for k in xrange(1,1001):
        yield len("".join(re.findall(r"[\w']+",p.number_to_words(k))))

# then do sum(lett())

from collections import defaultdict
from util import tokenedlines

def freqs1(hand):
    fs = defaultdict(int)
    for x in hand:
        fs[x] += 1
    return sorted(fs.values())

def freqs2(hand):
    jokers = 0
    fs = defaultdict(int)
    for x in hand:
        if x != 'J':
            fs[x] += 1
        else:
            jokers += 1
    ret = sorted(fs.values())
    if ret == []:
        return [5]
    ret[-1] += jokers
    return ret

def fiveofakind(hand, freqs):
    f = freqs(hand)
    return f == [5]

def fourofakind(hand, freqs):
    f = freqs(hand)
    return f == [1,4]

def fullhouse(hand, freqs):
    f = freqs(hand)
    return f == [2,3]

def threeofakind(hand, freqs):
    f = freqs(hand)
    return f == [1,1,3]

def twopair(hand, freqs):
    f = freqs(hand)
    return f == [1,2,2]

def pair(hand, freqs):
    f = freqs(hand)
    return f == [1,1,1,2]

def highcard(hand, freqs):
    f = freqs(hand)
    return f == [1,1,1,1,1]

funcs = [
    fiveofakind,
    fourofakind,
    fullhouse,
    threeofakind,
    twopair,
    pair,
    highcard
]

def torank(card):
    return '23456789TJQKA'.index(card)

def tocomp(hand):
    return [func(hand, freqs1) for func in funcs] + [torank(c) for c in hand]

def torank2(card):
    return 'J23456789TQKA'.index(card)

def tocomp2(hand):
    return [func(hand, freqs2) for func in funcs] + [torank2(c) for c in hand]

data = tokenedlines("7")
tuples = []
for row in data:
    #tuples.append((tocomp(str(row[0])), row[0], row[1]))
    tuples.append((tocomp2(str(row[0])), row[0], row[1]))

print(tuples)
res = 0
sortedlist = sorted(tuples)
#sortedlist.reverse()
for i, tup in enumerate(sortedlist):
    res += tup[2] * (i + 1)
    print(tup[2] * (i + 1), tup, (i+1))
print(res)

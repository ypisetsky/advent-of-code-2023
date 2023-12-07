
from collections import defaultdict

from util import tokenedlines

def freqs1(hand):
    fs = defaultdict(int)
    for x in hand:
        fs[x] += 1
    return sorted(fs.values(), reverse=True)

def freqs2(hand):
    jokers = 0
    fs = defaultdict(int)
    for x in hand:
        if x != 'J':
            fs[x] += 1
        else:
            jokers += 1
    ret = sorted(fs.values(),reverse=True) + [0]
    ret[0] += jokers
    return ret

def torank(card):
    return '23456789TJQKA'.index(card)

def torank2(card):
    return 'J23456789TQKA'.index(card)

def tocomp(hand):
    return freqs1(hand) + [torank(c) for c in hand]

def tocomp2(hand):
    return freqs2(hand) + [torank2(c) for c in hand]

data = tokenedlines("7")
p1 = []
p2 = []
for row in data:
    p1.append((tocomp(str(row[0])), row[1], row[0]))
    p2.append((tocomp2(str(row[0])), row[1], row[0]))

res = 0
for i, row in enumerate(sorted(p1)):
    res += row[1] * (i+1)
print(res)
res = 0
for i, row in enumerate(sorted(p2)):
    res += row[1] * (i+1)
print(res)
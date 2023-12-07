
from collections import defaultdict

from util import tokenedlines

def freqs(hand):
    fs = defaultdict(int)
    for x in hand:
        fs[x] += 1
    jokers = fs['N']
    del fs['N']
    ret = sorted(fs.values(),reverse=True) + [0]
    ret[0] += jokers
    return ret

def sortkey(hand):
    return freqs(hand) + ['N23456789TJQKA'.index(c) for c in hand]


data = tokenedlines("7")

print(sum(
    (i+1) * row[1] for i, row in enumerate(sorted(data, key=lambda row: sortkey(str(row[0]))))
))

print(sum(
    (i+1) * row[1] for i, row in enumerate(sorted(data, key=lambda row: sortkey(str(row[0]).replace('J', 'N'))))
))

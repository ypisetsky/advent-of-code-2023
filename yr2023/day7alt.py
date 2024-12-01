from collections import defaultdict

from util import tokenedlines, e


def sortkey(hand):
    freqs = defaultdict(int)
    for card in hand:
        freqs[card] += 1
    jokers = freqs["N"]
    del freqs["N"]
    ret = (
        sorted(freqs.values(), reverse=True)
        + [0]
        + ["N23456789TJQKA".index(c) for c in hand]
    )
    ret[0] += jokers
    return ret


data = tokenedlines("7")

print(
    sum(
        (i + 1) * row[1]
        for i, row in e(sorted(data, key=lambda row: sortkey(str(row[0]))))
    )
)

print(
    sum(
        (i + 1) * row[1]
        for i, row in e(
            sorted(data, key=lambda row: sortkey(str(row[0]).replace("J", "N")))
        )
    )
)

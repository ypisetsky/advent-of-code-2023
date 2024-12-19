from functools import cache
from util import getlines, tokenedlines

day = "19"

data = getlines(day)
patterns = frozenset(data[0].split(", "))
targets = data[1:]

@cache
def count_ways(target, patterns):
    if target == "":
        return 1
    ways = 0
    for pattern in patterns:
        if target.startswith(pattern):
            ways += count_ways(target[len(pattern):], patterns)
    return ways

print(sum(1 if count_ways(target, patterns) > 0 else 0 for target in targets))
print(sum(count_ways(target, patterns) for target in targets))

from util import tokenedlines
from collections import defaultdict

data = tokenedlines("1")
first = sorted([r[0] for r in data])
second = sorted([r[1] for r in data])
freqs = defaultdict(int)
for num in second:
    freqs[num] += 1

print(sum(abs(first[i] - second[i]) for i in range(len(data))))
print(sum(num * freqs[num] for num in first))
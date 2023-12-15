from collections import defaultdict
from util import tokenedlines, e

data = tokenedlines("4")

def parseline(line):
    for i in range(len(line)):
        if line[i] == '|':
            break
    winners = line[2:i]
    me = line[i+1:]
    return winners,me

res = 0
for line in data:
    winners,me = parseline(line)
    score = 1
    for x in me:
        if x in winners:
            score *= 2
    res += score // 2
print(res)


counts = {i: 1 for i in range(len(data))}

for i, line in e(data):
    winners,me = parseline(line)
    score = 0
    for x in me:
        if x in winners:
            score += 1
    for j in range(i + 1, min(i + score + 1, len(data))):
        counts[j] += counts[i]

print(sum(counts.values()))

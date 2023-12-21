from util import *
from collections import Counter

data = getlines("21")


for a in range(len(data)):
    for b in range(len(data[0])):
        if data[a][b] == 'S':
            i,j = a,b
            break

frontier = set([(i, j)])
for iter in range(65):
    newfrontier = set()
    for i, j in frontier:
        for x, y in neighbors4(i, j, data):
            if data[x][y] != '#':
                newfrontier.add((x, y))
    frontier = newfrontier
# 7584
# 3868
newdata = [row * 25 for row in data] * 25

for MUL in range(1, 5):
    i = j = 131 * 13 + 65
    frontier = set(neighbors4(i, j, newdata))
    lastfrontier = set(neighbors4(i, j, newdata))
    for iter in range(32 + 131 * MUL):
        newfrontier = set()
        for i, j in lastfrontier:
            for x, y in neighbors4(i, j, newdata):
                if newdata[x][y] == '#':
                    continue
                for a, b in neighbors4(x, y, newdata):
                    if (a, b) not in frontier and newdata[a][b] != '#':
                        newfrontier.add((a, b))
        frontier.update(newfrontier)
        lastfrontier = newfrontier
    buckets = defaultdict(int)
    for i, j in frontier:
        buckets[ (i // 131, j // 131)] += 1
    print(sorted(Counter(buckets.values()).items()))
    print(len(frontier))
    print(
        940 * (2 * MUL) +
        956 * (2 * MUL) +
        977 * (2 * MUL) +
        978 * (2 * MUL) +
        5719 + 5720 + 5732 + 5733 +
        6645 * (2 * MUL - 1) +
        6658 * (4 * MUL - 2) +
        6659 * (2 * MUL - 1) + 
        7584 * (2 * MUL - 1) * (2 * MUL - 1) +
        7613 * (4 * MUL * MUL)
    )

MUL = 202300 // 2
print(
    940 * (2 * MUL) +
    956 * (2 * MUL) +
    977 * (2 * MUL) +
    978 * (2 * MUL) +
    5719 + 5720 + 5732 + 5733 +
    6645 * (2 * MUL - 1) +
    6658 * (4 * MUL - 2) +
    6659 * (2 * MUL - 1) + 
    7584 * (2 * MUL - 1) * (2 * MUL - 1) +
    7613 * (4 * MUL * MUL)
)
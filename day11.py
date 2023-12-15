from util import getlines, e

data = getlines("11")
#data = getlines("11s")

addrows = set([])
for i,row in e(data):
    if '#' not in row:
        addrows.add(i)

addcols = set([])
for j in range(len(data[0])):
    if all(data[x][j] == '.' for x in range(len(data))):
        addcols.add(j)

galaxies = []
for i,row in e(data):
    for j,val in e(row):
        if val == '#':
            galaxies.append((i, j))

def dist(i, j, addrows, mul):
    if i > j:
        return dist(j, i, addrows, mul)
    res = 0
    while i < j:
        if i in addrows:
            res += mul
        else:
            res += 1
        i += 1
    return res

res = 0
for a in range(len(galaxies)):
    for b in range(a + 1, len(galaxies)):
        res += dist(galaxies[a][0], galaxies[b][0], addrows, 2)
        res += dist(galaxies[a][1], galaxies[b][1], addcols, 2)
print(res)

res = 0
for a in range(len(galaxies)):
    for b in range(a + 1, len(galaxies)):
        res += dist(galaxies[a][0], galaxies[b][0], addrows, 1000000)
        res += dist(galaxies[a][1], galaxies[b][1], addcols, 1000000)
print(res)

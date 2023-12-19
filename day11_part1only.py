from util import getlines, e

data = getlines("11")
# data = getlines("11s")


def addrow(grid, rowpos):
    return grid[:rowpos] + [grid[rowpos]] + grid[rowpos:]


def addcol(grid, colpos):
    return [row[:colpos] + row[colpos] + row[colpos:] for row in grid]


addrows = []
for i, row in e(data):
    if "#" not in row:
        addrows.append(i)

addrows.reverse()
for r in addrows:
    data = addrow(data, r)

addcols = []
for j in range(len(data[0])):
    if all(data[x][j] == "." for x in range(len(data))):
        addcols.append(j)
addcols.reverse()
for c in addcols:
    data = addcol(data, c)

galaxies = []
for i, row in e(data):
    for j, val in e(row):
        if val == "#":
            galaxies.append((i, j))

res = 0
for a in range(len(galaxies)):
    for b in range(a + 1, len(galaxies)):
        res += abs(galaxies[a][0] - galaxies[b][0])
        res += abs(galaxies[a][1] - galaxies[b][1])
        print(
            galaxies[a],
            galaxies[b],
            abs(galaxies[a][0] - galaxies[b][0]),
            abs(galaxies[a][1] - galaxies[b][1]),
        )
print(galaxies)
print(len(galaxies))
print(res)

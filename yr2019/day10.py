from math import gcd
from util import getlines, in_range

day = "10"

grid = getlines(day)

def get_visible_count(grid, row, col):
    ret = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#' and blockers(grid,row,col,i,j) == 0:
                ret += 1
    return ret

def blockers(grid, row, col, i, j):
    if row == i and j == col:
        return -1
    if row == i:
        dx = 0
        dy = 1 if j > col else -1
    if col == j:
        dx = 1 if i > row else -1
        dy = 0
    else:
        step_count = gcd(abs(i - row), abs(j - col))
        dx = (i - row) // step_count
        dy = (j - col) // step_count
    row += dx
    col += dy
    count = 0
    while row != i or col != j:
        if not in_range(row, col, len(grid), len(grid[0])):
            print(f"BAD {row} {col} {i} {j} {dx} {dy}")
        if grid[row][col] == '#':
            count += 1
        row += dx
        col += dy
    return count



best = 0
bestr = None
bestc = None
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '#' and get_visible_count(grid,r,c) > best:
            best = get_visible_count(grid,r,c)
            bestr = r
            bestc = c

print(best)

distances = {}
bestdist = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            distances[(i,j)] = blockers(grid, bestr, bestc, i, j)
            if distances[(i,j)] > bestdist:
                bestdist = distances[(i,j)]

def score(t):
    i, j = t
    slope = 0
    if j - bestc == 0:
        if i < bestr:
            quadrant = 0
        else:
            quadrant = 4
    elif j - bestc > 0:
        if i < bestr:
            quadrant = 1
            slope = (j - bestc) / (bestr - i)
        elif i == bestr:
            quadrant = 2
        else:
            quadrant = 3
            slope = (j - bestc) / (bestr - i)
    else:
        if i < bestr:
            quadrant = 7
            slope = (j - bestc) / (bestr - i)
        elif i == bestr:
            quadrant = 6
        else:
            quadrant = 5
            slope = (j - bestc) / (bestr - i)

    return (distances[(i, j)], quadrant, slope)

target = sorted(distances.keys(), key=score)[200]
print(target[1] * 100 + target[0])
print(bestr, bestc, list(enumerate(sorted(distances.keys(), key=score))))


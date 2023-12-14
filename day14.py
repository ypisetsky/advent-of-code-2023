from util import getlines

data = getlines("14")
#data = getlines("14s")


positions = []
obstacles = set()

for i, row in enumerate(data):
    for j, c in enumerate(row):
        if c == '#':
            obstacles.add((i, j))
        elif c == 'O':
            positions.append((i, j))

def neighbor(point, maxi, maxj, dir):
    i,j = point
    if dir == 0:
        if i == 0:
            return None
        return i-1, j
    elif dir == 1:
        if j == 0:
            return None
        return i, j-1
    elif dir == 2:
        if i == maxi - 1:
            return None
        return i+1, j
    else:
        if j == maxj - 1:
            return None
        return i, j+1


def walk(positions, obstacles, dir, maxi, maxj):
    newpositions = set()
    for point in sorted(positions, reverse=(dir >= 2)):
        while True:
            next = neighbor(point, maxi, maxj, dir)
            if not next or (next in obstacles) or (next in newpositions):
                newpositions.add(point)
                break
            else:
                point = next
    if len(positions) != len(newpositions):
        print("MISMATCH", dir, len(positions), len(newpositions), positions, newpositions)
    return frozenset(newpositions)

def score(positions, maxi):
    return sum(maxi - p[0] for p in positions)
i = 0
memo = {}
maxi = len(data)
maxj = len(data[0])

print(score(walk(positions, obstacles, 0, maxi, maxj), maxi))

while True:
    for dir in range(4):
        positions = walk(positions, obstacles, dir, maxi, maxj)
    i += 1
    if positions in memo:
        m = memo[positions]
        period = i - memo[positions]
        offset = (1000000000) % period
        for x, slot in memo.items():
            if slot % period == offset and slot >= m:
                print(score(positions, maxi))
        break
    else:
        memo[positions] = i
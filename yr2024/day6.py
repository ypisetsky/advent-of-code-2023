from util import getlines, in_range, printgrid, tokenedlines

day = 6
# day = "ex"

data = getlines(day)
obstacles = set()
for i, row in enumerate(data):
    for j, c in enumerate(row):
        if c == '#':
            obstacles.add((j, i))
        if c == '^':
            start = (j, i)
data = [list(row) for row in data]
res = 0

deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def walkguard(x, y, dir):
    visited = set()
    while True:
        visited.add((x, y))
        # print(count, x, y, dir)
        dx = deltas[dir][0]
        dy = deltas[dir][1]
        if not in_range(x + dx, y + dy, len(data[0]), len(data)):
            return visited
        if data[y+dy][x+dx] == '#':
            dir += 1
            dir %= 4
        else:
            x += dx
            y += dy


cells = walkguard(start[0], start[1], 0)
print(len(cells))


def isloop():
    visited = set()
    dir = 0
    x, y = start
    while True:
        visited.add((x, y, dir))
        dx = deltas[dir][0]
        dy = deltas[dir][1]
        if not in_range(x + dx, y + dy, len(data[0]), len(data)):
            return False
        if (x + dx, y + dy) in obstacles:
            dir += 1
            dir %= 4
        else:
            x += dx
            y += dy
        if (x,y,dir) in visited:
            return True

p2 = 0
for cell in cells:
    if cell not in obstacles:
        obstacles.add(cell)
        if isloop():
            p2 += 1
        obstacles.remove(cell)
print(p2)


from collections import deque
from util import *

data = tokenedlines("18")

dirs = {
    'R':  (0, 1), # right
    'D':  (1,0), # down
    'L':  (0, -1), # left
    'U':  (-1, 0), # up
}

curi = 10000
curj = 10000

boundary = [(curi,curj)]

for dir, dist, color in data:
    for i in range(dist):
        curi += dirs[dir][0]
        curj += dirs[dir][1]
        boundary.append((curi, curj))

boundary = set(boundary)
print(boundary)

def floodfill(boundary, starti, startj):
    filled = set()
    queue = deque([(starti, startj)])
    c = 0
    while len(queue) > 0:
        if len(filled) > 1000000:
            return -1
        curi, curj = queue.popleft()
        filled.add((curi, curj))
        for neighbor in neighbors4(curi, curj, 100000, 100000):
            if neighbor in boundary or neighbor in filled:
                continue
            queue.append(neighbor)
            filled.add(neighbor)
    return len(filled) + len(boundary)

print(floodfill(boundary, 10001, 10001))
print(floodfill(boundary, 10001, 9999))
print(floodfill(boundary, 9999, 10001))
print(floodfill(boundary, 9999, 9999))

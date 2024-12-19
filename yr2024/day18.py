from util import neighbors4, tokenedlines, getlines, Tuple
from heapq import heappush, heappop

day = "18"
import sys
sys.setrecursionlimit(100000)

points = [tuple(x) for x in tokenedlines(day, sep=",")]
size = 71 if day == "18" else 7
cutoff = 1024 if day == "18" else 12



# Write a function that determines the length of the shortest path from (0, 0) to (size-1, size-1) avoiding blockers
def shortest_path(blockers):
    start = (0, 0)
    end = (size-1, size-1)
    queue = [(0, start)]
    visited = set()
    while queue:
        dist, current = heappop(queue)
        if current == end:
            return dist
        if current in visited or current in blockers:
            continue
        visited.add(current)
        for neighbor in neighbors4(*current, size, size):
            heappush(queue, (dist + 1, neighbor))
    return None

d = points[:cutoff]
a = set(d)
print(shortest_path(a))
min = 1024
max = len(points)
while min < max:
    midpoint = (min + max) // 2
    if shortest_path(set(points[:midpoint])) is not None:
        min = midpoint + 1
    else:
        max = midpoint

print(max, points[min-1])
              
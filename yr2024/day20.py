from heapq import heappush, heappop

from util import getlines, in_range, neighbors4

data = getlines("20")
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_distances_from_point(start, grid, ban_hash):
    distances = {start: 0}
    parents = {start: set([])}
    queue = []
    heappush(queue, (0, start))
    visited = set()
    while len(queue) > 0:
        dist, loc = heappop(queue)
        if loc in visited:
            continue
        def handle_neighbor(newloc, newdist):
            r, c = newloc
            if not in_range(r, c, len(grid), len(grid[0])) or (grid[r][c] == '#' and ban_hash):
                return
            if newloc not in distances or distances[newloc] > newdist:
                heappush(queue, (newdist, newloc))
                distances[newloc] = newdist
                parents[newloc] = {loc}
            elif distances[newloc] == newdist:
                parents[newloc].add(loc)
        
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            handle_neighbor((loc[0] + dr, loc[1] + dc), dist + 1)
        visited.add(loc)

    return distances

for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == 'S':
            start = (y, x)
        elif char == 'E':
            end = (y, x)

from_start = get_distances_from_point(start, data, True)
from_end = get_distances_from_point(end, data, True)
best = from_start[end]
ret = 0

def neighbors_max_size(i, j, grid, dist):
    for newi in range(i - dist, i + dist + 1):
        for newj in range(j - dist, j + dist + 1):
            if in_range(newi, newj, len(grid), len(grid[0])) and abs(newi - i) + abs(newj - j) <= dist:
                yield (newi, newj)

def solve(data, from_start, from_end, max_dist):
    ret = 0
    for p1, d1 in from_start.items():
        for p2 in neighbors_max_size(*p1, data, max_dist):
            d2 = from_end.get(p2, None)
            if d2 is None:
                continue
            delta = manhattan_distance(p1, p2)
            if delta <= max_dist:
                if best - (d1 + d2 + delta) >= 100:
                    ret += 1
    return ret

print(solve(data, from_start, from_end, 2))
print(solve(data, from_start, from_end, 20))
from util import Tuple, getlines
from functools import cache
from heapq import heappop, heappush

day = "16"

grid = getlines(day)

DELTAS = {
    0: (0, -1, 0),
    1: (-1, 0, 0),
    2: (0, 1, 0),
    3: (1, 0, 0),
}

visited = set([])

@cache
def best_score(start):
    distances = {start: 0}
    parents = {start: set([])}
    queue = []
    heappush(queue, (0, start))
    visited = set()
    while len(queue) > 0:
        dist, loc = heappop(queue)
        # print(f"Processing {dist, loc}")
        if loc in visited:
            continue
        def handle_neighbor(newloc, newdist):
            r, c, d = newloc
            if grid[r][c] == '#' or d < 0 or d > 3:
                # print(f"Ignoring {newloc}")
                return
            if newloc not in distances or distances[newloc] > newdist:
                # print(f"Enqueueing {(newdist, newloc)}")
                heappush(queue, (newdist, newloc))
                distances[newloc] = newdist
                parents[newloc] = [loc]
            elif distances[newloc] == newdist:
                parents[newloc].append(loc)
        
        handle_neighbor(Tuple.add(loc, DELTAS[loc[2]]), dist + 1)
        for newdir in range(4):
            if newdir != loc[2]:
                handle_neighbor((loc[0], loc[1], newdir), dist + 1000)
        visited.add(loc)
    return distances, parents

epos = []
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == 'E':
            for i in range(4):
                epos.append((y, x, i))
         

def get_all_reachable(graph, pos):
    queue = [pos]
    ret = set([])
    while len(queue) > 0:
        pos = queue.pop()
        ret.add(pos[:2])
        queue.extend(graph[pos])
    return len(ret)


for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == 'S':
            scores, parents = best_score((y, x, 2))
            print(scores[epos[2]])
            print(get_all_reachable(parents, epos[2]))
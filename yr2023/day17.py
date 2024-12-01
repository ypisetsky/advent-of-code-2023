import heapq
from util import *

data = getlines("17")

dirs = [
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
    (-1, 0),  # up
]


def getdirs1(dir, constdir):
    directions = [0, 1, 2, 3]
    directions.remove((dir + 2) % 4)
    if constdir == 3:
        directions.remove(dir)
    return directions


def getdirs2(dir, constdir):
    directions = [0, 1, 2, 3]
    directions.remove((dir + 2) % 4)
    if constdir != 0 and constdir < 4:
        directions = [dir]
    elif constdir == 10:
        directions.remove(dir)
    return directions


def bfs(graph, start, getdirs):
    visited = set()
    distances = {start: 0}
    queue = []
    heapq.heappush(queue, (0, start))
    while len(queue) > 0:
        currdist, curr = heapq.heappop(queue)
        i, j, dir, constdir = curr
        if curr in visited or i >= len(graph) or i < 0 or j >= len(graph[0]) or j < 0:
            continue
        visited.add(curr)
        directions = getdirs(dir, constdir)
        for newdir in directions:
            nexti = i + dirs[newdir][0]
            nextj = j + dirs[newdir][1]
            if nexti >= len(graph) or nexti < 0 or nextj >= len(graph[0]) or nextj < 0:
                continue
            newdist = ord(graph[nexti][nextj]) - ord("0") + currdist
            newpos = (nexti, nextj, newdir, 1 + (constdir if newdir == dir else 0))
            if newpos not in distances or newdist < distances[newpos]:
                distances[newpos] = newdist
                heapq.heappush(queue, (newdist, newpos))
    return distances


bestbypos = {}
for (i, j, dir, constdir), score in bfs(data, (0, 0, 0, 0), getdirs1).items():
    if (i, j) not in bestbypos or bestbypos[(i, j)] >= score:
        bestbypos[(i, j)] = score
print(bestbypos[(len(data) - 1, len(data[0]) - 1)])

bestbypos = {}
for (i, j, dir, constdir), score in bfs(data, (0, 0, 0, 0), getdirs2).items():
    if (i, j) not in bestbypos or bestbypos[(i, j)] >= score:
        bestbypos[(i, j)] = score
print(bestbypos[(len(data) - 1, len(data[0]) - 1)])

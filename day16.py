from collections import deque
from util import getlines

data = getlines("16")
# data = getlines("16s")

dirs = [
      (0, 1), # right
      (1,0), # down
      (0, -1), # left
      (-1, 0), # up
]

transforms = {
      '.': [0, 1, 2, 3],
      '\\': [1, 0, 3, 2],
      '/': [3, 2, 1, 0],
      '|': [(1, 3) , 1, (1,  3), 3],
      '-': [0, (0, 2), 2, (0, 2)],
}

def bfs(graph, start):
      visited = set()
      queue = deque([start])
      while len(queue) > 0:
            curr = queue.popleft()
            i, j, dir = curr
            if curr in visited or i >= len(graph) or i < 0 or j >= len(graph[0]) or j < 0:
                  continue
            visited.add(curr)
            target_or_targets = transforms[graph[i][j]][dir]
            if isinstance(target_or_targets, int):
                  target_or_targets = [target_or_targets]
            for newdir in target_or_targets:
                  queue.append((i + dirs[newdir][0], j + dirs[newdir][1], newdir))
      return visited

def unique(points):
      newpoints = set()
      for i, j, dir in points:
            newpoints.add((i, j))
      return len(newpoints)

print(unique(bfs(data, (0, 0, 0))))

maxi = len(data)
maxj = len(data[0])
starts = [(i, 0, 0) for i in range(maxi)] + \
      [(i, maxj - 1, 2) for i in range(maxi)] + \
      [(0, j, 1) for j in range(maxj)] + \
      [(maxi - 1, j, 3) for j in range(maxj)]

print(max(unique(bfs(data, start)) for start in starts))

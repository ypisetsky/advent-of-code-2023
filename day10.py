from util import getlines, neighbors4, e
from collections import deque

def filter_inbounds(board, points):
    return [(i,j) for i,j in points if i < len(board) and j < len(board[0]) and i >= 0 and j >= 0]

def true(board, points):
    return points

def adjacent(board, i, j, a=None, b=None, filter=filter_inbounds):
    # allow for returning adjacencies relative to somewhere other than the point for part 2
    # where we want to double the size of the board
    if a == None:
        a = i
        b = j
    if board[a][b] == '.':
        return []
    if board[a][b] == '|':
        return filter(board, [(i-1, j), (i+1, j)])
    if board[a][b] == '-':
        return filter(board, [(i, j-1), (i, j+1)])
    if board[a][b] == 'L':
        return filter(board, [(i-1, j), (i, j+1)])
    if board[a][b] == 'J':
        return filter(board, [(i, j-1), (i-1, j)])
    if board[a][b] == '7':
        return filter(board, [(i+1, j), (i, j-1)])
    if board[a][b] == 'F':
        return filter(board, [(i, j+1), (i+1, j)])
    if board[a][b] == 'S':
        return [(x, y) for x, y in neighbors4(i, j, board) if (i, j) in adjacent(board, x, y)]
    raise NotImplementedError(f"WTF where are we {board[i][j], board, i, j}")

data = getlines("10")

for i, row in e(data):
    for j, c in e(row):
        if c == 'S':
            coord = (i,j)

def bfs1(board, i, j):
    found = set([(i, j)])
    queue = deque([(i, j)])
    while len(queue) > 0:
        i, j = queue.popleft()
        for neighbor in adjacent(board, i, j):
            if neighbor not in found and board[neighbor[0]][neighbor[1]] != '.':
                found.add(neighbor)
                queue.append(neighbor)
    return len(found), found

p1res, found = bfs1(data, *coord)
print(p1res // 2)

points = [(2 * i, 2 * j) for i, j in found]
newpoints = []

for bi, bj in points:
    si = bi // 2
    sj = bj // 2
    for neighbor in adjacent(data, bi, bj, si, sj, true):
        newpoints.append(neighbor)

allpoints = set(points + newpoints)
A,B = coord
starts = set([(2*A + 1, 2*B + 1), (2*A - 1, 2*B + 1), (2*A + 1, 2*B - 1), (2*A - 1, 2*B - 1)])
             
def bfs2(start, boundaryset, maxi, maxj):
    visited = set([start])
    queue = deque([start])
    while(len(queue) > 0):
        i, j = queue.popleft()
        for neighbor in neighbors4(i, j, maxi, maxj):
            if neighbor in boundaryset:
                continue
            if neighbor == (0,0):
                return 0
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return sum(1 for i, j in visited if i % 2 == 0 and j % 2 == 0)

for start in starts:
    print(start, bfs2(start, allpoints, len(data) * 2, len(data[0]) * 2))

from util import e, getlines, neighbors4
import sys

data = getlines("23")

# lol
sys.setrecursionlimit(1000000)

# NOTE: I preprocessed my input to put a solid row above the first one and below the last one, and tagged the destination as '*'

def dfs(graph, sofar, i, j):
    neighbors = None
    if graph[i][j] == '*':
        return len(sofar) - 1
    elif graph[i][j] != 'X':
        neighbors = neighbors4(i, j, graph)
    elif graph[i][j] == '>':
        neighbors = [(i, j + 1)]
    elif graph[i][j] == 'v':
        neighbors = [(i + 1, j)]
    elif graph[i][j] == '<':
        neighbors = [(i - 1, j)]
    else:
        neighbors = [(i, j - 1)]

    best = None
    for neighbor in neighbors:
        (x, y) = neighbor
        if neighbor in sofar or graph[x][y] == '#':
            continue
        sofar.add(neighbor)
        res = dfs(graph, sofar, x, y)
        if best is None or (res is not None and res > best):
            best = res
        sofar.remove(neighbor)
    return best

def make_adjacencies(graph):
    res = {}
    for i, row in e(graph):
        for j, c in e(row):
            if c != '#':
                adjacent = dict()
                for x, y in neighbors4(i, j, graph):
                    if graph[x][y] != '#':
                        adjacent[(x, y)] = 1
                res[(i, j)] = adjacent
    allkeys = list(res.keys())
    print(len(res))
    for key in allkeys:
        neighbors = res[key]
        if len(neighbors) == 2:
            left_neighbor, right_neighbor = neighbors.keys()
            del res[left_neighbor][key]
            del res[right_neighbor][key]
            res[left_neighbor][right_neighbor] = max(res[left_neighbor].get(right_neighbor, 0),  neighbors[left_neighbor] + neighbors[right_neighbor])
            res[right_neighbor][left_neighbor] = res[left_neighbor][right_neighbor]
            del res[key]
    print(len(res))
    return res

def dfs2(graph, sofar, current, target):
    if current == target:
        return sum(sofar.values())
    best = None
    for neighbor in graph[current]:
        if neighbor in sofar:
            continue
        sofar[neighbor] = graph[current][neighbor]
        res = dfs2(graph, sofar, neighbor, target)
        if best is None or (res is not None and res > best):
            best = res
        del sofar[neighbor]
    return best

print(dfs(data, set([(1,1)]), 1, 1))

graph = make_adjacencies(data)
print(dfs2(graph, {(1,1): 0}, (1,1), (len(data) - 2, len(data[0]) - 2)))
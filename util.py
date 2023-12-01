def getlines(day):
    with open(f"data/day{day}.txt") as f:
        return [line.strip() for line in f.readlines() if len(line) > 1]

def getblankseparated(day):
    with open(f"data/day{day}.txt") as f:
        return f.read().split("\n\n")

def tokenedlines(day):
    lines = getlines(day)
    ret = []
    for line in lines:
        parts = line.strip().split(' ')
        parsed_parts = []
        for part in parts:
            try:
                parsed_parts.append(int(part))
            except:
                try:
                    parsed_parts.append(float(part))
                except:
                    parsed_parts.append(part)
        ret.append(parsed_parts)
    return ret

def as_ints(arr):
    return tuple(int(x) for x in arr)

def in_range(i, j, max_i, max_j):
    return i >= 0 and j >= 0 and i < max_i and j < max_j

def neighbors4(i, j, max_i, max_j=None):
    return neighbors_helper(max_i, max_j, [(i-1, j), (i+1, j), (i, j-1), (i, j+1)])

def neighbors8(i, j, max_i, max_j=None):
    return neighbors_helper(max_i, max_j, [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)])

def neighbors_helper(max_i, max_j, candidates):
    if max_j is None and isinstance(max_i, list):
        max_j = len(max_i[0])
        max_i = len(max_i)
    return [(i, j) for i, j in candidates if in_range(i, j, max_i, max_j)]

def printgrid(points):
    maxX = max(p[0] for p in points)
    maxY = max(p[1] for p in points)
    for y in range(maxY + 1):
        for x in range(maxX + 1):
            if (x,y) in points:
                print('X', end='')
            else:
                print(' ', end='')
        print("")

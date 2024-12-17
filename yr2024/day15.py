from util import Tuple, getblankseparated, printgrid, printgrid2

day = "15"

gridchars, fishmoves = getblankseparated(day)

gridstrs = gridchars.split("\n")
grid = {}
grid2 = {}
for y, row in enumerate(gridstrs):
    for x, char in enumerate(row):
        grid[(x, y)] = char
        if char != 'O':
            grid2[(2 * x, y)] = char
            if char == '#':
                grid2[(2 * x + 1, y)] = char
            else:
                grid2[(2 * x + 1, y)] = '.'
        else:
            grid2[(2 * x, y)] = '['
            grid2[(2 * x + 1, y)] = ']'
        if char == '@':
            pos = (x, y)
            pos2 = (2 * x, y)
print(grid2)

fishmoves = fishmoves.replace("\n","")

DELTAS = {
    '^': (0, -1),
    '<': (-1, 0),
    'v': (0, 1),
    '>': (1, 0),
}



def push(src, dir, grid, dryrun=False):
    dst = Tuple.add(src, DELTAS[dir])
    if grid[dst] == '#':
        return False
    elif grid[dst] == '[' and dir in ('^', 'v'):
        other = Tuple.add(dst, DELTAS['>'])
        if push(dst, dir, grid, dryrun=True) and push(other, dir, grid, dryrun=True):
            if not dryrun:
                push(dst, dir, grid)
                if grid[other] != '.':
                    push(other, dir, grid)
                grid[dst] = grid[src]
                grid[src] = '.'
            return True
        else:
            return False
    elif grid[dst] == ']' and dir in ('^', 'v'):
        other = Tuple.add(dst, DELTAS['<'])
        if push(dst, dir, grid, dryrun=True) and push(other, dir, grid, dryrun=True):
            if not dryrun:
                push(dst, dir, grid)
                if grid[other] != '.':
                    push(other, dir, grid)
                grid[dst] = grid[src]
                grid[src] = '.'
            return True
        else:
            return False
    elif grid[dst] in 'O[]':
        if push(dst, dir, grid, dryrun):
            if not dryrun:
                grid[dst] = grid[src]
                grid[src] = '.'
            return True
        else:
            return False
    if grid[dst] == '.':
        if not dryrun:
            grid[dst] = grid[src]
            grid[src] = '.'
        return True
    print(f"WTF IS IT {grid[dst]=} {dst=}")
    return False

for dir in fishmoves:
    # printgrid2(grid2)
    if push(pos, dir, grid):
        pos = Tuple.add(pos, DELTAS[dir])
    if push(pos2, dir, grid2):
        pos2 = Tuple.add(pos2, DELTAS[dir])

ret = 0
for pos, char in grid.items():
    if char == 'O':
        ret += 100 * pos[1] + pos[0]
print(ret)

ret = 0
for pos, char in grid2.items():
    if char == '[':
        ret += 100 * pos[1] + pos[0]
printgrid2(grid2)
print(ret)
from collections import deque
from util import *

data = getlines("22")


def parse_line(line):
    start, end = line.split("~")
    a, b, c = tuple(int(p) for p in start.split(","))
    x, y, z = tuple(int(p) for p in end.split(","))

    def delta(i, j):
        if i == j:
            return 0
        elif i > j:
            return -1
        else:
            return 1

    points = [(a, b, c)]
    while (a, b, c) != (x, y, z):
        a += delta(a, x)
        b += delta(b, y)
        c += delta(c, z)
        points.append((a, b, c))
    return points


parsed_lines = [parse_line(line) for line in data]

blocks = {
    i: line for i, line in e(sorted(parsed_lines, key=lambda points: points[0][2]))
}
tile_to_block = {}
supported_by = defaultdict(set)
supports = defaultdict(set)

for i, block in blocks.items():
    for cube in block:
        tile_to_block[cube] = i


# def toposort(blocks, supported_by, supports)
#       supportcounts = {i: len(supported_by[i])}
#       ready = [i for i in supportcounts where supportcounts[i] == 0]
#       res = []
#       for i in ready:
#             res.


any_moved = True
while any_moved:
    supported_by = defaultdict(set)
    supports = defaultdict(set)
    touches_ground = set()
    ordering = range(len(blocks))  # todo sort more intelligently
    any_moved = False
    for block_index in ordering:
        block = blocks[block_index]
        if any(cube[2] == 0 for cube in block):
            touches_ground.add(block_index)
            continue
        dropped = [(x, y, z - 1) for x, y, z in block]
        can_move = True
        for cube in dropped:
            if cube in tile_to_block and tile_to_block[cube] != block_index:
                supported_by[block_index].add(tile_to_block[cube])
                supports[tile_to_block[cube]].add(block_index)
                can_move = False
        if can_move:
            any_moved = True
            for cube in block:
                del tile_to_block[cube]
            for cube in dropped:
                tile_to_block[cube] = block_index
            blocks[block_index] = dropped

res = 0
for block_index in blocks:
    valid = True
    for supported in supports[block_index]:
        if len(supported_by[supported]) == 1:
            valid = False
    if valid:
        res += 1
print(res)


def get_chaos(block_index, supported_by, supports, touches_ground):
    visited = set()
    queue = deque([block_index])
    while len(queue) > 0:
        curr = queue.popleft()
        visited.add(curr)
        for supported in supports[curr]:
            if supported in touches_ground or any(
                x not in visited for x in supported_by[supported]
            ):
                continue
            queue.append(supported)
    return len(visited) - 1


print(sum(get_chaos(i, supported_by, supports, touches_ground) for i in blocks))

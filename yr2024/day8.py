from math import gcd
from util import in_range, tokenedlines, getlines
from collections import defaultdict

day = "8"
# day = "ex"

data = getlines(day)

def get_antenna_groups():
    groups = defaultdict(list)
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c != '.':
                groups[c].append((x, y))
    return groups

def get_p1_antinodes(nodes, _ignored, _ignored2):
    antinodes = []
    for first in nodes:
        for second in nodes:
            if first != second:
                dx = second[0] - first[0]
                dy = second[1] - first[1]
                
                antinodes.append((second[0] + dx, second[1] + dy))
                antinodes.append((first[0] - dx, first[1] - dy))
    return antinodes

def get_p2_antinodes(nodes, max_x, max_y):
    antinodes = []
    for first in nodes:
        for second in nodes:
            if first != second:
                dx = second[0] - first[0]
                dy = second[1] - first[1]
                gcd = gcd2(dx, dy)
                dx //= gcd
                dy //= gcd
                x = first[0]
                y = first[1]
                while in_range(x, y, max_x, max_y):
                    antinodes.append((x, y))
                    x += dx
                    y += dy
                x = first[0]
                y = first[1]
                while in_range(x, y, max_x, max_y):
                    antinodes.append((x, y))
                    x -= dx
                    y -= dy
    return antinodes

def gcd2(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(a, b)

def get_all_antinodes(antinode_func, antenna_groups):
    all_antinodes = set()
    for group in antenna_groups:
        for node in antinode_func(group, len(data[0]), len(data)):
            if in_range(node[0], node[1], len(data[0]), len(data)):
                all_antinodes.add(node)
    return all_antinodes

groups = get_antenna_groups().values()
print(len(get_all_antinodes(get_p1_antinodes, groups)))
print(len(get_all_antinodes(get_p2_antinodes, groups)))

from math import gcd
from util import in_range, tokenedlines, getlines, Tuple
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

def get_p1_antinodes(nodes, _ignored):
    antinodes = []
    for first in nodes:
        for second in nodes:
            if first != second:
                delta = Tuple.add(second, Tuple.negate(first))
                antinodes.append(Tuple.add(second, delta))
                antinodes.append(Tuple.add(first, Tuple.negate(delta)))
    return antinodes

def get_p2_antinodes(nodes, data):
    antinodes = []
    for first in nodes:
        for second in nodes:
            if first != second:
                delta = Tuple.add(second, Tuple.negate(first))
                gcd = gcd2(*delta)
                delta = Tuple.idivide(delta, gcd)
                cur = first
                while Tuple.in_range(cur, data):
                    antinodes.append(cur)
                    cur = Tuple.add(cur, delta)
                
                cur = first
                delta = Tuple.negate(delta)
                while Tuple.in_range(cur, data):
                    antinodes.append(cur)
                    cur = Tuple.add(cur, delta)
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
        for node in antinode_func(group, data):
            if Tuple.in_range(node, data):
                all_antinodes.add(node)
    return all_antinodes

groups = get_antenna_groups().values()
print(len(get_all_antinodes(get_p1_antinodes, groups)))
print(len(get_all_antinodes(get_p2_antinodes, groups)))

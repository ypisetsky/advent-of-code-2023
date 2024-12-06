from util import printgrid, tokenedlines
from collections import defaultdict
from yr2019.intcode import get_all_output, Processor
import itertools

day = "11"

bytecode = tokenedlines(day, sep=",")[0]

colors = defaultdict(int)

proc = Processor(bytecode, [])

#dirs = ["UP", "RIGHT", "DOWN", "LEFT"]
deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = 0
x = 0
y = 0

while not proc.done():
    proc.feed_input([colors[(x, y)]])
    results = proc.consume_output()
    if len(results) == 2:
        colors[(x, y)] = results[0]
        dir += 3 if results[1] == 0 else 1
        dir %= 4
    x += deltas[dir][0]
    y += deltas[dir][1]

print(len(colors))

colors = defaultdict(int)
x = 0
y = 0
colors[(x, y)] = 1
proc = Processor(bytecode, [])
dir = 1
while not proc.done():
    proc.feed_input([colors[(x, y)]])
    results = proc.consume_output()
    if len(results) == 2:
        colors[(x, y)] = results[0]
        dir += 3 if results[1] == 0 else 1
        dir %= 4
    x += deltas[dir][0]
    y -= deltas[dir][1]

colored = [point for point, value in colors.items() if value == 1]
printgrid(colored)
from util import printgrid, printgrid2, tokenedlines
from collections import defaultdict
from yr2019.intcode import get_all_output, Processor
import itertools

day = "13"

bytecode = tokenedlines(day, sep=",")[0]

# proc = Processor(bytecode, [])
tiles = {}
output = get_all_output(bytecode, [])
for i in range(0, len(output), 3):
    tiles[(output[i], output[i+1])] = output[i+2]
print(len([t for t in tiles.values() if t == 2]))



def draw_grid(tiles):
    if (-1, 0) in tiles:
        print(f"SCORE: {tiles[(-1, 0)]}")
    printable_grid = {}
    for pos, value in tiles.items():
        if value == 0:
            continue
        elif value == 1:
            value = 'X'
        elif value == 2:
            value = '.'
        elif value == 3:
            value = '-'
        elif value == 4:
            value = 'B'
        printable_grid[pos] = value
    printgrid2(printable_grid)

bytecode[0] = 2
proc = Processor(bytecode, [])
tiles = {}
output = proc.consume_output()
for i in range(0, len(output), 3):
    tiles[(output[i], output[i+1])] = output[i+2]
draw_grid(tiles)

def find(tiles, value):
    for tile, val in tiles.items():
        if val == value:
            return tile

ball = find(tiles, 4)
paddle = find(tiles, 3)

for _ in range(100000):
    if paddle[0] == ball[0]:
        proc.feed_input([0])
    elif paddle[0] > ball[0]:
        proc.feed_input([-1])
    else:
        proc.feed_input([1])
    output = proc.consume_output()
    for i in range(0, len(output), 3):
        tiles[(output[i], output[i+1])] = output[i+2]
    ball = find(tiles, 4)
    paddle = find(tiles, 3)
    if find(tiles, 2) is None:
        print(tiles[(-1, 0)])
        break
    # draw_grid(tiles)
    
from util import tokenedlines

day = "3"
# day = "ex"

lines = tokenedlines(day, sep=",")

DELTAS = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

first_path = {}
x = 0
y = 0
i = 0
for token in lines[0]:
    first_path[(x, y)] = i
    for step in range(int(token[1:])):
        i += 1
        x += DELTAS[token[0]][0]
        y += DELTAS[token[0]][1]
        first_path[(x, y)] = i

best_crossing = 99999999999
fastest_crossing = 99999999999
x = 0
y = 0
i = 0
for token in lines[1]:
    for step in range(int(token[1:])):
        i += 1
        x += DELTAS[token[0]][0]
        y += DELTAS[token[0]][1]
        if (x,y) in first_path:
            print(x, y)
            if abs(x) + abs(y) < best_crossing:
                best_crossing = abs(x) + abs(y)
            if i + first_path[(x, y)] < fastest_crossing:
                fastest_crossing = i + first_path[(x, y)]

print(best_crossing, fastest_crossing)

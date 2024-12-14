from util import neighbors8, printgrid, tokenedlines, getlines, Tuple
from collections import defaultdict
import matplotlib.pyplot as plt

def get_position(p, v, t, w, h):
    result = Tuple.add(p, Tuple.multiply(v, t))
    return (result[0] % w, result[1] % h)

def parse_line(line):
    parts = line.split(' ')
    return parse_part(parts[0]), parse_part(parts[1])

def parse_part(part):
    if '=' not in part:
        print(f"{part=} BAD")
    part = part.split('=')[1]
    return tuple(int(x) for x in part.split(','))

day = "14"
robots = [parse_line(line) for line in getlines(day) if line != '']
# print(robots)

if day == "14":
    w = 101
    h = 103
else:
    w = 11
    h = 7


positions = [get_position(*robot, 100, w, h) for robot in robots]

counts = defaultdict(int)
skipx = w // 2
skipy = h // 2
for position in positions:
    if position[0] == skipx or position[1] == skipy:
        continue
    counts[(position[0] > skipx, position[1] > skipy )] += 1

ret = 1
for num in counts.values():
    ret *= num
print(ret)

def get_top_frames(robots, scorer):
    positions = [[get_position(*robot, t, w, h) for robot in robots] for t in range(w*h)]
    scores = [(t, scorer(positions[t])) for t in range(w * h)]
    scores.sort(key=lambda x: x[1])
    for t, score in scores[:10]:
        print(f"Time: {t} Score: {score}")
        printgrid(positions[t])
        input("Press enter")

    for t, score in scores[-10:]:
        print(f"Time: {t} Score: {score}")
        printgrid(positions[t])
        input("Press enter")


def count_alone(robots):
    alone_count = 0
    robots = set(robots)
    for robot in robots:
        for neighbor in neighbors8(*robot, w, h):
            if neighbor in robots:
                break
        else:
            alone_count += 1
    return alone_count

def count_unique(robots):
    return len(set(robots))

get_top_frames(robots, count_unique)
get_top_frames(robots, count_alone)


# Following is worthless code left in for fun
secs = 0
c = 0
frames = []
while c < 6000 and secs <= w * h:
    robots = [(get_position(*robot, secs, w, h), robot[1]) for robot in robots]
    secs += 1
    points = set([r[0] for r in robots])
    centered = 0
    for point in points:
        if (point[0]-1,point[1]+1) in points and (point[0]+1,point[1]-1) in points:
            centered += 1
    if centered > 10:
        print(f"{secs=} {centered}")
    if len([p for p in points if p[1] == 22]) > 70:
        print(f"{secs=}")
        # printgrid([r[0] for r in robots if 22 < r[0][1] < 54])
        fig, ax = plt.subplots()
        xs = [p[0] for p in points]
        ys = [-p[1] for p in points]

        ax.scatter(xs, ys)
        ax.set_title(f"{secs} seconds")

        fig.savefig(f"imgs/{c:04}.jpg")
        plt.close()
        c += 1
from util import *

data = tokenedlines("18")

# The last hexadecimal digit encodes the direction to dig: 0 means R, 1 means D, 2 means L, and 3 means U.
dirs = [
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
    (-1, 0),  # up
]


def solve(points):
    pointxy = defaultdict(list)
    for i, point in e(points):
        pointxy[point[0]].append(point[1])

    current_criticals = set()

    score = 0
    lastx = 0
    for x in sorted(pointxy.keys()):
        sorted_criticals = sorted(current_criticals)
        for i in range(0, len(sorted_criticals), 2):
            score += (x - lastx - 1) * (
                sorted_criticals[i + 1] - sorted_criticals[i] + 1
            )
        added_criticals = set()
        removed_criticals = set()
        for y in set(pointxy[x]):
            if y in current_criticals:
                removed_criticals.add(y)
            else:
                added_criticals.add(y)

        all_points = sorted(current_criticals.union(added_criticals))
        inbefore = False
        inafter = False
        lasty = 0
        next_criticals = current_criticals.union(added_criticals).difference(
            removed_criticals
        )
        for y in all_points:
            if inbefore or inafter:
                score += y - lasty
            if y in current_criticals:
                inbefore = not inbefore
            if y in next_criticals:
                inafter = not inafter
            if not inbefore and not inafter:
                score += 1
            lasty = y
        if inbefore or inafter:
            print(f"WTF failed {all_points}", x, sorted_criticals, next_criticals)
        current_criticals = next_criticals
        lastx = x
    return score


points = [(0, 0)]
curi = 0
curj = 0

for row in data:
    distance = row[1]
    dir = "RDLU".index(row[0])

    curi += distance * dirs[dir][0]
    curj += distance * dirs[dir][1]
    points.append((curi, curj))

print(solve(points))

points = [(0, 0)]
curi = 0
curj = 0

for row in data:
    distance = int(row[2][2:7], 16)
    dir = int(row[2][-2])

    # distance = row[1]
    # dir = 'RDLU'.index(row[0])

    curi += distance * dirs[dir][0]
    curj += distance * dirs[dir][1]
    points.append((curi, curj))

print(solve(points))

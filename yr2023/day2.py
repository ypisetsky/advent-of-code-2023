from util import tokenedlines

data = tokenedlines("2")


def to_trials(row):
    cursor = 2
    current_trial = {}
    trials = []
    while cursor < len(row):
        color = row[cursor + 1]
        end = False
        if color[-1] == ";":
            end = True
            color = color[:-1]
        elif color[-1] == ",":
            color = color[:-1]
        current_trial[color] = row[cursor]
        if end:
            trials.append(current_trial)
            current_trial = {}
        cursor += 2
    if current_trial != {}:
        trials.append(current_trial)
    return trials, int(row[1][:-1])


res = 0
for row in data:
    trials, id = to_trials(row)
    valid = True
    for x in trials:
        if x.get("red", 0) > 12:
            valid = False
        if x.get("green", 0) > 13:
            valid = False
        if x.get("blue", 0) > 14:
            valid = False
    if valid:
        res += id

print("Part 1", res)

res = 0
for row in data:
    trials, id = to_trials(row)
    minr = 0
    ming = 0
    minb = 0
    for x in trials:
        if x.get("red", 0) > minr:
            minr = x["red"]
        if x.get("green", 0) > ming:
            ming = x["green"]
        if x.get("blue", 0) > minb:
            minb = x["blue"]
    res += minr * ming * minb
print("Part 2", res)

from util import tokenedlines

day = "7"

data = tokenedlines(day)
res = 0

def checkline(line, part):
    target = int(line[0][:-1])
    previous = set([line[1]])

    for current in line[2:]:
        candidates = []
        for val in previous:
            candidates.append(val + current)
            candidates.append(val * current)
            if part == 2:
                candidates.append(int(f"{val}{current}"))
        previous = set()
        for candidate in candidates:
            if candidate <= target:
                previous.add(candidate)
    return target if target in previous else 0


print(sum([checkline(line, 1) for line in data]))
print(sum([checkline(line, 2) for line in data]))

from util import tokenedlines

day = "7"

data = tokenedlines(day)
res = 0

def checkline(line, part):
    target = int(line[0][:-1])
    candidates = [line[1]]

    for current in line[2:]:
        new_candidates = []
        for val in candidates:
            if val > target:
                continue
            new_candidates.append(val + current)
            new_candidates.append(val * current)
            if part == 2:
                new_candidates.append(int(f"{val}{current}"))
        candidates = new_candidates
    return target if target in candidates else 0


print(sum([checkline(line, 1) for line in data]))
print(sum([checkline(line, 2) for line in data]))

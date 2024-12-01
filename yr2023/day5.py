from util import getblankseparated

data = getblankseparated("5")
# data = getblankseparated("5s")

seeds = list(map(int, data[0].split()[1:]))
p2seeds = []
for i in range(0, len(seeds), 2):
    p2seeds.append((seeds[i], seeds[i + 1]))


# return the array index of the range which covers the given seed (or None if none do)
def find_range(seed, tokens):
    for i in range(0, len(tokens), 3):
        if seed in range(tokens[i + 1], tokens[i + 1] + tokens[i + 2]):
            return i
    return None


# Transforms a seed value assuming it's in the provided range
def transform(seed, range, tokens):
    if range is None:
        return seed
    else:
        return seed + tokens[range] - tokens[range + 1]


# Walk a step of the mapping for part 1
def convert(seeds, converter):
    tokens = list(map(int, converter.split()[2:]))
    newseeds = []
    for seed in seeds:
        newseeds.append(transform(seed, find_range(seed, tokens), tokens))
    return newseeds


# Finds the start of the next range after start
def findnext(rangestarts, start):
    # this should really be a binary search, but :shrug:
    for r in rangestarts:
        if r > start:
            return r
    return 98989898989898989898989898989


def convert2(seeds, converter):
    tokens = list(map(int, converter.split()[2:]))
    rangestarts = sorted(tokens[i] for i in range(1, len(tokens), 3))
    newseeds = []
    for start, size in seeds:
        while size > 0:
            rangeIndex = find_range(start, tokens)
            if rangeIndex is None:
                endrange = findnext(rangestarts, start)
            else:
                endrange = tokens[rangeIndex + 1] + tokens[rangeIndex + 2]
            step = min(endrange - start, size)
            newseeds.append((transform(start, rangeIndex, tokens), step))
            size -= step
            start += step
    return newseeds


for converter in data[1:]:
    seeds = convert(seeds, converter)

print(min(seeds))

for converter in data[1:]:
    p2seeds = convert2(p2seeds, converter)

print(min(p2seeds)[0])

from util import tokenedlines
from collections import defaultdict

day = "5"
# day = "ex"

data = tokenedlines(day, sep="|")
rules = defaultdict(set)
p1 = 0
p2 = 0

def sort_row(row, rules):
    res = []
    to_place = set(row)
    while len(to_place) > 0:
        for page in to_place:
            if rules[page].isdisjoint(to_place):
                res.append(page)
                to_place.remove(page)
                break
    res.reverse()
    return res

for row in data:
    if len(row) == 2:
        rules[row[0]].add(row[1])
    elif row != ['']:
        pages = [int(val) for val in row[0].split(',')]
        sorted = sort_row(pages, rules)
        if sorted == pages:
            p1 += sorted[len(pages) // 2]
        else:
            p2 += sorted[len(pages) // 2]


#print(rules)
print(p1)
print(p2)
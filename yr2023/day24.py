from util import *

data = getlines("24")

class Hailstone:
    def __init__(self, line):
        tokens = line.split()
        print(tokens)
        self.start = (
            int(tokens[0][:-1]),
            int(tokens[1][:-1]),
            int(tokens[2]),
        )
        self.velocity = (
            int(tokens[4][:-1]),
            int(tokens[5][:-1]),
            int(tokens[6]),
        )

    def past(self, x):
        if x <= self.start[0]:
            return self.velocity[0] > 0
        return self.velocity[0] < 0


hailstones = [Hailstone(line) for line in data]

def intersectxy(hailstone1, hailstone2):
    A = [
        [hailstone1.velocity[1], -hailstone1.velocity[0]],
        [hailstone2.velocity[1], -hailstone2.velocity[0]],
    ]
    b = [hailstone1.start[0] * hailstone1.velocity[1] - hailstone1.start[1] * hailstone1.velocity[0],
         hailstone2.start[0] * hailstone2.velocity[1] - hailstone2.start[1] * hailstone2.velocity[0]
         ]

    detA = A[0][0] * A[1][1] - A[1][0] * A[0][1]
    if detA == 0:
        return None
    Ainv = [
        [A[1][1] / detA, -A[0][1] / detA ],
        [-A[1][0] / detA, A[0][0] / detA]
    ]

    return tuple(Ainv[i][0] * b[0] + Ainv[i][1] * b[1] for i in range(2))
c = 0

for i, h1 in e(hailstones):
    for j in range(i + 1, len(hailstones)):
        res = intersectxy(h1, hailstones[j])
        if res is None:
            print(f"{h1} and {hailstones[j]} are parallel")
        elif h1.past(res[0]):
            print(f"In the past for A")
        elif hailstones[j].past(res[0]):
            print(f"In the past for B")
        elif res[0] >= 200000000000000 and res[0] <= 400000000000000 and res[1] >= 200000000000000 and res[1] <= 400000000000000:
            c += 1
            print(f"Intersect at {res}")
print(c)
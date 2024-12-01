from math import ceil, floor
from util import getlines, tokenedlines, e


data = tokenedlines("6")


def solve(n, x):
    # a * (n-a) >= X
    # 0 >= a^2 - an + X
    # zeroes are (n +- sqrt(n^2 - 4X) ) / 2

    highroot = (n + pow(n * n - 4 * x, 0.5)) / 2.0
    lowroot = (n - pow(n * n - 4 * x, 0.5)) / 2.0
    print(n, x, lowroot, highroot)
    return floor(highroot) - ceil(lowroot) + 1


ns = data[0][1:]
xs = data[1][1:]
res = 1
for i, n in e(ns):
    res *= solve(n, xs[i])
print(res)

data = getlines("6")
time = float(data[0].split(":")[1].replace(" ", ""))
dist = float(data[1].split(":")[1].replace(" ", ""))
print(solve(time, dist))

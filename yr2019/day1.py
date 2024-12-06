from util import getlines, tokenedlines

day = "1"
# day = "ex"

ret = 0
for row in getlines(day):
    fuel = int(row) // 3 - 2
    while fuel > 0:
        ret += fuel
        fuel = fuel // 3 - 2
print(ret)
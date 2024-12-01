from util import getlines, neighbors8, e

data = getlines("3")
# data = getlines("3s")


res = 0
for i, row in e(data):
    is_part = False
    val = 0
    for j, c in e(row + "."):
        if not c.isdigit():
            if is_part:
                res += val
                print(val)
            is_part = False
            val = 0
        else:
            val *= 10
            val += ord(c) - ord("0")
            if not is_part:
                for x, y in neighbors8(i, j, data):
                    if data[x][y] not in ".1234567890":
                        is_part = True
                        break
print(res)


def get_ratio(i, j, data):
    firstx = None
    firsty = None
    for x, y in neighbors8(i, j, data):
        if not data[x][y].isdigit():
            continue
        while data[x][y].isdigit() and y > 0:
            y -= 1
        if not data[x][y].isdigit():
            y += 1
        if firstx is None:
            firstx = x
            firsty = y
        elif firstx != x or firsty != y:
            v1 = 0
            while y < len(data[x]) and data[x][y].isdigit():
                v1 *= 10
                v1 += ord(data[x][y]) - ord("0")
                y += 1

            v2 = 0
            x = firstx
            y = firsty
            while data[x][y].isdigit():
                v2 *= 10
                v2 += ord(data[x][y]) - ord("0")
                y += 1
            print(i, j, v1, v2, v1 * v2)
            return v1 * v2
    return 0


res = 0
for i, row in e(data):
    for j, c in e(row):
        if c == "*":
            res += get_ratio(i, j, data)

print(res)

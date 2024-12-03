from util import getlines, tokenedlines

day = "2"
# day = "ex"

def is_safeish(level):
    return is_safe(level) or any(is_safe(level[:i] + level[i+1:]) for i in range(0, len(level)))

def is_safe(level):
    last = level[0]
    sign = None
    for i in range(1, len(level)):
        cur = level[i]
        if cur - last > 3:
            return False
        if cur - last < -3:
            return False
        if cur == last:
            return False
        if cur > last:
            if sign == "dec":
                return False
            else:
                sign = "inc"
        else:
            if sign == "inc":
                return False
            else:
                sign = "dec"
        last = cur
    return True

data = tokenedlines(day)
print(sum([1 for level in data if is_safe(level)]))
print(sum([1 for level in data if is_safeish(level)]))
        
from util import tokenedlines, getlines, neighbors8, in_range

day = 4
# day = "ex"

puzzle = getlines(day)

LETTERS = "XMAS"
def xmascount(data, i, j):
    if data[i][j] != LETTERS[0]:
        return 0
    res = 0
    for neighbor in neighbors8(i, j, data):
        valid = True
        x, y = neighbor
        dx = x - i
        dy = y - j
        for idx in range(1, 4):
            if not in_range(x, y, len(data), len(data[0])) or data[x][y] != LETTERS[idx]:
                valid = False
            x += dx
            y += dy
        if valid:
            res += 1
    return res

print(sum(xmascount(puzzle, i, j) for i in range(len(puzzle)) for j in range(len(puzzle[0]))))

def p2count(data, i, j):
    if data[i][j] != 'A':
        return 0
    if not in_range(i - 1, j - 1, len(data), len(data[0])):
        return 0
    if not in_range(i + 1, j + 1, len(data), len(data[0])):
        return 0
    
    tokens = [data[i-1][j-1], data[i-1][j+1], data[i+1][j-1], data[i+1][j+1]]
    return 1 if "".join(tokens) in ["MMSS", "MSMS", "SSMM", "SMSM"] else 0

print(sum(p2count(puzzle, i, j) for i in range(len(puzzle)) for j in range(len(puzzle[0]))))

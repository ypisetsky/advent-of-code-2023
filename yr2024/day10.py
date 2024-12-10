from util import getlines, neighbors4, tokenedlines

day = "10"

data = getlines(day)

memo_p2 = {}
def get_num_trails(row, col, grid):
    if (row, col) in memo_p2:
        return memo_p2[(row, col)]
    my_height = int(grid[row][col])
    if my_height == 9:
        return 1
    score = 0
    for r, c in neighbors4(row, col, grid):
        if int(grid[r][c]) == my_height + 1:
            score += get_num_trails(r, c, grid)
    memo_p2[(row, col)] = score
    return score

memo_p1 = {}
def get_visitable_peaks(row, col, grid):
    if (row, col) in memo_p1:
        return memo_p1[(row, col)]
    my_height = int(grid[row][col])
    if my_height == 9:
        return set([(row, col)])
    visitable = set([])
    for r, c in neighbors4(row, col, grid):
        if int(grid[r][c]) == my_height + 1:
            visitable.update(get_visitable_peaks(r, c, grid))
    memo_p1[(row, col)] = visitable
    return visitable


print(sum([len(get_visitable_peaks(row, col, data)) 
           for row in range(len(data)) 
           for col in range(len(data[0]))
           if data[row][col] == '0']))
print(sum([get_num_trails(row, col, data)
           for row in range(len(data)) 
           for col in range(len(data[0])) 
           if data[row][col] == '0']))
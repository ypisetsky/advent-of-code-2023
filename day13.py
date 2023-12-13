from util import getblankseparated
from collections import defaultdict

data = getblankseparated("13")
#data = getblankseparated("13s")

def distance(x, y):
      return sum(1 for i in range(len(x)) if x[i] != y[i])

def getsplit(grid, targetdistance):
      for i in range(1, len(grid)):
            editdistance = 0
            for j in range(i):
                  left = i - 1 - j
                  right = i + j
                  if left >= 0 and right < len(grid):
                        editdistance += distance(grid[left], grid[right])
            if editdistance == targetdistance:
                  return i
      return 0

def solve(case, targetdistance):
      lines = case.split("\n")
      grid = defaultdict(dict)
      tgrid = defaultdict(dict)
      rows = len(lines)
      cols = len(lines[0])
      for i, line in enumerate(lines):
            for j, c in enumerate(line):
                  grid[i][j] = c
                  tgrid[j][i] = c
      rowsplit = getsplit(grid, targetdistance)
      colsplit = getsplit(tgrid, targetdistance)
      if rowsplit * colsplit != 0 or rowsplit + colsplit == 0:
            print("FAILED " + case)
      return 100 * rowsplit + colsplit

print(sum(solve(case, 0) for case in data))
print(sum(solve(case, 1) for case in data))

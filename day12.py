from util import tokenedlines

data = tokenedlines("12")
# data = tokenedlines("12s")


def getcount(memo, line, counts, pos, current_count, countpos):
      # pos is the next character to be processed
      # current_count is how far into the current sequence of #s we are in
      # countpos is how many sequences of #s we have already finished
      key = (pos, current_count, countpos)
      # print(key)
      if key in memo:
            return memo[key]
      if pos == len(line):
            ret = 1 if len(counts) == countpos else 0
      elif line[pos] == '#':
            ret = getcount(memo, line, counts, pos + 1, current_count + 1, countpos)
      elif line[pos] == '.' or countpos == len(counts):
            if countpos < len(counts) and current_count == counts[countpos]:
                  ret = getcount(memo, line, counts, pos + 1, 0, countpos + 1)
            elif current_count == 0:
                  ret = getcount(memo, line, counts, pos + 1, 0, countpos)
            else:
                  ret = 0
      else:
            hash_count = getcount(memo, line, counts, pos + 1, current_count + 1, countpos)
            dot_count = 0
            if current_count == counts[countpos]:
                  dot_count = getcount(memo, line, counts, pos + 1, 0, countpos + 1)
            elif current_count == 0:
                  dot_count = getcount(memo, line, counts, pos + 1, 0, countpos)
            ret = hash_count + dot_count
      memo[key] = ret
      # print(key, ret)
      return ret

res = 0
for row in data:
      counts = [int(x) for x in row[1].split(',')]
      res += getcount({}, row[0] + '.', counts, 0, 0, 0)
print(res)

res = 0
for row in data:
      counts = [int(x) for x in row[1].split(',')] * 5
      res += getcount({}, (row[0] + '?') * 4 + row[0] + '.', counts, 0, 0, 0)
print(res)

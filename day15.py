"""
    Determine the ASCII code for the current character of the string.
    Increase the current value by the ASCII code you just determined.
    Set the current value to itself multiplied by 17.
    Set the current value to the remainder of dividing itself by 256.
"""


from util import *

data = getlines("15")
parts = data[0].split(",")

def step(cur, c):
      if c == '\n':
            return cur
      return ((cur + ord(c)) * 17) % 256


def hash(s):
      x = 0
      for c in s:
            x = step(x, c)
      return x

print(sum(hash(s) for s in parts))

boxes = [[] for i in range(256)]
focal_lengths = {}

for s in parts:
      if s[-1] == '-':
            label = s[:-1]
            h = hash(label)
            if label in boxes[h]:
                  boxes[h].remove(label)
      else:
            label, fl = s.split("=")
            focal_lengths[label] = int(fl)
            h = hash(label)
            if label not in boxes[h]:
                  boxes[h].append(label)
res = 0
for i, lenses in enumerate(boxes):
      res += (i + 1) * sum((j + 1) * focal_lengths[lens] for j, lens in enumerate(lenses))
print(res)

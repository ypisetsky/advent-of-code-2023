from util import getlines, lcm

data = getlines("8")

instructions = data[0]
ilen = len(instructions)

adjacencies = {}
for row in data:
      adjacencies[row[:3]] = (row[7:10], row[12:15])


current = 'AAA'
icursor = 0
res = 0
while current != 'ZZZ':
      if instructions[icursor] == 'L':
            current = adjacencies[current][0]
      else:
            current = adjacencies[current][1]
      icursor = (icursor + 1) % ilen
      res += 1
print(res)


def getcycleinfo(current):
      visited = {}
      icursor = 0
      step = 0
      while (current, icursor) not in visited:
            visited[(current, icursor)] = step
            if instructions[icursor] == 'L':
                  current = adjacencies[current][0]
            else:
                  current = adjacencies[current][1]
            icursor = (icursor + 1) % ilen
            step += 1
      return visited[(current, icursor)], step - visited[(current, icursor)], current, {x:y for x,y in visited.items() if x[0][2] == 'Z'}



cycle_lengths = []
for row in data:
      x = row[:3]
      if x[2] == 'A':
            cycle_lengths.append(getcycleinfo(x)[1])

print(lcm(cycle_lengths))

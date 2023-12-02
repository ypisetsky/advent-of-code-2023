from util import getlines

data = getlines("2")

def parse_trial(trial: str):
      colors = [x.split(" ") for x in trial.split(", ")]
      return {c[1]: int(c[0]) for c in colors}

def to_trials(row: str):
      header,data = row.split(": ")
      return [parse_trial(trial) for trial in data.split("; ")], int(header[5:])

res = 0
for row in data:
      trials,id = to_trials(row)
      valid = True
      for x in trials:
            if x.get('red', 0) > 12:
                  valid = False
            if x.get('green', 0) > 13:
                  valid = False
            if x.get('blue', 0) > 14:
                  valid = False
      if valid:
            res += id

print("Part 1",res)

res = 0
for row in data:
      trials,id = to_trials(row)
      minr = 0
      ming = 0
      minb = 0
      for x in trials:
            if x.get('red', 0) > minr:
                  minr = x['red']
            if x.get('green', 0) > ming:
                  ming = x['green']
            if x.get('blue', 0) > minb:
                  minb = x['blue']
      res += minr * ming * minb
print("Part 2",res)

from util import getlines

data = getlines("1")

res = 0
NUMS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
# uncomment for part 1
# NUMS = []
for line in data:
    nums = []
    for i in range(len(line)):
        if line[i].isnumeric():
            nums.append(ord(line[i]) - ord("0"))
        for n in range(len(NUMS)):
            if line[i:].startswith(NUMS[n]):
                nums.append(n + 1)
    res += nums[0] * 10 + nums[-1]

print(res)

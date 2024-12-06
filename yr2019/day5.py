from util import tokenedlines
from collections import defaultdict
from yr2019.intcode import execute_one_inst

day = "5"


bytecode = tokenedlines(day, sep=",")[0]

memory = defaultdict(int)
for i, v in enumerate(bytecode):
    memory[i] = v

ip = 0
output = []
while ip is not None:
    ip = execute_one_inst(ip, memory, [5], output)

print(output)
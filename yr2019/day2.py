from util import getlines, tokenedlines
from collections import defaultdict
from yr2019.intcode import execute_one_inst

day = "2"
# day = "ex"

memory = defaultdict(int)


bytecode = tokenedlines(day, sep=",")[0]
bytecode[1] = 49
bytecode[2] = 0
memory = defaultdict(int)
for i, v in enumerate(bytecode):
    memory[i] = v

for i in range(0, len(bytecode) - 4, 4):
    if bytecode[i+1] % 4 == 3 and bytecode[i+1] != i - 1:
        print("Weird memory access!")
    if bytecode[i+2] % 4 == 3 and bytecode[i+2] != i - 1:
        print("Weird memory access!")
    if bytecode[i+3] % 4 != 3:
        print("Weird write!")
    if bytecode[i+3] >= i+4:
        print("Modify future!")
    print(i, bytecode[i:i+4])
ip = 0
while ip is not None:
    ip = execute_one_inst(ip, memory)

print(memory)
from util import tokenedlines
from collections import defaultdict
from yr2019.intcode import get_all_output, Processor
import itertools

day = "9"
# day = "ex"

bytecode = tokenedlines(day, sep=",")[0]

print(get_all_output(bytecode, [1]))
print(get_all_output(bytecode, [2]))
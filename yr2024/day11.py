from util import getlines, tokenedlines
import functools
from math import log10, pow

day = "11"

@functools.cache
def num_stones(stone, generations):
    if generations == 0:
        return 1
    if stone == 0:
        return num_stones(1, generations - 1)
    num_digits = int(log10(stone)) + 1
    if num_digits % 2 == 0:
        return num_stones(stone // pow(10, num_digits // 2), generations - 1) + \
            num_stones(stone % pow(10, num_digits // 2), generations - 1)
    else:
        return num_stones(stone * 2024, generations - 1)
    
stones = tokenedlines(day)[0]
print(sum([num_stones(stone, 25) for stone in stones]))
print(sum([num_stones(stone, 75) for stone in stones]))
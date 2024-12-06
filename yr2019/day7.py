from util import tokenedlines
from collections import defaultdict
from yr2019.intcode import get_all_output, Processor
import itertools

day = "7"


bytecode = tokenedlines(day, sep=",")[0]

def run_amplifier_chain(settings, input):
    for amplifier in settings:
        input = get_all_output(bytecode, [amplifier, input])[0]
    return input

best_score = 0
for chain in itertools.permutations(range(5)):
    score = run_amplifier_chain(chain, 0)
    if score > best_score:
        best_score = score



print(best_score)


def run_amplifier_loop(settings):
    amplifiers = [Processor(bytecode, [amplifier]) for amplifier in settings]
    input = [0]
    while not all(amp.done() for amp in amplifiers):
        for amplifier in amplifiers:
            amplifier.feed_input(input)
            input = amplifier.consume_output()
    return input[0]

for chain in itertools.permutations(range(5, 10)):
    score = run_amplifier_loop(chain)
    if score > best_score:
        best_score = score

print(best_score)
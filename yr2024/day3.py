from util import getlines, tokenedlines
import re

day = "3"
# day = "ex"

data = getlines(day)

mul_regex = r'(?:(mul)\((\d+),(\d+)\))|(?:(do)\(\))|(?:(don\'t)\(\))'

def get_score(line):
    all_matches = re.findall(mul_regex, line)
    res = 0
    on = True
    for match in all_matches:
        print(match)
        if match[3] == "do":
            on = True
        elif match[4] == "don't":
            on = False
        elif on:
            res += int(match[1]) * int(match[2])
    return res

print(get_score("".join(data)))
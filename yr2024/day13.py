from util import Tuple, lcm, tokenedlines, getlines

day = "13"
# day = "ex"

data = getlines(day)
puzzles = []
def get_button(row, delim1, delim2):
    first_plus = row.index(delim1)
    row = row[first_plus+1:]
    return tuple(int(n) for n in row.split(delim2))

for i in range(0, len(data), 3):
    a = get_button(data[i], '+', ', Y+')
    b = get_button(data[i+1], '+', ', Y+')
    prize = get_button(data[i+2], '=', ', Y=')
    puzzles.append((a, b, prize))


def get_best_score(a, b, prize, delta):
    prize = Tuple.add(prize, delta)
    determinant = a[0] * b[1] - (b[0] * a[1])
    if determinant == 0:
        print(f"Sorry {a} {b} {prize}")
        return 0
    matrix_parts = Tuple.multiply([b[1], -a[1], -b[0], a[0]], 1/determinant)
    num_a = int(matrix_parts[0] * prize[0] + matrix_parts[2] * prize[1] + .01)
    num_b = int(matrix_parts[1] * prize[0] + matrix_parts[3] * prize[1] + .01)
    if num_a < 0 or num_b < 0:
        return 0
    if num_a * a[0] + num_b * b[0] != prize[0]:
        return 0
    if num_a * a[1] + num_b * b[1] != prize[1]:
        return 0
    return 3 * int(num_a) + int(num_b)

def part1(puzzles):
    return sum([get_best_score(*puzzle, [0, 0]) for puzzle in puzzles])

def part2(puzzles):
    return sum([get_best_score(*puzzle, [10000000000000, 10000000000000]) for puzzle in puzzles])


print(part1(puzzles))
print(part2(puzzles))

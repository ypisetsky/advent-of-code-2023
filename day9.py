from util import tokenedlines


def is_same(seq):
    return min(seq) == max(seq)


def extrapolate(seq, right):
    if is_same(seq):
        return seq[0]
    else:
        deltas = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
        next_delta = extrapolate(deltas, right)
        if right:
            return seq[-1] + next_delta
        else:
            return seq[0] - next_delta


data = tokenedlines("9")
print(sum(extrapolate(line, True) for line in data))
print(sum(extrapolate(line, False) for line in data))

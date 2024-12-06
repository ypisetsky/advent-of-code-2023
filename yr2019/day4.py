

memo = {}

def get_count(digits, had_idle=False, prev_digit=0):
    digits = tuple(digits)
    if (digits, had_idle, prev_digit) in memo:
        return memo[(digits, had_idle, prev_digit)]
    if len(digits) == 1:
        return 10 - digits[0] if had_idle else 1
    
    ret = 0
    if digits[1] < digits[0]:
        new_digits = digits[0:1] * (len(digits) - 1)
        ret += get_count(new_digits, had_idle or digits[0] == prev_digit, digits[0])
    else:
        ret += get_count(digits[1:], had_idle or digits[0] == prev_digit, digits[0])

    for num in range(digits[0] + 1, 10):
        ret += get_count([num] * (len(digits) - 1), had_idle, num)

    memo[(digits, had_idle, prev_digit)] = ret
    return ret

memo2 = {}
def get_count2(digits, had_idle=False, prev_digit = 0, streak = 0):
    digits = tuple(digits)
    if (digits, had_idle, prev_digit, streak) in memo2:
        return memo2[(digits, had_idle, prev_digit, streak)]
    if len(digits) == 1:
        if had_idle:
            ret = 10 - digits[0]
        elif streak == 2:
            ret = 9 - digits[0]
        elif streak == 1 and prev_digit >= digits[0]:
            ret = 1
        else:
            ret = 0
        
        memo2[(digits, had_idle, prev_digit, streak)] = ret
        return ret
        
    break_streak = digits[0] != prev_digit
    ret = get_count2(digits[1:], had_idle or (break_streak and streak == 2), digits[0], 1 if break_streak else (streak + 1))

    for num in range(digits[0] + 1, 10):
        ret += get_count2([num] * (len(digits) - 1), had_idle or streak == 2, num, 1)

    memo2[(digits, had_idle, prev_digit, streak)] = ret
    return ret


print(get_count((2,6,6,6,6,6)) - get_count((8,8,8,8,8,8)))
print(get_count2((2,6,6,6,6,6)) - get_count2((8,8,8,8,8,8)))
from util import Tuple, tokenedlines, getlines

day = "17"

lines = getlines(day)
def getdata(line):
    return line.split(": ")[1]
a = int(getdata(lines[0]))
b = int(getdata(lines[1]))
c = int(getdata(lines[2]))
program = [int(x) for x in getdata(lines[3]).split(",")]

def combo(a, b, c, value):
    if value < 4:
        return value
    if value == 4:
        return a
    if value == 5:
        return b
    if value == 6:
        return c
    # print("Attempting to parse combo {value}")
    return None

def eval(a, b, c, ip, program):
    opcode = program[ip]
    arg = program[ip+1]
    comb = combo(a, b, c, arg)
    # print(f"Running {opcode} with arg {arg:o} (combo {comb:o}) with state {a:o},{b:o},{c:o},{ip}")
    if opcode == 0:
        num = a
        denom = pow(2, comb)
        return (None, num // denom, b, c, ip + 2)
    elif opcode == 1:
        return (None, a, b ^ arg, c, ip + 2)
    elif opcode == 2:
        return (None, a, comb % 8, c, ip + 2)
    elif opcode == 3:
        if a == 0:
            return (None, a, b, c, ip + 2)
        else:
            return (None, a, b, c, arg)
    elif opcode == 4:
        return (None, a, b ^ c, c, ip + 2)
    elif opcode == 5:
        return (comb % 8, a, b, c, ip + 2)
    elif opcode == 6:
        num = a
        denom = pow(2, comb)
        return (None, a, num // denom, c, ip + 2)
    elif opcode == 7:
        num = a
        denom = pow(2, comb)
        return (None, a, b, num // denom, ip + 2)

def run_program(a, b, c, program):
    ip = 0
    res = []
    while ip < len(program) - 1:
        (out, a, b, c, ip) = eval(a, b, c, ip, program)
        if out is not None:
            res.append(out)
    return res

def get_best_quine_input(program, cursor, sofar):
    for candidate in range(8):
        if run_program(sofar * 8 + candidate, 0, 0, program) == program[cursor:]:
            if cursor == 0:
                return sofar * 8 + candidate
            ret = get_best_quine_input(program, cursor - 1, sofar * 8 + candidate)
            if ret is not None:
                return ret
    return None

print(",".join([str(x) for x in run_program(a, b, c, program)]))
print(get_best_quine_input(program, len(program) - 1, 0))
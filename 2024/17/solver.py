import math

registers, program = open(0).read().split("\n\n")

register_a, _, _ = [int(register[12:]) for register in registers.split("\n")]
program = list(map(int, program[8:].split(",")))


def combo(opcode, register_a, register_b, register_c):
    match opcode:
        case literal if literal in [0, 1, 2, 3]:
            return literal
        case 4:
            return register_a
        case 5:
            return register_b
        case 6:
            return register_c
        case _:
            raise Exception("unsupported operand")


def run(register_a, program):
    instruction_ptr = 0
    register_b = register_c = 0
    output = []

    while instruction_ptr < len(program):
        op = program[instruction_ptr]
        operand = program[instruction_ptr + 1]
        combo_op = combo(operand, register_a, register_b, register_c)

        match op:
            # adv
            case 0:
                register_a >>= combo_op
            # bxl
            case 1:
                register_b ^= operand
            # bst
            case 2:
                register_b = combo_op % 8
            # jnz
            case 3 if register_a != 0:
                instruction_ptr = operand
                continue
            # bxc
            case 4:
                register_b ^= register_c
            # out
            case 5:
                output.append(combo_op % 8)
            # bdv
            case 6:
                register_b = register_a >> combo_op
            # cdv
            case 7:
                register_c = register_a >> combo_op

        instruction_ptr += 2

    return output


# Part 1

print(",".join(map(str, run(register_a, program))))


# Part 2

a = [0] * len(program)
q = [(a, 0)]
res = math.inf

while q:
    (a, i) = q.pop()

    dec = int("".join(map(str, a)), 8)
    curr = run(dec, program)

    if i >= len(program):
        if curr == program:
            res = dec
            break

    if curr[::-1][:i] != program[::-1][:i]:
        continue

    for j in range(7, -1, -1):
        q.append((a[:i] + [j] + a[i + 1 :], i + 1))

print(res)

import os
import inspect

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "input.txt"), "r") as f:
    ops = [
        (d, int(a), c[2:-1])
        for d, a, c in [line.split() for line in f.read().splitlines()]
    ]


def get_pos(direction):
    match direction:
        case "R":
            return 1
        case "L":
            return -1
        case "U":
            return -1j
        case "D":
            return 1j


def get_lava_amount(p1, d, a):
    p2 = p1 + get_pos(d) * a

    area = 0

    # shoelace formula
    area += p1.real * p2.imag
    area -= p2.real * p1.imag

    # make sure we include the outline
    area += a

    return area


# part 1

curr_pos = 0
res = 0

for d, a, _ in ops:
    res += get_lava_amount(curr_pos, d, a)
    curr_pos += get_pos(d) * a

print(int(res / 2) + 1)

# part 2

curr_pos = 0
res = 0

for _, _, h in ops:
    d, a = h[-1].translate(str.maketrans("0123", "RDLU")), int(h[:-1], 16)

    res += get_lava_amount(curr_pos, d, a)
    curr_pos += get_pos(d) * a

print(int(res / 2) + 1)

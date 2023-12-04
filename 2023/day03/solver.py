import collections
import inspect
import math
import os

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "example.txt"), "r") as f:
    lines = f.read().splitlines()


def get_neighbours(x, y, lst):
    return [
        n
        for n in [
            (x, y - 1),
            (x, y + 1),
            (x - 1, y),
            (x - 1, y - 1),
            (x - 1, y + 1),
            (x + 1, y),
            (x + 1, y - 1),
            (x + 1, y + 1),
        ]
        if n[0] >= 0 and n[1] >= 0 and n[0] < len(lst[0]) - 1 and n[1] < len(lst) - 1
    ]


res = 0
gears = collections.defaultdict(list)

for y, line in enumerate(lines):
    x_s = x_e = None
    num = ""

    for x, char in enumerate(line):
        if char.isdigit():
            if x_s is None:
                x_s = x

            x_e = x

            num += char

        if char.isdigit() and x != len(line) - 1 or not num:
            continue

        n_1 = get_neighbours(x_s, y, lines)
        n_2 = get_neighbours(x_e, y, lines) if len(num) > 1 else []

        for x_n, y_n in n_1 + n_2:
            n = lines[y_n][x_n]

            if n not in ".0123456789":
                res += int(num)

                if n == "*":
                    gears[(x_n, y_n)].append(int(num))

                break

        x_s = x_e = None
        num = ""

# part 1

print(res)

# part 2

print(sum(math.prod(gear) for gear in gears.values() if len(gear) == 2))

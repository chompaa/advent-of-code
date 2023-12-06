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


# part 1

res = 0

for y, line in enumerate(lines):
    x_e = None
    num = ""

    for x, char in enumerate(line):
        if char.isdigit():
            x_e = x
            num += char

            if x != len(line) - 1:
                continue

        if not num:
            continue

        n_1 = get_neighbours(x_e - (len(num) - 1), y, lines)
        n_2 = get_neighbours(x_e, y, lines) if len(num) > 1 else []

        for x_n, y_n in n_1 + n_2:
            if lines[y_n][x_n] not in ".0123456789":
                res += int(num)
                break

        x_e = None
        num = ""

print(res)

# part 2

res = collections.defaultdict(list)

for y, line in enumerate(lines):
    x_e = None
    num = ""

    for x, char in enumerate(line):
        if char.isdigit():
            x_e = x
            num += char

            if x != len(line) - 1:
                continue

        if not num:
            continue

        n_1 = get_neighbours(x_e - (len(num) - 1), y, lines)
        n_2 = get_neighbours(x_e, y, lines) if len(num) > 1 else []

        for x_n, y_n in n_1 + n_2:
            if lines[y_n][x_n] == "*":
                res[(x_n, y_n)].append(int(num))
                break

        x_e = None
        num = ""


print(sum(math.prod(res) for res in res.values() if len(res) == 2))

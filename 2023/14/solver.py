import collections
import inspect
import os

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "example.txt"), "r") as f:
    lines = [list(line) for line in f.read().splitlines()]


def rotate(lines):
    return [list(x) for x in zip(*lines[::-1])]


def move(lines):
    for line in lines:
        moved = True

        while moved:
            moved = False

            for i in range(len(line) - 1):
                if line[i] == "O" and line[i + 1] == ".":
                    line[i], line[i + 1] = line[i + 1], line[i]
                    moved = True

    return lines


def check(lines):
    return sum(i + 1 for line in lines for i, c in enumerate(line) if c == "O")


# part 1

print(check(move(rotate(lines.copy()))))

# part 2

res = 0
seen = []
current_cycle = 0

while 1:
    for _ in range(4):
        lines = move(rotate(lines))

    if lines in seen:
        start = seen.index(lines)
        length = current_cycle - start
        res = seen[start + (1_000_000_000 - start) % length - 1]
        break

    seen.append(lines)
    current_cycle += 1

print(check(rotate(res)))

import inspect
import itertools
import os

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "example.txt"), "r") as f:
    mirrors = [line.splitlines() for line in f.read().split("\n\n")]


def get_reflection_lines(mirror, smudges=0):
    for row in list(itertools.pairwise(range(len(mirror)))):
        amount = min(abs(0 - row[0]), abs(len(mirror) - row[1] - 1))

        smudge_count = sum(
            sum(s != r for s, r in zip(mirror[src], mirror[row[0] + row[1] - src]))
            for src in range(row[0] - amount, row[1])
        )

        if smudge_count == smudges:
            return row


def get_reflection_sum(mirror, smudges=0):
    mirror_t = list(zip(*mirror))

    row_reflect = get_reflection_lines(mirror, smudges=smudges)
    col_reflect = get_reflection_lines(mirror_t, smudges=smudges)

    if row_reflect:
        return row_reflect[1] * 100
    if col_reflect:
        return col_reflect[1]


# part 1

print(sum(get_reflection_sum(mirror) for mirror in mirrors))

# part 2

print(sum(get_reflection_sum(mirror, smudges=1) for mirror in mirrors))

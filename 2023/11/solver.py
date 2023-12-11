import os
import inspect
import itertools

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "example.txt"), "r") as f:
    space = [list(line) for line in f.read().splitlines()]


def parse_space(space, offset):
    row_pad = 0
    col_exp = set(range(len(space[0])))
    galaxies = []

    for y, row in enumerate(space):
        empty = True

        for x, col in enumerate(row):
            if col == "#":
                galaxies.append([x, y + (row_pad * offset)])

                if x in col_exp:
                    col_exp.remove(x)

                empty = False

        if empty:
            row_pad += 1

    for galaxy in galaxies:
        x = galaxy[0]

        for col in col_exp:
            if col < galaxy[0]:
                x += offset

        galaxy[0] = x

    return galaxies


def get_shortest_path_sum(galaxies):
    return sum(
        abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
        for g1, g2 in itertools.combinations(galaxies, 2)
        if g1 != g2
    )


# part 1

print(get_shortest_path_sum(parse_space(space, 2 - 1)))

# part 2

print(get_shortest_path_sum(parse_space(space, 100_000_000 - 1)))

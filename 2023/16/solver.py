import os
import inspect

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "example.txt"), "r") as f:
    tiles = {
        complex(i, j): col
        for j, row in enumerate(f)
        for i, col in enumerate(row.strip())
    }


def get_directions(tile, d):
    match tile:
        case "/":
            return (-1j / d,)
        case "\\":
            return (1j / d,)
        case "|":
            return (1j, -1j)
        case "-":
            return (1, -1)
        case _:
            return (d,)


def get_energized_count(p, d, tiles):
    energized = set()
    q = [(p, d)]

    while q:
        p, d = q.pop()

        if ((p, d)) in energized:
            continue

        energized.add((p, d))
        q.extend((p + d, d) for d in get_directions(tiles.get(p), d) if p + d in tiles)

    return len({p for p, _ in energized})


# part 1

print(get_energized_count(0, 1, tiles))

# part 2

print(
    max(
        get_energized_count(p, d, tiles)
        for p in tiles
        for d in (1, 1j, -1, -1j)
        if p - d not in tiles
    )
)

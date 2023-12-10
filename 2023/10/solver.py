import inspect
import os

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
grid = []
start = 0

with open(os.path.join(cwd, "input.txt"), "r") as f:
    for y, row in enumerate(f.read().splitlines()):
        grid.append([".", *list(row), "."])

        if "S" in row:
            start = (row.index("S") + 1, y + 1)

    grid.insert(0, ["."] * len(grid[0]))
    grid.append(["."] * len(grid[0]))


def get_tile(grid, x, y):
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
        return None

    return grid[y][x]


def get_tiles(grid, positions):
    return [get_tile(grid, *tile) for tile in positions]


def get_neighbors(x, y, diagonal=False):
    diagonals = (
        (
            (x + 1, y + 1),
            (x - 1, y - 1),
            (x + 1, y - 1),
            (x - 1, y + 1),
        )
        if diagonal
        else ()
    )

    return (
        (x + 1, y),
        (x - 1, y),
        (x, y - 1),
        (x, y + 1),
    ) + diagonals


def get_connections(x, y):
    pipe = get_tile(grid, x, y)
    e, w, n, s = get_neighbors(x, y)
    east_tile, west_tile, north_tile, south_tile = get_tiles(grid, [e, w, n, s])

    match pipe:
        case "-":
            if east_tile in "-J7":
                yield e
            if west_tile in "-FL":
                yield w
        case "|":
            if north_tile in "|F7":
                yield n
            if south_tile in "|LJ":
                yield s
        case "F":
            if east_tile in "-7J":
                yield e
            if south_tile in "|LJ":
                yield s
        case "7":
            if west_tile in "-FL":
                yield w
            if south_tile in "|JL":
                yield s
        case "L":
            if north_tile in "|F7":
                yield n
            if east_tile in "-J7":
                yield e
        case "J":
            if north_tile in "|7F":
                yield n
            if west_tile in "-LF":
                yield w
        case "S":
            if east_tile in "-7J":
                yield e
            if west_tile in "-LF":
                yield w
            if north_tile in "|F7":
                yield n
            if south_tile in "|LJ":
                yield s


def get_distances(start):
    distances = [["_" for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited = set()
    queue = [(start, 0)]

    while queue:
        (x, y), dist = queue.pop(0)

        if (x, y) in visited:
            continue

        distances[y][x] = dist

        visited.add((x, y))

        queue.extend(
            (connection, dist + 1)
            for connection in get_connections(x, y)
            if connection not in visited
        )

    return distances


# part 1

print(max(col for row in get_distances(start) for col in row if isinstance(col, int)))

# part 2

# replace unreachable pipes with normal tiles
distances = [
    ["." if col == "_" else grid[y][x] for x, col in enumerate(row)]
    for y, row in enumerate(get_distances(start))
]


# add paths between every tile
paths = ["*" for _ in range(len(grid[0]) * 2 - 1)]

for row in distances:
    for i in range(1, len(row) * 2 - 1, 2):
        row.insert(i, paths[0])

for i in range(1, len(grid) * 2 - 1, 2):
    distances.insert(i, paths)

visited = set()
# start from the top-left
queue = [(0, 0)]

# flood fill
while queue:
    (x, y) = queue.pop(0)

    if (x, y) in visited:
        continue

    visited.add((x, y))

    if get_tile(distances, x, y) == ".":
        distances[y][x] = "O"

    for nx, ny in get_neighbors(x, y, diagonal=True):
        tile = get_tile(distances, nx, ny)

        match tile:
            case ".":
                queue.append((nx, ny))
            case "*":
                # check if we can leak through this tile
                e, w, n, s = get_tiles(distances, get_neighbors(nx, ny))

                if (e not in ["-", "J", "7"] and w not in ["-", "F", "L"]) and (
                    s not in ["|", "L", "J"] and n not in ["|", "F", "7"]
                ):
                    queue.append((nx, ny))
            case _:
                continue


# count leaks
print(sum(row.count(".") for row in distances))

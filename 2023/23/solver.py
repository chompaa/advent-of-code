import collections
import inspect
import os

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "example.txt"), "r") as f:
    trails = {
        complex(x, y): char
        for y, line in enumerate(f.readlines())
        for x, char in enumerate(line.strip())
    }

WALL = "#"
EMPTY = "."

start = next(pos for pos, char in trails.items() if char == EMPTY)
end = max(trails, key=lambda x: abs(x.real) + abs(x.imag) if trails[x] == EMPTY else 0)

points = [start, end]

for pos in trails:
    if trails[pos] == WALL:
        continue

    neighbors = sum(
        pos + neighbor in trails and trails[pos + neighbor] != WALL
        for neighbor in (1, -1, 1j, -1j)
    )

    if neighbors >= 3:
        points.append(pos)


graph = {pos: {} for pos in points}


def make_verticies(graph, neighbors, trails=trails):
    for pos in points:
        stack = [(0, pos)]
        visited = {pos}

        while stack:
            dist, c_pos = stack.pop()

            if dist != 0 and c_pos in points:
                graph[pos][c_pos] = dist
                continue

            for neighbor in neighbors[trails[c_pos]]:
                n_pos = c_pos + neighbor

                if n_pos in trails and trails[n_pos] != WALL and n_pos not in visited:
                    stack.append((dist + 1, n_pos))
                    visited.add(n_pos)

    return graph


def find_longest_path(graph, start, end):
    seen = set()

    def dfs(point):
        if point == end:
            return 0

        res = -float("inf")

        seen.add(point)

        for n in graph[point]:
            if n not in seen:
                res = max(res, dfs(n) + graph[point][n])

        seen.remove(point)

        return res

    return dfs(start)


# part 1

print(
    find_longest_path(
        make_verticies(
            graph,
            {
                "^": (-1j,),
                ">": (1,),
                "v": (1j,),
                "<": (-1,),
                ".": (1, -1, 1j, -1j),
            },
        ),
        start,
        end,
    )
)

# part 2

print(
    find_longest_path(
        make_verticies(graph, collections.defaultdict(lambda: (1, -1, 1j, -1j))),
        start,
        end,
    )
)

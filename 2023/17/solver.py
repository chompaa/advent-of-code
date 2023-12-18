import heapq
import inspect
import os

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "example.txt"), "r") as f:
    grid = {
        complex(i, j): int(col)
        for j, row in enumerate(f)
        for i, col in enumerate(row.strip())
    }


def dijkstra(min, max, grid=grid, start=0, end=[*grid][-1], c=0):
    q = [(0, 0, start, 1)]
    visited = set()

    while q:
        heat, _, pos, p_dir = heapq.heappop(q)

        if pos == end:
            return heat

        if (pos, p_dir) in visited:
            continue

        visited.add((pos, p_dir))

        for n_dir in (1j / p_dir, -1j / p_dir):
            n_heat = heat + sum(grid.get(pos + n_dir * amt, 0) for amt in range(1, min))

            for amt in range(min, max + 1):
                n_pos = pos + (n_dir * amt)

                if n_pos not in grid:
                    continue

                n_heat += grid[n_pos]

                heapq.heappush(q, (n_heat, c := c + 1, n_pos, n_dir))

    return None


# part 1

print(dijkstra(1, 3))

# part 2

print(dijkstra(4, 10))

lines = open(0).read().splitlines()
plots = {(y, x): lines[x][y] for x in range(len(lines[0])) for y in range(len(lines))}

N = ((0, 1), (0, -1), (-1, 0), (1, 0))


def dfs(start):
    q = [start]
    seen = set()

    while q:
        p = q.pop()
        px, py = p

        if p in seen:
            continue

        seen.add(p)

        for nx, ny in N:
            n = (px + nx, py + ny)
            if n in plots and plots[p] == plots[n]:
                q.append(n)

    return seen


# Part 1

q = set(plots.keys())
res = 0

while q:
    start = next(iter(q))
    region = dfs(start)
    q -= region
    edges = []

    for px, py in region:
        for nx, ny in N:
            n = (px + nx, py + ny)
            if n not in region:
                edges.append((n, (nx, ny)))

    price = len(edges) * len(region)
    res += price

print(res)

# Part 2

q = set(plots.keys())
res = 0

while q:
    start = next(iter(q))
    region = dfs(start)
    q -= region
    edges = []

    for px, py in region:
        for nx, ny in N:
            n = (px + nx, py + ny)
            if n not in region:
                edges.append((n, (nx, ny)))

    edge_count = 0
    while edges:
        (ex, ey), (dx, dy) = edges.pop()
        for nx, ny in N:
            i = 1
            while ((ex + nx * i, ey + ny * i), (dx, dy)) in edges:
                edges.remove(((ex + nx * i, ey + ny * i), (dx, dy)))
                i += 1
        edge_count += 1

    price = edge_count * len(region)
    res += price

print(res)

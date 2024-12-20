import heapq

w = h = 70
start = (0, 0)
end = (w, h)

b = [tuple(map(int, line.split(","))) for line in open(0).read().splitlines()]


def dfs(start, end, b):
    memory = {
        (x, y): "#" if (x, y) in b else "." for y in range(h + 1) for x in range(w + 1)
    }
    q = [(0, start)]
    seen = set()

    while q:
        dist, curr = heapq.heappop(q)

        if curr == end:
            return dist

        if curr in seen:
            continue
        seen.add(curr)

        cx, cy = curr
        for nx, ny in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            n = (cx + nx, cy + ny)
            if n in memory and memory[n] != "#":
                heapq.heappush(q, (dist + 1, n))

    return -1


# Part 1

print(dfs(start, end, b[:1024]))

# Part 2

l, r = 1024, len(b)
while l + 1 < r:
    m = (l + r) // 2
    dist = dfs(start, end, b[:m])
    if dist == -1:
        r = m
    else:
        l = m

res = map(str, b[r - 1])
print(",".join(res))

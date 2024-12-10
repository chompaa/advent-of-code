lines = open(0).read().splitlines()

m = {(x, y): int(lines[x][y]) for x in range(len(lines)) for y in range(len(lines[0]))}
trail_heads = set(h for h, s in m.items() if s == 0)

# Part 1

res = 0

for h in trail_heads:
    q = [h]
    s = set()
    while q:
        c = q.pop()
        cx, cy = c
        if c in s:
            continue
        s.add(c)
        if m[c] == 9:
            res += 1
        for nx, ny in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            n = (cx + nx, cy + ny)
            if n in m and m[n] - m[c] == 1:
                q.append(n)

print(res)

# Part 2

res = 0

for h in trail_heads:
    q = [h]
    while q:
        c = q.pop()
        cx, cy = c
        if m[c] == 9:
            res += 1
        for nx, ny in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            n = (cx + nx, cy + ny)
            if n in m and m[n] - m[c] == 1:
                q.append(n)

print(res)

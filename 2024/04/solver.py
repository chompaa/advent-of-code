lines = open(0).read().splitlines()

W = len(lines[0])
H = len(lines)

grid = {(x, y): lines[x][y] for x in range(W) for y in range(H)}

# Part 1

pattern = "XMAS"

cols = ["" for _ in range(W)]
rows = ["" for _ in range(H)]
f_diag = ["" for _ in range(H + W - 1)]
b_diag = ["" for _ in range(len(f_diag))]

for y in range(H):
    for x in range(W):
        cols[x] += lines[x][y]
        rows[y] += lines[x][y]
        f_diag[y + x] += lines[x][y]
        b_diag[y - x - H + 1] += lines[x][y]

res = 0

for lines in [cols, rows, f_diag, b_diag]:
    for row in lines:
        if len(row) < len(pattern):
            continue
        res += row.count(pattern)
        res += row[::-1].count(pattern)

print(res)

# Part 2

combs = [
    [
        "M.S",
        ".A.",
        "M.S",
    ],
    [
        "M.M",
        ".A.",
        "S.S",
    ],
    [
        "S.M",
        ".A.",
        "S.M",
    ],
    [
        "S.S",
        ".A.",
        "M.M",
    ],
]


def valid(c, x, y):
    for j in range(3):
        for i in range(3):
            if c[i][j] != "." and grid.get((x - 1 + i, y - 1 + j), "") != c[i][j]:
                return False
    return True


res = 0

for x, y in grid:
    if grid.get((x, y)) != "A":
        continue

    for c in combs:
        if valid(c, x, y):
            res += 1

print(res)

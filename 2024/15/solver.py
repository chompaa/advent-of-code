import copy

warehouse, moves = open(0).read().split("\n\n")
warehouse = warehouse.splitlines()
moves = moves.replace("\n", "")

w = {
    (y, x): warehouse[x][y]
    for x in range(len(warehouse))
    for y in range(len(warehouse[0]))
}

move_map = {
    "<": (-1, 0),
    ">": (1, 0),
    "v": (0, 1),
    "^": (0, -1),
}

robot = next(pos for pos, tile in w.items() if tile == "@")

# Part 1

for move in moves:
    rx, ry = robot
    dx, dy = move_map[move]
    next_robot = (rx + dx, ry + dy)
    n = w[(rx + dx, ry + dy)]

    if n == ".":
        w[robot], w[next_robot] = ".", "@"
        rx, ry = rx + dx, ry + dy
    elif n == "O":
        cx = rx + 2 * dx
        cy = ry + 2 * dy
        while w[(cx, cy)] not in ".#":
            cx, cy = cx + dx, cy + dy
        if w[(cx, cy)] == ".":
            w[robot], w[next_robot] = ".", "@"
            rx, ry = rx + dx, ry + dy
            w[(cx, cy)] = "O"

    robot = (rx, ry)

print(sum(100 * py + px for (px, py), tile in w.items() if tile == "O"))

# Part 2


def crates(warehouse, robot, dir):
    crates = set()
    cx, cy = robot
    ch, (dx, dy) = dir

    if ch in "<>":
        nx, ny = cx + dx, cy
        while warehouse[(nx, ny)] in "[]":
            crates.add((nx, ny))
            nx += dx
    else:
        lx, ly = -dy, dx
        rx, ry = dy, dx
        if dy == -1:
            lx, ly, rx, ry = rx, ry, lx, ly

        fx, fy = cx + dx, cy + dy
        q = [(fx, fy)]

        if warehouse[(fx, fy)] == "[":
            q.append((fx + rx, fy + ry))
        else:
            q.append((fx + lx, fy + ly))

        seen = set()
        while q:
            p = q.pop(0)
            px, py = p

            if (px, py) not in warehouse or (px, py) in seen:
                continue
            seen.add((px, py))

            if warehouse[p] in "[]":
                crates.add(p)

            fwd = (px + dx, py + dy)
            fx, fy = fwd

            if fwd not in warehouse or warehouse[fwd] not in "[]":
                continue

            q.append(fwd)
            if warehouse[fwd] == "]":
                q.append((fx + lx, fy + ly))
            else:
                q.append((fx + rx, fy + ry))

    return crates


w = [
    line.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
    for line in warehouse
]
w = {(y, x): w[x][y] for x in range(len(w)) for y in range(len(w[0]))}

robot = next(pos for pos, tile in w.items() if tile == "@")

for move in moves:
    rx, ry = robot

    dx, dy = move_map[move]
    nrx, nry = rx + dx, ry + dy

    adj = w[(nrx, nry)]

    if adj in "[]":
        c = crates(w, robot, (move, (dx, dy)))

        for cx, cy in c:
            n = (cx + dx, cy + dy)
            if n in w and w[n] == "#":
                break
        else:
            next_w = copy.copy(w)
            changed = set()

            for cx, cy in c:
                n = (cx + dx, cy + dy)
                next_w[n] = w[(cx, cy)]
                changed.add(n)

            for cx, cy in c - changed:
                next_w[(cx, cy)] = "."

            next_w[robot] = "."
            robot = (nrx, nry)
            next_w[robot] = "@"

            w = next_w
    elif adj != "#":
        w[robot] = "."
        robot = (nrx, nry)
        w[robot] = "."


res = 0
for (px, py), tile in w.items():
    if tile != "[":
        continue

    res += 100 * py + px

print(res)

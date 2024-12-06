import copy

lines = open(0).read().splitlines()
m = {(y, x): line[y] for x, line in enumerate(lines) for y in range(len(line))}

start = next(pos for pos, tile in m.items() if tile == "^")


def next(guard, dir):
    return (guard[0] + dir[0], guard[1] + dir[1])


def prev(guard, dir):
    return (guard[0] - dir[0], guard[1] - dir[1])


dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# Part 1

dir = 0
guard = start
seen = set()

while guard in m:
    while guard in m and m[guard] != "#":
        guard = next(guard, dirs[dir])
        seen.add(guard)

    seen.remove(guard)

    if guard in m and m[guard] == "#":
        guard = prev(guard, dirs[dir])
        dir = (dir + 1) % 4

print(len(seen))

# Part 2


def is_loop(guard, m):
    dir = 0
    seen = set([(guard, dir)])
    guard = start
    looping = False

    while guard in m and not looping:
        while guard in m and m[guard] != "#":
            guard = next(guard, dirs[dir])
            if (guard, dir) in seen:
                looping = True
                break
            seen.add((guard, dir))
        seen.remove((guard, dir))

        if guard in m and m[guard] == "#":
            guard = prev(guard, dirs[dir])
            dir = (dir + 1) % 4

    return looping


res = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if m[(x, y)] in ["^", "#"] or (x, y) not in seen:
            continue

        m_copy = copy.copy(m)
        m_copy[(x, y)] = "#"

        if is_loop(guard, m_copy):
            res += 1


print(res)

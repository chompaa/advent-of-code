import itertools

lines = open(0).read().splitlines()
freqs = {(y, x): lines[x][y] for y in range(len(lines[0])) for x in range(len(lines))}
antennas = set([pos for pos, antenna in freqs.items() if antenna != "."])

# Part 1

antinodes = set()

for (x1, y1), (x2, y2) in itertools.combinations(antennas, 2):
    if freqs[(x1, y1)] != freqs[(x2, y2)]:
        continue

    dx, dy = x2 - x1, y2 - y1

    x0 = (x1 - dx, y1 - dy)
    if x0 in freqs:
        antinodes.add(x0)

    x3 = (x2 + dx, y2 + dy)
    if x3 in freqs:
        antinodes.add(x3)


print(len(antinodes))

# Part 2

antinodes = set()

for (x1, y1), (x2, y2) in itertools.combinations(antennas, 2):
    if freqs[(x1, y1)] != freqs[(x2, y2)]:
        continue

    dx, dy = x2 - x1, y2 - y1

    xi, yi = x1, y1
    while (xi, yi) in freqs:
        antinodes.add((xi, yi))
        xi, yi = xi - dx, yi - dy

    xi, yi = x2, y2
    while (xi, yi) in freqs:
        antinodes.add((xi, yi))
        xi, yi = xi + dx, yi + dy


print(len(antinodes))

import itertools

lines = open(0).read().splitlines()
freqs = {(y, x): lines[x][y] for y in range(len(lines[0])) for x in range(len(lines))}
antennas = set([pos for pos, antenna in freqs.items() if antenna != "."])

# Part 1

antinodes = set()

for (x1, y1), (x2, y2) in itertools.permutations(antennas, 2):
    if freqs[(x1, y1)] != freqs[(x2, y2)]:
        continue

    dx, dy = x2 - x1, y2 - y1

    xi = (x2 + dx, y2 + dy)
    if xi in freqs:
        antinodes.add(xi)


print(len(antinodes))

# Part 2

antinodes = set()

for (x1, y1), (x2, y2) in itertools.permutations(antennas, 2):
    if freqs[(x1, y1)] != freqs[(x2, y2)]:
        continue

    dx, dy = x2 - x1, y2 - y1

    xi, yi = x2, y2
    while (xi, yi) in freqs:
        antinodes.add((xi, yi))
        xi, yi = xi + dx, yi + dy


print(len(antinodes))

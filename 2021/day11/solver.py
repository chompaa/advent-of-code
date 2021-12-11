with open("example.txt") as f:
  cavern = [[int(col) for col in row] for row in f.read().splitlines()]

cavern_dict = {}

for row_idx, row in enumerate(cavern):
  for col_idx, col in enumerate(row):
    cavern_dict[(row_idx, col_idx)] = col

length = len(cavern)


def get_neighbours(x, y):
  neighbours = []

  for i in range(x - 1, x + 2):
    for j in range(y - 1, y + 2):
      if i == x and j == y:
        continue

      if i >= 0 and i < length and j >= 0 and j < length:
        neighbours.append((i, j))

  return neighbours


# part 1

flashes = 0
cavern = cavern_dict.copy()

for step in range(100):
  flashing = True
  flashed = []

  while flashing:

    for (x, y) in cavern:
      if (x, y) not in flashed and cavern[(x, y)] >= 9:
        flashed.append((x, y))
        flashes += 1

        for neighbour in get_neighbours(x, y):
          cavern[neighbour] += 1

        break
    else:
      flashing = False

  cavern = {k: cavern[k] + 1 for k in cavern}

  for flash in flashed:
    cavern[flash] = 0

print(flashes)

# part 2

stop = False
cavern = cavern_dict.copy()

for step in range(1000):
  if stop:
    break

  flashing = True
  flashed = []

  while flashing:

    for (x, y) in cavern:
      if (x, y) not in flashed and cavern[(x, y)] >= 9:
        flashed.append((x, y))

        if len(flashed) == len(cavern.keys()):
          stop = True

        for neighbour in get_neighbours(x, y):
          cavern[neighbour] += 1

        break
    else:
      flashing = False

  cavern = {k: cavern[k] + 1 for k in cavern}

  for flash in flashed:
    cavern[flash] = 0

print(step)

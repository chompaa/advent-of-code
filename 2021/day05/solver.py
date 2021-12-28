from os.path import dirname, join
from itertools import chain

with open(join(dirname(__file__), "example.txt"), "r") as f:
  lines = [line.strip().split(" -> ") for line in f.readlines()]

lines = [[node.split(",") for node in line] for line in lines]
lines = [[tuple(map(int, node)) for node in line] for line in lines]

max_x = 0
max_y = 0

for line in lines:
  for node in line:
    if node[0] > max_x:
      max_x = node[0]
    if node[1] > max_y:
      max_y = node[1]

grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

# part 1

# remove x1 != x2 and y1 != y2 entries
_lines = list(filter(lambda x: x[0][0] == x[1]
              [0] or x[0][1] == x[1][1], lines))

for line in _lines:
  x1, y1 = line[0][0], line[0][1]
  x2, y2 = line[1][0], line[1][1]

  if x1 == x2:
    for y in range(min(y1, y2), max(y1, y2) + 1):
      grid[y][x1] += 1
  elif y1 == y2:
    for x in range(min(x1, x2), max(x1, x2) + 1):
      grid[y1][x] += 1

print(sum(i > 1 for i in list(chain.from_iterable(grid))))

# part 2

# remove x1 == x2 and y1 == y2 entries
_lines = list(filter(lambda x: x[0][0] != x[1]
              [0] and x[0][1] != x[1][1], lines))

# remove non 45 degree angle entries
_lines = list(
    filter(
        lambda x: abs((x[0][1] - x[1][1]) / (x[0][0] - x[1][0])) ==
        1, _lines))

for line in _lines:
  x1, x2 = line[0][0], line[1][0]
  y1, y2 = line[0][1], line[1][1]

  while True:
    grid[y1][x1] += 1

    if x1 == x2:
      break

    x1 += 1 if x1 < x2 else -1
    y1 += 1 if y1 < y2 else -1


print(sum(i > 1 for i in list(chain.from_iterable(grid))))

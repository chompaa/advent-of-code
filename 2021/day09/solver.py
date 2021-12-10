with open("input.txt", "r") as f:
  grid = [
      list(filter(lambda x: x != "\n", [line for line in lines]))
      for lines in f.readlines()]
  grid = [list(map(int, val)) for val in grid]

# part 1


def check_neighbours(grid, x, y):
  directions = [
      (x - 1, y),
      (x + 1, y),
      (x, y - 1),
      (x, y + 1),
  ]

  for i, j in directions:
    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
      if grid[i][j] < grid[x][y]:
        return False

  return True


risk_values = []

for i in range(len(grid)):
  for j in range(len(grid[0])):
    if check_neighbours(grid, i, j):
      risk_values.append(grid[i][j] + 1)

print(sum(risk_values))

# part 2

basins = {}
idx = 0

for i in range(len(grid)):
  for j in range(len(grid[0])):
    if check_neighbours(grid, i, j):
      basins[idx] = [i, j]
      idx += 1


def get_neighbours(grid, x, y):
  points = []

  directions = [
      (x - 1, y),
      (x + 1, y),
      (x, y - 1),
      (x, y + 1),
  ]

  for i, j in directions:
    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
      if grid[i][j] != 9:
        points.append([i, j])

  return points


def get_basin(grid, px, py):
  pts = []

  def get_points(x, y):
    neighbours = get_neighbours(grid, x, y)

    if not neighbours:
      return

    for point in neighbours:
      if point not in pts:
        pts.append(point)
        get_points(point[0], point[1])

  get_points(px, py)
  return pts


basins = {idx: get_basin(grid, low[0], low[1]) for idx, low in basins.items()}
len_basins = sorted([len(basin) for basin in basins.values()])

product = 1
for length in len_basins[-3:]:
  product *= length

print(product)

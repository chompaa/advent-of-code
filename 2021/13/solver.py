from os.path import dirname, join
from copy import deepcopy

with open(join(dirname(__file__), "example.txt"), "r") as f:
  lines = [line.strip() for line in f.readlines()]

coords = [list(map(int, line.split(","))) for line in lines if "," in line]
folds = [line.replace("fold along ", "") for line in lines if "=" in line]


def fold(coords, folds):
  for coord in coords:
    for f in folds:
      idx = 0 if f[0] == "x" else 1
      line = int(f[2:])

      if coord[idx] > line:
        coord[idx] = - coord[idx]

        while coord[idx] < 0:
          coord[idx] = coord[idx] % line


# part 1

_coords = deepcopy(coords)

fold(_coords, [folds[0]])

print(len(set([tuple(coord) for coord in _coords])))

# part 2

_coords = deepcopy(coords)

fold(_coords, folds)

max_x = max(_coords, key=lambda x: x[0])[0]
max_y = max(_coords, key=lambda x: x[1])[1]

for y in range(max_y + 1):
  for x in range(max_x + 1):
    if [x, y] in _coords:
      print("#", end="")
    else:
      print(" ", end="")
  print("")

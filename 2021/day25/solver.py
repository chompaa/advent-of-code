from os.path import join, dirname
from itertools import count

with open(join(dirname(__file__), "input.txt")) as f:
  lines = f.read().splitlines()

east = set()
south = set()

for i, row in enumerate(lines):
  for j, col in enumerate(row):
    if col == ".":
      continue
    match col:
      case ".":
        pass
      case ">":
        east.add((i, j))
      case "v":
        south.add((i, j))


for n in count():
  new_east = set()

  for c in east:
    evolve = c[0], (c[1] + 1) % len(lines[0])
    if evolve not in east and evolve not in south:
      new_east.add(evolve)
    else:
      new_east.add(c)

  new_south = set()

  for c in south:
    evolve = (c[0] + 1) % len(lines), c[1]
    if evolve not in new_east and evolve not in south:
      new_south.add(evolve)
    else:
      new_south.add(c)

  if new_east == east and new_south == south:
    n += 1
    break

  east = new_east
  south = new_south


# part 1

print(n)

from os.path import dirname, join

with open(join(dirname(__file__), "example.txt"), "r") as f:
  dirs = [(l.split()[0], int(l.split()[1])) for l in f.read().splitlines()]

# part 1

pos = 0
depth = 0

for dir, val in dirs:
  match dir:
    case "forward":
      pos += val
    case "up":
      depth -= val
    case "down":
      depth += val

print(pos * depth)

# part 2

pos = 0
depth = 0
aim = 0

for dir, val in dirs:
  match dir:
    case "forward":
      pos += val
      depth += aim * val
    case "up":
      aim -= val
    case "down":
      aim += val

print(pos * depth)

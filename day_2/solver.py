with open("input.txt", "r") as f:
  dirs = [line.strip().split(' ') for line in f.readlines()]
  dirs = [(dir, int(val)) for [dir, val] in dirs]

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

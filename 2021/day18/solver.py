import re
from math import ceil
from ast import literal_eval

with open("example.txt") as f:
  lines = f.read().splitlines()

pair_re = re.compile(r"\[(\d+),(\d+)\]")
lb_re = re.compile(r"\d+(?!.*\d)")
rb_re = re.compile(r"\d+")


def explode(line):
  for pair in pair_re.finditer(line):
    open = line[:pair.start()]

    if open.count("[") - open.count("]") >= 4:
      start = lb_re.sub(
          lambda x: str(int(x[0]) + int(pair[1])),
          line[:pair.start()],
          count=1
      )

      end = rb_re.sub(
          lambda x: str(int(x[0]) + int(pair[2])),
          line[pair.end():],
          count=1
      )

      return f"{start}0{end}"
  return None


split_re = re.compile(r"\d\d+")


def split(line):
  match = split_re.search(line)

  if match:
    return split_re.sub(
        lambda x: f"[{int(x[0]) // 2},{ceil(int(x[0]) / 2)}]",
        line,
        count=1
    )

  return None


def reduce(line):
  reducable = True

  while reducable:
    e_line = explode(line)
    if e_line:
      line = e_line
      continue

    s_line = split(line)
    if s_line:
      line = s_line
    else:
      reducable = False

  return line


def add(l1, l2):
  return f"[{l1},{l2}]"


def magnitude_sum(line_sum):
  def magnitude(value):
    if isinstance(value, int):
      return value
    else:
      return 3 * magnitude(value[0]) + 2 * magnitude(value[1])

  return magnitude(literal_eval(line_sum))


# part 1

line_sum = lines[0]

for idx in range(1, len(lines)):
  line_sum = reduce(add(line_sum, lines[idx]))

print(magnitude_sum(line_sum))

# part 2

max_magnitude = 0

for main_line in lines:
  for other_line in lines:
    if main_line == other_line:
      continue

    # addition is not commutative! must check both ways
    max_magnitude = max(
        magnitude_sum(reduce(add(main_line, other_line))),
        max_magnitude
    )
    max_magnitude = max(
        magnitude_sum(reduce(add(other_line, main_line))),
        max_magnitude
    )

print(max_magnitude)

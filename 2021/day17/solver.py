with open("input.txt") as f:
  line = f.readlines()[0][13:].split(", ")

ax_0, ax_1 = list(map(int, line[0][2:].split("..")))
ay_0, ay_1 = list(map(int, line[1][2:].split("..")))


def sim(vx_0, vy_0):
  x = y = y_max = 0
  vx, vy = vx_0, vy_0

  while y > ay_0 and x < ax_1:
    x += vx
    y += vy
    y_max = max(y, y_max)

    if vx > 0:
      vx -= 1
    elif vx < 0:
      vx += 1
    vy -= 1

    if ax_0 <= x <= ax_1 and ay_0 <= y <= ay_1:
      return True, y_max

  return False, None


hits = set()
y_max = 0

for vx in range(ax_1 + 1):
  for vy in range(ay_0, -ay_0 + 1):
    hit, apex = sim(vx, vy)
    if hit:
      hits.add((vx, vy))
      y_max = max(y_max, apex)


# part 1

print(y_max)

# part 2

print(len(hits))

import copy
import math

data = [line.split() for line in open(0).read().splitlines()]

W = 101
H = 103

bathroom = {(x, y): 0 for x in range(W) for y in range(H)}
robots = []

for p, v in data:
    px, py = map(int, p[2:].split(","))
    vx, vy = map(int, v[2:].split(","))
    robots.append(((px, py), (vx, vy)))
    bathroom[(px, py)] += 1


def step(robots, bathroom):
    res = []
    for p, v in robots:
        px, py = p
        vx, vy = v

        bathroom[p] -= 1
        px, py = (px + vx) % W, (py + vy) % H

        bathroom[(px, py)] += 1
        res.append(((px, py), v))
    return res


# Part 1


def simulate(robots, bathroom):
    robots = copy.copy(robots)
    bathroom = copy.copy(bathroom)

    for _ in range(100):
        robots = step(robots, bathroom)

    return bathroom


q = [0, 0, 0, 0]

for (x, y), count in simulate(robots, bathroom).items():
    if x < W // 2 and y < H // 2:
        q[0] += count
    elif x > W // 2 and y < H // 2:
        q[1] += count
    elif x > W // 2 and y > H // 2:
        q[2] += count
    elif x < W // 2 and y > H // 2:
        q[3] += count

print(math.prod(q))

# Part 2

for i in range(W * H):
    robots = step(robots, bathroom)
    if max(bathroom.values()) == 1:
        print(i)

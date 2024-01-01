import dataclasses
import inspect
import itertools
import os

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "input.txt"), "r") as f:
    hailstones = [line.split(" @ ") for line in f.read().splitlines()]


@dataclasses.dataclass
class Vector3:
    x: int
    y: int
    z: int

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):
        return Vector3(self.x / other, self.y / other, self.z / other)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    @staticmethod
    def zero():
        return Vector3(0, 0, 0)


@dataclasses.dataclass
class Hailstone:
    pos: Vector3
    vel: Vector3


hailstones = [
    Hailstone(
        Vector3(*[int(i) for i in pos.split(", ")]),
        Vector3(*[int(i) for i in vel.split(", ")]),
    )
    for pos, vel in hailstones
]

# part 1


def get_slope_and_intercept(p1, p2):
    m = (p2.y - p1.y) / (p2.x - p1.x)
    c = p1.y - m * p1.x

    return m, c


def in_past(x, h):
    return (x < h.pos.x and h.vel.x > 0) or (x > h.pos.x and h.vel.x < 0)


lower = 2e14
upper = 4e14

res = 0

for a, b in itertools.combinations(hailstones, 2):
    m1, c1 = get_slope_and_intercept(a.pos, a.pos + a.vel)
    m2, c2 = get_slope_and_intercept(b.pos, b.pos + b.vel)

    if m1 == m2:
        continue

    x = (c2 - c1) / (m1 - m2)
    y = m1 * x + c1

    if not (lower <= x <= upper) or not (lower <= y <= upper):
        continue

    if in_past(x, a) or in_past(x, b):
        continue

    res += 1

print(res)

# part 2


def intersect_plane_and_line(p0, n, h):
    d = n.dot(p0 - h.pos) / n.dot(h.vel)

    return h.pos + h.vel * d, d


origin = hailstones[0]
# translate all hailstones based on our chosen origin
hailstones = [Hailstone(h.pos - origin.pos, h.vel - origin.vel) for h in hailstones]

h1 = hailstones[1]
# define a normal vector to the plane at the origin using the second hailstone
n = h1.pos.cross(h1.pos + h1.vel)

# (0, 0, 0) is on the plane since we made it our origin
p0 = Vector3.zero()
p2, t2 = intersect_plane_and_line(p0, n, hailstones[2])
p3, t3 = intersect_plane_and_line(p0, n, hailstones[3])

# now the differences between the positions and times form a linear system
vel = (p3 - p2) / (t3 - t2)

print(int(sum(*[(p2 - vel * t2 + origin.pos)])))

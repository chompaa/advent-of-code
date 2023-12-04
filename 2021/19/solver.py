from os.path import dirname, join
from collections import defaultdict

with open(join(dirname(__file__), "example.txt")) as f:
  scanners = [
      {eval(line) for line in scanner.splitlines() if "scanner" not in line}
      for scanner in f.read().split("\n\n")
  ]


def rotate_point(n, p):
  x, y, z = p

  match n:
    case 0:
      return x, y, z
    case 1:
      return x, -z, y
    case 2:
      return x, -y, -z
    case 3:
      return x, z, -y
    case 4:
      return -x, -y, z
    case 5:
      return -x, -z, -y
    case 6:
      return -x, y, -z
    case 7:
      return -x, z, y
    case 8:
      return y, x, -z
    case 9:
      return y, -x, z
    case 10:
      return y, z, x
    case 11:
      return y, -z, -x
    case 12:
      return -y, x, z
    case 13:
      return -y, -x, -z
    case 14:
      return -y, -z, x
    case 15:
      return -y, z, -x
    case 16:
      return z, x, y
    case 17:
      return z, -x, -y
    case 18:
      return z, -y, x
    case 19:
      return z, y, -x
    case 20:
      return -z, x, -y
    case 21:
      return -z, -x, y
    case 22:
      return -z, y, x
    case 23:
      return -z, -y, -x


def sub_points(p1, p2):
  x1, y1, z1 = p1
  x2, y2, z2 = p2

  return (x1 - x2, y1 - y2, z1 - z2)


def add_points(p1, p2):
  x1, y1, z1 = p1
  x2, y2, z2 = p2

  return (x1 + x2, y1 + y2, z1 + z2)


def inv_point(p):
  x, y, z = p

  return -x, -y, -z


def find_full_map(scanners):
  ocean = set(scanners[0])
  scanners = scanners[1:]
  offsets = []

  def scan(scanners):
    for s in scanners:
      for n in range(24):
        rota_offsets = defaultdict(int)

        for ref_p in ocean:
          for pt in s:
            rota_offsets[sub_points(rotate_point(n, pt), ref_p)] += 1

        for offset, count in rota_offsets.items():
          if count < 12:
            continue

          offset = inv_point(offset)
          offsets.append(offset)

          for p in s:
            ocean.add(add_points(rotate_point(n, p), offset))

          scanners.remove(s)
          return scanners

    return scanners

  while scanners:
    scanners = scan(scanners)

  return len(ocean), offsets


beacons, offsets = find_full_map(scanners)

# part 1

print(beacons)


# part 2

def manhattan_dist(p1, p2):
  x1, y1, z1 = p1
  x2, y2, z2 = p2

  return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)


print(max(manhattan_dist(i, j) for j in offsets for i in offsets))

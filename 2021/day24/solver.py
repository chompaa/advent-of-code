from functools import lru_cache
from time import perf_counter

with open("input.txt", "r") as f:
  lines = f.read().splitlines()

progs = [line.split() for line in lines]


def find_model(start, end, step):
  @lru_cache(maxsize=None)
  def search(idx, w, x, y, z):
    # for z > 10^7, z will never converge to zero
    if z > 10 ** 7:
      return False, 0

    if idx == len(progs):
      return z == 0, ""

    lookup = {
        "w": w,
        "x": x,
        "y": y,
        "z": z,
    }

    ins = progs[idx]
    op = ins[0]

    if op == "inp":
      for n in range(start, end, step):
        lookup[ins[1]] = n
        res = search(
            idx + 1,
            lookup["w"],
            lookup["x"],
            lookup["y"],
            lookup["z"])

        if res[0]:
          return True, f"{str(n)}{res[1]}"

      return False, 0

    a = ins[1]
    # faster than the pythonic try-except method
    b = lookup[ins[2]] if ins[2] in lookup else int(ins[2])

    match op:
      case "add":
        lookup[a] += b
      case "mul":
        lookup[a] *= b
      case "div":
        if b == 0:
          return False, 0
        lookup[a] //= b
      case "mod":
        if lookup[a] < 0 or b <= 0:
          return False, 0
        lookup[a] %= b
      case "eql":
        lookup[a] = 1 if lookup[a] == b else 0

    return search(idx + 1, lookup["w"], lookup["x"], lookup["y"], lookup["z"])

  return search(0, 0, 0, 0, 0)[1]


# part 1

start_time = perf_counter()
print(find_model(9, 0, -1), perf_counter() - start_time)

# part 2

start_time = perf_counter()
print(find_model(1, 10, 1), perf_counter() - start_time)

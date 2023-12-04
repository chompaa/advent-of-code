from os.path import dirname, join

with open(join(dirname(__file__), "example.txt"), "r") as f:
  vals = [int(val) for val in f.read().split(",")]

# part 1


def get_fuel(vals, n):
  for j in range(len(vals)):
    yield(abs(vals[j] - n))


fuel_lst = [list(get_fuel(vals, n)) for n in range(max(vals))]

fuel_min = min([sum(fuel) for fuel in fuel_lst])

print(fuel_min)

# part 2

fuel_lst = [[int(((move * (move + 1)) / 2)) for move in fuel]
            for fuel in fuel_lst]

fuel_min = min([sum(fuel) for fuel in fuel_lst])

print(fuel_min)

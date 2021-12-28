from os.path import dirname, join
from copy import deepcopy

with open(join(dirname(__file__), "example.txt"), "r") as f:
  lines = [line.strip() for line in f.readlines()]

# part 1

lines = [[int(bit) for bit in line] for line in lines]
bit_sum = [sum(bit) for bit in zip(*lines)]

gamma = "".join("1" if i > len(lines) / 2 else "0" for i in bit_sum)
epsilon = "".join("1" if i < len(lines) / 2 else "0" for i in bit_sum)

print(int(gamma, 2) * int(epsilon, 2))

# part 2

oxy = deepcopy(lines)
oxy_sum = deepcopy(bit_sum)

for i in range(len(bit_sum)):
  if len(oxy) == 1:
    break

  oxy_crit = 0 if oxy_sum[i] >= len(oxy) / 2 else 1
  oxy = list(filter(lambda j: j[i] != oxy_crit, oxy))
oxy_sum = [sum(bit) for bit in zip(*oxy)]

co2 = deepcopy(lines)
co2_sum = deepcopy(bit_sum)

for i in range(len(bit_sum)):
  if len(co2) == 1:
    break

  co2_crit = 0 if co2_sum[i] < len(co2) / 2 else 1
  co2 = list(filter(lambda j: j[i] != co2_crit, co2))
  co2_sum = [sum(bit) for bit in zip(*co2)]

oxy = "".join(str(bit) for i in oxy for bit in i)
co2 = "".join(str(bit) for i in co2 for bit in i)

print(int(oxy, 2) * int(co2, 2))

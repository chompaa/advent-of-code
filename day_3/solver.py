from copy import deepcopy

with open("input.txt", "r") as f:
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
    oxy_queue = [line for line in oxy if line[i] == oxy_crit]
    oxy = [line for line in oxy if line not in oxy_queue]
    oxy_sum = [sum(bit) for bit in zip(*oxy)]

co2 = deepcopy(lines)
co2_sum = deepcopy(bit_sum)

for i in range(len(bit_sum)):
    if len(co2) == 1:
        break

    co2_crit = 0 if co2_sum[i] < len(co2) / 2 else 1
    co2_queue = [line for line in co2 if line[i] == co2_crit]
    co2 = [line for line in co2 if line not in co2_queue]
    co2_sum = [sum(bit) for bit in zip(*co2)]

oxy = int("".join(str(bit) for i in oxy for bit in i), 2)
co2 = int("".join(str(bit) for i in co2 for bit in i), 2)

print(oxy * co2)

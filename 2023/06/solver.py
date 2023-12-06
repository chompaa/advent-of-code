import inspect
import math
import os

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "input.txt"), "r") as f:
    lines = f.read().splitlines()

# part 1

times = list(map(int, lines[0].split(":")[-1].split()))
distances = list(map(int, lines[1].split(":")[-1].split()))

res = 1

# naive approach
for time, distance in zip(times, distances):
    res *= sum(hold * (time - hold) > distance for hold in range(time))

print(res)

# part 2

time = int(lines[0].split(":")[-1].replace(" ", ""))
distance = int(lines[1].split(":")[-1].replace(" ", ""))

res = 1

# seeking a solution where hold satisfies:
#   hold * (time - hold) > distance,
# rearrangement gives
#   hold^2 - time * hold + distance > 0
# which can be solved with quadratic formula:
#   -hold = (time +- sqrt(time^2 - 4 * distance)) / 2

root = (time**2 - 4 * distance) ** 0.5
hold_max = math.floor((time + root) / 2)
hold_min = math.ceil((time - root) / 2)
res = hold_max - hold_min + 1

print(res)

import inspect
import os
import re

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "example.txt"), "r") as f:
    lines = f.read().splitlines()

# part 1

res = 0

for line in lines:
    digits = re.sub("[^0-9]", "", line)

    if len(digits) == 0:
        continue

    res += int(f"{digits[0]}{digits[-1]}")

print(res)

# part 2

res = 0

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for line in lines:
    first = (-1, "")
    last = (-1, "")

    # faster than itertools.chain
    for digit in list(sum(digits.items(), ())):
        first_idx = line.find(digit)
        last_idx = line.rfind(digit)

        if first_idx != -1 and (first_idx < first[0] or first[0] == -1):
            first = (first_idx, digit)

        if last_idx != -1 and last_idx > last[0]:
            last = (last_idx, digit)

    if first[1] in digits:
        first = (first[0], digits[first[1]])

    if last[1] in digits:
        last = (last[0], digits[last[1]])

    res += int(f"{first[1]}{last[1]}")

print(res)

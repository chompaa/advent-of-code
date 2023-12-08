import inspect
import os
import re
import math

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "example.txt"), "r") as f:
    lines = f.read().splitlines()

ops = [int(op) for op in lines[0].translate(str.maketrans("LR", "01"))]
maps = {
    key: [re.sub(r"[()]", "", path) for path in values.split(", ")]
    for key, values in [line.split(" = ") for line in lines[2:]]
}


def find_path_count(maps, current, pattern):
    res = 0

    while not pattern(current):
        for op in ops:
            res += 1
            current = maps[current][op]
            if pattern(current):
                break

    return res


# part 1

print(find_path_count(maps, "AAA", lambda p: p == "ZZZ"))

# part 2

currents = tuple(node for node in maps if node.endswith("A"))
counts = [
    find_path_count(maps, current, lambda p: p.endswith("Z")) for current in currents
]


def find_lcm(lst):
    if len(lst) == 1:
        return lst[0]

    lcm = lst[0]

    for curr in lst[1:]:
        num = max(lcm, curr)
        den = min(lcm, curr)

        rem = num % den

        while rem != 0:
            num = den
            den = rem
            rem = num % den

        # den ends up being gcd

        lcm = int((lcm * curr) / den)

    return lcm


print(math.lcm(*counts))

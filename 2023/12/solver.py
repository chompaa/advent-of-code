import functools
import inspect
import os

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "input.txt"), "r") as f:
    entries = [
        (record, tuple(map(int, groups.split(","))))
        for record, groups in [entry.split() for entry in f.read().splitlines()]
    ]


@functools.cache
def count_permutations(record, groups, count=0):
    if not record:
        # if all groups are matched, return 1
        return len(groups) == 0

    res = 0

    branches = record[0].replace("?", ".#")

    for branch in branches:
        if branch == "#":
            # we either start a new group or continue a group
            res += count_permutations(record[1:], groups, count + 1)
        elif count:
            # we just ended a group, check if it matches the group we are on
            if groups and groups[0] == count:
                res += count_permutations(record[1:], groups[1:])
        else:
            # we are outside a group, keep going
            res += count_permutations(record[1:], groups)

    return res


# part 1

print(sum(count_permutations(f"{record}.", groups) for record, groups in entries))

# part 2

print(
    sum(
        count_permutations(f"{'?'.join([record] * 5)}.", groups * 5)
        for record, groups in entries
    )
)

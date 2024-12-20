import functools

patterns, designs = open(0).read().split("\n\n")

patterns = set(patterns.replace(" ", "").split(","))
designs = designs.splitlines()


@functools.cache
def dfs(design, pattern, index):
    if design[index : index + len(pattern)] != pattern:
        return 0

    index = index + len(pattern)

    if index >= len(design):
        return 1

    res = 0

    for p in patterns:
        res += dfs(design, p, index)

    return res


# Part 1

print(sum(min(1, dfs(design, "", 0)) for design in designs))

# Part 2

print(sum(dfs(design, "", 0) for design in designs))

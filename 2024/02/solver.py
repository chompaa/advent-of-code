levels = [list(map(int, line.split())) for line in open(0).read().splitlines()]


sign = lambda x: (1, -1)[x < 0]


def safe(level, i, j, s):
    delta = int(level[i]) - int(level[j])
    return sign(delta) == s and 1 <= abs(delta) <= 3


# Part 1

res = 0

for level in levels:
    s = sign(level[0] - level[1])
    for i in range(1, len(level)):
        if not safe(level, i - 1, i, s):
            break
    else:
        res += 1

print(res)

# Part 2


def level_safe_dampened(level, skip=False):
    s = sign(level[0] - level[1])
    for i in range(1, len(level)):
        if safe(level, i - 1, i, s):
            continue
        if skip:
            return False
        return (
            # Remove the `0`th element
            level_safe_dampened(level[1:], True)
            # Remove the `i - 1`th element
            or level_safe_dampened(level[: i - 1] + level[i:], True)
            # Remove the `i`th element
            or level_safe_dampened(level[:i] + level[i + 1 :], True)
        )
    return True


print(sum(level_safe_dampened(level) for level in levels))

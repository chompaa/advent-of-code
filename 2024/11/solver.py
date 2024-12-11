import functools

stones = list(map(int, open(0).read().splitlines()[0].split()))


def evolve(stones, limit):
    @functools.cache
    def r(stone, blinks=0):
        if blinks >= limit:
            return 1

        if stone == 0:
            return r(1, blinks + 1)

        stone_str = str(stone)
        stone_str_len = len(str(stone))
        if stone_str_len % 2 == 0:
            stone_str_len_div_2 = stone_str_len // 2
            left = int(stone_str[:stone_str_len_div_2])
            right = int(stone_str[stone_str_len_div_2:])
            return r(left, blinks + 1) + r(right, blinks + 1)

        return r(stone * 2024, blinks + 1)

    res = 0
    for stone in stones:
        res += r(stone)
    return res


# Part 1

print(evolve(stones, 25))

# Part 2

print(evolve(stones, 75))

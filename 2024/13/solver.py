import regex

machines = [line.split("\n") for line in open(0).read().rstrip().split("\n\n")]


def solve(a_x, a_y, b_x, b_y, p_x, p_y):
    det = a_x * b_y - a_y * b_x

    if abs(det) == 0:
        return 0

    k_1 = (b_y * p_x + -b_x * p_y) // det
    k_2 = (-a_y * p_x + a_x * p_y) // det

    if k_1 * a_x + k_2 * b_x == p_x and k_1 * a_y + k_2 * b_y == p_y:
        return 3 * int(k_1) + 1 * int(k_2)

    return 0


# Part 1

res = 0

for button_a, button_b, prize in machines:
    button_a = map(int, regex.findall(r"[+-]\d+", button_a))
    button_b = map(int, regex.findall(r"[+-]\d+", button_b))
    prize = map(int, regex.findall(r"-?\d+", prize))
    res += solve(*button_a, *button_b, *prize)

# Part 2

res = 0
offset = 10000000000000

for button_a, button_b, prize in machines:
    button_a = map(int, regex.findall(r"[+-]\d+", button_a))
    button_b = map(int, regex.findall(r"[+-]\d+", button_b))
    p_x, p_y = map(int, regex.findall(r"-?\d+", prize))
    res += solve(*button_a, *button_b, p_x + offset, p_y + offset)

print(res)

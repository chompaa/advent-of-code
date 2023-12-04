import inspect
import os

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "example.txt"), "r") as f:
    cards = [
        (n1.split(": ")[-1].split(), n2.split())
        for n1, n2 in [card.split(" | ") for card in f.read().splitlines()]
    ]


def get_winning_amount(win, play):
    return sum(n in win for n in play)


# part 1

res = 0

for win, play in cards:
    amt = get_winning_amount(win, play)

    if amt != 0:
        res += 2 ** (amt - 1)

print(res)

# part 2

res = [1 for _ in range(len(cards))]

for num, (win, play) in enumerate(cards):
    amt = get_winning_amount(win, play)

    for i in range(num + 1, num + amt + 1):
        res[i] += res[num]

print(sum(res))

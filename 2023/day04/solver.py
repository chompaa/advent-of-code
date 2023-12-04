import os
import collections

cards = []

with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
    cards = [
        (n1.split(": ")[-1].split(), n2.split())
        for n1, n2 in [card.split(" | ") for card in f.read().splitlines()]
    ]


def get_winning_amount(win, play):
    return sum(n in win for n in play)


res = 0

for win, play in cards:
    amt = get_winning_amount(win, play)

    if amt != 0:
        res += 2 ** (amt - 1)

print(res)

res = [1 for _ in range(len(cards))]

for num, (win, play) in enumerate(cards):
    amt = get_winning_amount(win, play)

    for i in range(num + 1, num + amt + 1):
        res[i] += res[num]

print(sum(res))

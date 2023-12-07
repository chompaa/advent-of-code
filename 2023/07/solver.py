import os
import inspect
import collections

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "example.txt"), "r") as f:
    lines = [line.split() for line in f.read().splitlines()]

hands = [line[0] for line in lines]
bids = {line[0]: line[1] for line in lines}


def get_rank(hand):
    counts = collections.Counter(list(hand))
    unique_cards = len(counts)
    max_count = max(counts.values())

    if unique_cards == 1:
        # five of a kind
        return 7
    elif max_count == 4:
        # four of a kind
        return 6
    elif unique_cards == 2:
        # full hoise
        return 5
    elif max_count == 3:
        # three of a kind
        return 4
    elif unique_cards == 3:
        # two pair
        return 3
    elif unique_cards == 4:
        # one pair
        return 2
    else:
        # high card
        return 1


def get_winnings(pairs):
    return sum(int(bids[hand]) * (idx + 1) for idx, hand in enumerate(pairs))


# part 1

order = "23456789TJQKA"

res = [
    hand
    for hand, _ in sorted(
        [[hand, get_rank(hand)] for hand in hands],
        key=lambda x: (
            x[1],
            *map(order.index, x[0]),
        ),
    )
]

print(get_winnings(res))

# part 2


def replace_joker(hand, order):
    counts = collections.Counter(list(hand))

    if len(counts) == 1:
        return hand

    # don't count jokers if it's not a full house
    del counts["J"]

    max_card = max(counts, key=counts.get)

    for card, amount in counts.items():
        if order.index(card) > order.index(max_card) and amount == counts[max_card]:
            max_card = card

    hand = hand.replace("J", max_card)

    return hand


order = "J23456789TQKA"

res = [
    hand
    for hand, _ in sorted(
        [[hand, get_rank(replace_joker(hand, order))] for hand in hands],
        key=lambda x: (
            x[1],
            *map(order.index, x[0]),
        ),
    )
]


print(get_winnings(res))

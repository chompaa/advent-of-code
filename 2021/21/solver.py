from os.path import dirname, join
from itertools import cycle, product
from functools import lru_cache
from collections import Counter

with open(join(dirname(__file__), "example.txt")) as f:
  lines = [int(line[-1]) for line in f.read().splitlines()]

p1_start = lines[0]
p2_start = lines[1]


# part 1

def get_min_deterministic_score(p1_pos, p2_pos):
  p1_score = p2_score = 0
  die = cycle(range(1, 101))
  rolls = 0

  while True:
    p1_pos = (p1_pos + next(die) + next(die) + next(die) - 1) % 10 + 1
    p1_score += p1_pos
    rolls += 3

    if p1_score >= 1000:
      return p2_score, rolls

    p2_pos = (p2_pos + next(die) + next(die) + next(die) - 1) % 10 + 1
    p2_score += p2_pos
    rolls += 3

    if p2_score >= 1000:
      return p1_score, rolls


score, rolls = get_min_deterministic_score(p1_start, p2_start)
print(score * rolls)

# part 2

# find the amount of combinations for each roll
combs = Counter(
    (sum(r)
     for r in product((1, 2, 3),
                      (1, 2, 3),
                      (1, 2, 3)))).items()


# couldn't figure out how to implement a linear dp solution :(
@lru_cache(maxsize=None)
def get_dirac_wins(p1_pos, p2_pos, p1_score, p2_score):
  p1_wins = p2_wins = 0

  for roll, count in combs:
    new_p1_pos = (p1_pos + roll - 1) % 10 + 1
    new_p1_score = new_p1_pos + p1_score

    if new_p1_score >= 21:
      p1_wins += count
    else:
      _p2_wins, _p1_wins = get_dirac_wins(
          p2_pos, new_p1_pos, p2_score, new_p1_score)
      p1_wins += _p1_wins * count
      p2_wins += _p2_wins * count

  return p1_wins, p2_wins


print(max(get_dirac_wins(p1_start, p2_start, 0, 0)))

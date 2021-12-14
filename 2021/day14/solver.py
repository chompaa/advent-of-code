from collections import Counter, defaultdict

with open("input.txt") as f:
  lines = [line.strip() for line in f.readlines()]

# template
template = lines[0]
# insertions
ins = {tuple(s.split(" -> ")[0]): s.split(" -> ")[1] for s in lines[2:]}


def difference(step, temp, ins):
  # assign counts to template pairs
  pairs = Counter(zip(temp, temp[1:]))

  # to keep track of letter counts
  counts = defaultdict(int)

  new_pairs = defaultdict(int)

  for _ in range(step):
    for pair, count in pairs.items():
      if count == 0:
        continue

      new_pairs[(pair[0], ins[pair])] += count
      new_pairs[(ins[pair], pair[1])] += count

    _pairs = new_pairs.copy()
    # reset new_pairs
    new_pairs = defaultdict(int)
    # accumulate total pairs
    pairs = _pairs.copy()

  for pair, count in pairs.items():
    counts[pair[1]] += count

  return max(counts.values()) - min(counts.values())


# part 1

print(difference(10, template, ins))

# part 2

print(difference(40, template, ins))

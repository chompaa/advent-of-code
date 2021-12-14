with open("input.txt") as f:
  lines = [line.strip() for line in f.readlines()]

# template
template = lines[0]
# insertions
ins = {tuple(s.split(" -> ")[0]): s.split(" -> ")[1] for s in lines[2:]}


def difference(step, temp, ins):
  # for resetting pair counts
  zero_pairs = {k: 0 for k in ins}

  # template pairs
  temp_pairs = [(temp[idx - 1], temp[idx])
                for idx in range(1, len(temp))]

  # assign counts to template pairs
  pairs = zero_pairs.copy()
  for pair in temp_pairs:
    pairs[pair] += 1

  # to keep track of letter counts
  counts = {letter: 0 for letter in set(ins.values())}

  new_pairs = zero_pairs.copy()

  for _ in range(step):
    for pair, count in pairs.items():
      if count == 0:
        continue

      new_pairs[(pair[0], ins[pair])] += count
      new_pairs[(ins[pair], pair[1])] += count

    _pairs = new_pairs.copy()
    # reset new_pairs
    new_pairs = zero_pairs.copy()
    # accumulate total pairs
    pairs = _pairs.copy()

  for pair, count in pairs.items():
    counts[pair[1]] += count

  least = min(list(counts.values()))
  most = max(list(counts.values()))

  return most - least


# part 1

print(difference(10, template, ins))

# part 2

print(difference(40, template, ins))

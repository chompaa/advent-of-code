from os.path import dirname, join

with open(join(dirname(__file__), "example.txt"), "r") as f:
  vals = [line for line in f.read()]

vals = ("".join(val for val in vals for _ in val)).split("\n")

# part 1

digits = [2, 3, 4, 7]
count = 0

for val in vals:
  found = {num: [] for num in digits}
  signals, output = val.split(" |")

  for digit in signals.split():
    if len(digit) in digits and digit not in found[len(digit)]:
      found[len(digit)].append(digit)

  for digit in output.split():
    signals = found.get(len(digit), None)
    try:
      for s in signals:
        if sorted(digit) == sorted(s):
          count += 1
    except TypeError:
      pass

print(count)

# part 2


class Solver():
  def remove_candidates(self, queue, n1, n2, n3):
    for candidate in queue:
      self.signals[n1].remove(candidate)

    self.signals[n2] = list(
        filter(lambda x: x != self.signals[n1][0], self.signals[n2]))
    self.signals[n3] = list(
        filter(lambda x: x != self.signals[n1][0], self.signals[n3]))

  def digit_difference(self, d1, d2):
    signal = self.signals.get(d1)[0]

    for char in self.signals.get(d2)[0]:
      signal = signal.replace(char, "")

    return signal

  def __init__(self, val):
    self.signals = {
        0: [], 1: [], 2: [], 3: [], 4: [],
        5: [], 6: [], 7: [], 8: [], 9: []
    }

    self.digits = {
        0: 6, 1: 2, 2: 5, 3: 5, 4: 4,
        5: 5, 6: 6, 7: 3, 8: 7, 9: 6
    }
    self.val = val

    signals, output = val.split(" |")

    for digit in signals.split():
      for k, v in self.digits.items():
        if v == len(digit):
          self.signals[k].append(digit)

    for k, v in self.signals.items():
      match k:
        # isolate 1
        case 1:
          queue = []
          for candidate in self.signals[6]:
            if set(candidate) & set(v[0]) == set(v[0]):
              queue.append(candidate)

          self.remove_candidates(queue, 6, 0, 9)
        # isolate 0 and 9
        case 4:
          queue = []
          for candidate in self.signals[0]:
            if set(candidate) & set(v[0]) == set(v[0]):
              queue.append(candidate)

          self.remove_candidates(queue, 0, 6, 9)
        # isolate 3
        case 7:
          queue = []
          for candidate in self.signals[3]:
            if set(candidate) & set(v[0]) != set(v[0]):
              queue.append(candidate)

          self.remove_candidates(queue, 3, 2, 5)

    # when considering 2 and 5, b is unique to 5
    # hence we isolate b via 4 - 3
    b_map = self.digit_difference(4, 3)

    # isolate 2 and 5
    queue = []
    for candidate in self.signals[2]:
      if b_map in candidate:
        queue.append(candidate)

    self.remove_candidates(queue, 2, 5, 3)

    count = ""
    for digit in output.split():
      for k, v in self.signals.items():
        if sorted(digit) == sorted(v[0]):
          count += str(k)

    self.count = count

  def get_count(self):
    return self.count


print(sum([int(Solver(val).get_count()) for val in vals]))

with open("input.txt", "r") as f:
  vals = [int(val) for val in f.readlines()[0] if val != ","]

fish = dict()

for i in range(-1, 9):
  fish[i] = 0

for val in vals:
  fish[val] += 1

# part 1

_fish = fish.copy()

for i in range(80):
  for j in range(0, len(_fish) - 1):
    _fish[j - 1] = _fish[j]

  _fish[8] = _fish[-1]
  _fish[6] += _fish[-1]
  _fish[-1] = 0

print(sum(list(_fish.values())))

# part 2

for i in range(256):
  for j in range(0, len(fish) - 1):
    fish[j - 1] = fish[j]

  fish[8] = fish[-1]
  fish[6] += fish[-1]
  fish[-1] = 0

print(sum(list(fish.values())))

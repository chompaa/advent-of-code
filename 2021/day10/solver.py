with open("example.txt", "r") as f:
  lines = f.read().splitlines()

syms = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

# part 1

illegal_weights = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

score = 0

for line in lines:
  stack = []

  for idx, char in enumerate(line):
    if char in syms.keys():
      stack.append(char)
    elif syms[stack.pop()] != char:
      score += illegal_weights[line[idx]]
      break


print(score)

# part 2

open_weights = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

scores = []

for line in lines:
  stack = []
  score = 0

  for idx, char in enumerate(line):
    if char in syms.keys():
      stack.append(char)
    elif syms[stack.pop()] != char:
      break
  else:
    for char in reversed(stack):
      score *= 5
      score += open_weights[char]
    scores.append(score)

print(sorted(scores)[len(scores) // 2])

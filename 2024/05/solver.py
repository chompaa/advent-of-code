import collections
import copy

data = open(0).read().split("\n\n")

rules = collections.defaultdict(set)
for rule in data[0].split():
    a, b = map(int, rule.split("|"))
    rules[b].add(a)

updates = [list(map(int, line.split(","))) for line in data[1].split()]

# Part 1

res = 0

for update in updates:
    valid = True
    for index, page in enumerate(update):
        if rules[page].intersection(set(update[index + 1 :])):
            break
    else:
        res += update[len(update) // 2]


print(res)

# Part 2

res = 0

for update in updates:
    bad = False
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] in rules[update[i]]:
                update.insert(i, update.pop(j))
                bad = True
    if bad:
        res += update[len(update) // 2]

print(res)

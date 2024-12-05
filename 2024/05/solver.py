import collections

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
    sorting = True
    corrected = False
    while sorting:
        sorting = False
        for index, page in enumerate(update):
            for n in rules[page]:
                if n in update[index + 1 :]:
                    update.remove(n)
                    update.insert(index, n)
                    sorting = True
                    corrected = True
    if corrected:
        res += update[len(update) // 2]

print(res)

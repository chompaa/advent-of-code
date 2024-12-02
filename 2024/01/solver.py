import collections

lines = open(0, "r").read().splitlines()

a = [line.split()[0] for line in lines]
b = [line.split()[1] for line in lines]

# Part 1

print(sum(abs(int(p) - int(q)) for p, q in zip(sorted(a), sorted(b))))

# Part 2

counts = collections.Counter(b)
print(sum(int(p) * counts[p] for p in a))

import re

data = "".join(open(0).read().splitlines())

# Part 1

res = 0
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

for a, b in re.findall(pattern, data):
    res += int(a) * int(b)

print(res)

# Part 2

res = 0
pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))"
e = True

for m in re.findall(pattern, data):
    match m[0]:
        case "do()":
            e = True
        case "don't()":
            e = False
        case _ if e:
            res += int(m[1]) * int(m[2])

print(res)

with open("input.txt", "r") as f:
    depths = [int(line.strip()) for line in f]

# Part 1

increased = 0

for i in range(1, len(depths)):
    if int(depths[i]) > int(depths[i - 1]):
        increased += 1

print(increased)

# Part 2

increased = 0

for i in range(3, len(depths)):
    if int(depths[i]) > int(depths[i - 3]):
        increased += 1

print(increased)

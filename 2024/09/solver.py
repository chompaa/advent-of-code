disk_map = list(map(int, list(open(0).read().splitlines()[0])))


def form_blocks(disk_map):
    blocks = []
    j = 0

    for i in range(len(disk_map)):
        if i % 2 == 0:
            for _ in range(disk_map[i]):
                blocks.append(j)
            j += 1
        else:
            for _ in range(disk_map[i]):
                blocks.append(".")

    return blocks


def checksum(blocks):
    return sum(id * block for id, block in enumerate(blocks) if block != ".")


# Part 1


blocks = form_blocks(disk_map)
l, r = 0, len(blocks) - 1

while l < r:
    while blocks[l] != ".":
        l += 1
    while blocks[r] == ".":
        r -= 1
    if l < r:
        blocks[l], blocks[r] = blocks[r], blocks[l]


print(checksum(blocks))

# Part 2


blocks = form_blocks(disk_map)


def space(blocks, l=0):
    while l < len(blocks) - 1 and blocks[l] != ".":
        l += 1
    r = l + 1
    while r < len(blocks) - 1 and blocks[r] == ".":
        r += 1
    return (l, r)


def search_files(blocks, r=0):
    while r > 0 and blocks[r] == ".":
        r -= 1
    l = r - 1
    while l >= 0 and blocks[l] != "." and blocks[l] == blocks[r]:
        l -= 1
    return (l + 1, r + 1)


files = []

r = len(blocks) - 1
while r >= 0:
    f = search_files(blocks, r)
    files.append((blocks[f[0]], f))
    r = f[0] - 1
files = sorted(files, key=lambda f: f[0], reverse=True)


for _, (fl, fr) in files:
    # Find the nearest (left) space
    s = space(blocks)
    sl, sr = s
    d = (sr - sl) - (fr - fl)

    # If we haven't found a big enough gap, keep searching to the left
    while sr < len(blocks) and d < 0 and sl < fl:
        sl, sr = space(blocks, sr)
        d = (sr - sl) - (fr - fl)

    # Did we find a large enough left gap?
    if d >= 0 and sl < fl:
        blocks[sl : sr - d], blocks[fl:fr] = (
            blocks[fl:fr],
            blocks[sl : sr - d],
        )

print(checksum(blocks))

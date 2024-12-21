import heapq
import time
import math
import collections

lines = open(0).read().splitlines()

maze = {(y, x): lines[x][y] for x in range(len(lines[0])) for y in range(len(lines))}

s = e = (0, 0)

for c, t in maze.items():
    if t == "S":
        s = c
    elif t == "E":
        e = c


def dijkstra(s, e):
    dist = {}

    q = [(0, s, (1, 0), [])]

    paths = []
    lowest_score = math.inf

    while q:
        score, curr, dir, path = heapq.heappop(q)
        cx, cy = curr

        if score > lowest_score:
            break

        if (curr, dir) in dist and dist[(curr, dir)] < score:
            continue
        dist[(curr, dir)] = score

        if curr == e:
            lowest_score = min(lowest_score, score)
            paths.append(path)

        for d in rots(*dir):
            heapq.heappush(q, (score + 1000, curr, d, path))

        dx, dy = dir
        n = (cx + dx, cy + dy)
        if n in maze and maze[n] != "#":
            heapq.heappush(q, (score + 1, n, dir, path + [n]))

    return paths, lowest_score


paths, lowest_score = dijkstra(s, e)

# Part 1

print(lowest_score)

# Part 2

print(len(set([p for q in paths for p in q])) + 1)

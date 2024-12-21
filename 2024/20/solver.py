import collections
import heapq
import itertools

lines = open(0).read().splitlines()

racetrack = {
    (x, y): lines[y][x] for y in range(len(lines)) for x in range(len(lines[0]))
}

start = next(pos for pos, track in racetrack.items() if track == "S")
end = next(pos for pos, track in racetrack.items() if track == "E")


def dfs(start, end):
    q = [(0, start)]
    distances = collections.defaultdict(int)
    path = []
    seen = set()

    while q:
        dist, curr = heapq.heappop(q)

        if curr in seen:
            continue
        seen.add(curr)

        distances[curr] = dist
        path.append(curr)

        if curr == end:
            return distances

        cx, cy = curr
        for dx, dy in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            n = (cx + dx, cy + dy)

            if n in racetrack and racetrack[n] != "#":
                heapq.heappush(q, (dist + 1, n))

    return distances


distances = dfs(start, end)
res = 0


def cheat(count, threshold):
    res = 0
    for (sx, sy), (ex, ey) in itertools.combinations(distances.keys(), 2):
        manhattan = abs(sx - ex) + abs(sy - ey)
        if manhattan <= count:
            delta = distances[(ex, ey)] - distances[(sx, sy)] - manhattan
            if delta >= threshold:
                res += 1
    return res


# Part 1

print(cheat(2, 100))

# Part 2

print(cheat(20, 100))

from heapq import heappush, heappop
from collections import defaultdict
from math import sqrt

with open("input.txt") as f:
  cavern = [[int(col) for col in row] for row in f.read().splitlines()]

last = len(cavern) - 1
graph = {}

for row_idx, row in enumerate(cavern):
  for col_idx, col in enumerate(row):
    graph[(row_idx, col_idx)] = col


def get_neighbours(node):
  x, y = node
  nodes = []

  directions = [
      (x - 1, y),
      (x + 1, y),
      (x, y - 1),
      (x, y + 1),
  ]

  for i, j in directions:
    nodes.append((i, j))

  return nodes


def dijkstra(graph, start, end):
  seen = set(start)
  queue = [(0, start)]

  while len(queue) > 0:
    dist, node = heappop(queue)

    if node == end:
      return dist

    # if node in seen:
    #   continue

    # seen.add(node)

    for neighbour in get_neighbours(node):
      if neighbour not in graph or neighbour in seen:
        continue

      heappush(queue, (dist + graph[neighbour], neighbour))
      seen.add(neighbour)


# part 1

start = (0, 0)
end = (len(cavern) - 1, len(cavern) - 1)

print(dijkstra(graph, start, end))

# part 2

offset = len(cavern)

# definitely a better way to do this...

for _ in range(1, 5):
  chunk = graph.copy()

  for node, cost in graph.items():
    x, y = node
    cost = 9 if (cost + 1) % 9 == 0 else (cost + 1) % 9
    chunk[x + offset, y] = cost

  graph.update(chunk)

for _ in range(1, 5):
  chunk = {}

  for node, cost in graph.items():
    x, y = node
    cost = 9 if (cost + 1) % 9 == 0 else (cost + 1) % 9
    chunk[x, y + offset] = cost

  graph.update(chunk)


start = (0, 0)
last = int(sqrt(len(graph))) - 1
end = (last, last)

print(dijkstra(graph, start, end))

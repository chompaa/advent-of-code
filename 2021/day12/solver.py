with open("input.txt") as f:
  lines = [line for line in f.read().splitlines()]

nodes = []

for line in lines:
  for n in line.split("-"):
    if n not in nodes:
      nodes.append(n)

graph = {node: [] for node in nodes}

for node in nodes:
  for line in lines:
    x, y = line.split("-")

    if x == node:
      if y == "start":
        continue

      if y not in graph[node]:
        graph[node].append(y)
    elif y == node:
      if x == "start":
        continue

      if x not in graph[node]:
        graph[node].append(x)

graph["end"] = []


def dfs(prev, seen, graph, two=False):
  if prev == "end":
    return 1

  paths = 0

  for node in graph[prev]:
    if not (node.islower() and node in seen):
      paths += dfs(node, seen.union({node}), graph, two)
    elif node.islower() and node in seen and two:
      paths += dfs(node, seen.union({node}), graph, False)

  return paths


# part 1

print(dfs("start", set(), graph))

# part 2

print(dfs("start", set(), graph, True))

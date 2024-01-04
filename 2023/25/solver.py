import inspect
import os

import networkx as nx

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

wiring = nx.Graph()

with open(os.path.join(cwd, "example.txt"), "r") as f:
    wires = {
        component: connections.split()
        for component, connections in [
            line.split(": ") for line in f.read().splitlines()
        ]
    }

# part 1

# TODO: don't use a library :)

for component, connections in wires.items():
    for connection in connections:
        wiring.add_edge(component, connection)
        wiring.add_edge(connection, component)

wiring.remove_edges_from(nx.minimum_edge_cut(wiring))
a, b = nx.connected_components(wiring)

print(len(a) * len(b))

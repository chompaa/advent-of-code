import collections
import inspect
import os

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "example.txt"), "r") as f:
    histories = [list(map(int, history.split())) for history in f.readlines()]


def get_sequences(history):
    q = collections.deque()
    q.append(history)
    sequences = [history]

    while q:
        current = q.pop()
        prev = current[0]
        diff = []

        for next in current[1:]:
            diff.append(next - prev)
            prev = next

        if any(d != 0 for d in diff):
            q.append(diff)

        sequences.append(diff)

    return sequences


def extrapolate(history, index, f):
    sequences = get_sequences(history)
    prev = sequences[-1][-1]

    for sequence in sequences[-2::-1]:
        prev = f(sequence[index], prev)

    return prev


# part 1

print(sum(extrapolate(history, -1, lambda x, y: x + y) for history in histories))

# part 2

print(sum(extrapolate(history, 0, lambda x, y: x - y) for history in histories))

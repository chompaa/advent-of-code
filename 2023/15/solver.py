import collections
import functools
import inspect
import os

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "example.txt"), "r") as f:
    steps = f.read().splitlines()[0].split(",")


def hash(label):
    return functools.reduce(lambda acc, char: (acc + ord(char)) * 17 % 256, label, 0)


# part 1

print(sum(hash(step) for step in steps))

# part 2

boxes = collections.defaultdict(dict)

for step in steps:
    if step.endswith("-"):
        label = step[:-1]
        boxes[hash(label)].pop(label, -1)
    else:
        label, focal = step.split("=")
        boxes[hash(label)][label] = int(focal)


print(
    sum(
        sum(
            (box + 1) * (slot + 1) * focal for slot, focal in enumerate(lenses.values())
        )
        for box, lenses in boxes.items()
    )
)

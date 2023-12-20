import inspect
import math
import os
import re

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "example.txt"), "r") as f:
    workflows, ratings = f.read().split("\n\n")

    workflows = {
        name: rules[:-1].split(",")
        for name, rules in [workflow.split("{") for workflow in workflows.splitlines()]
    }

    ratings = [rating[1:-1] for rating in ratings.splitlines()]

# part 1

ops = {">": lambda x, y: x > y, "<": lambda x, y: x < y}
res = 0

for rating in ratings:
    values = {
        "xmas"[idx]: int(r.split(",")[0]) for idx, r in enumerate(rating.split("=")[1:])
    }

    workflow = "in"

    while workflow not in "AR":
        for rule in workflows[workflow]:
            if ":" not in rule:
                workflow = rule
                break

            if ops[rule[1]](values[rule[0]], int(re.findall(r"-?\d+", rule)[0])):
                workflow = rule.split(":")[1]
                break

    if workflow == "A":
        res += sum(values.values())

print(res)

# part 2

# not a huge fan of writing a class, but it makes it easier to work with intervals


class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def __mul__(self, other):
        # [1, 10] * [5, 10] = [5, 10]

        if self.lower <= other.lower <= self.upper:
            lower = other.lower
        elif other.lower <= self.lower <= other.upper:
            lower = self.lower
        else:
            return None

        if self.lower <= other.upper <= self.upper:
            upper = other.upper
        elif other.lower <= self.upper <= other.upper:
            upper = self.upper
        else:
            return None

        return Interval(lower, upper)

    def __truediv__(self, other):
        # [1, 10] / [3, 5] = [1, 2] union [6, 10]

        if self.lower == other.lower and self.upper == other.upper:
            return None

        if self.lower == other.lower:
            return (Interval(other.upper + 1, self.upper),)

        if self.upper == other.upper:
            return (Interval(self.lower, other.lower - 1),)

        return (
            Interval(self.lower, other.lower - 1),
            Interval(other.upper + 1, self.upper),
        )

    def __len__(self):
        return self.upper - self.lower + 1

    def __bool__(self):
        return True


MIN = 1
MAX = 4000


def find_accepted_combinations(workflow, values, intervals, rule_start=0):
    if workflow == "A":
        return math.prod(len(interval) for interval in intervals.values())
    elif workflow == "R":
        return 0

    res = 0

    for rule_idx, rule in enumerate(workflows[workflow][rule_start:]):
        if ":" not in rule:
            res += find_accepted_combinations(rule, values, intervals)
            break

        compare = int(re.findall(r"-?\d+", rule)[0])
        rating_label = rule[0]
        rating = intervals[rating_label]
        operation = rule[1]

        send = (
            Interval(compare + 1, MAX)
            if operation == ">"
            else Interval(MIN, compare - 1)
        )

        overlap = rating * send

        if not overlap:
            continue

        # send overlap to next workflow
        intervals[rating_label] = overlap
        res += find_accepted_combinations(rule.split(":")[1], values, intervals)

        # process outside of overlap in consequent rules
        outside = rating / overlap

        for interval in outside:
            intervals[rating_label] = interval
            res += find_accepted_combinations(
                workflow, values, intervals, rule_start=rule_idx + 1
            )

        intervals[rating_label] = rating

        break

    return res


print(
    find_accepted_combinations(
        "in", ratings, {char: Interval(MIN, MAX) for char in "xmas"}
    )
)

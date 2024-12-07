import abc

equations = [
    (int(test), list(map(int, remaining.split())))
    for line in open(0).read().splitlines()
    for test, remaining in [line.split(": ")]
]


class Op(metaclass=abc.ABCMeta):
    ch: str

    @classmethod
    @abc.abstractmethod
    def apply(cls, a: int, b: int) -> int: ...


class Add(Op):
    ch = "+"

    @classmethod
    def apply(cls, a: int, b: int) -> int:
        return a + b


class Mul(Op):
    ch = "*"

    @classmethod
    def apply(cls, a: int, b: int) -> int:
        return a * b


def calibration_result(equations, ops: list[type[Op]]):
    res = 0

    for test, remaining in equations:
        q = [tuple((remaining[0], 0, op)) for op in ops]

        while q:
            curr, index, op = q.pop(0)

            if index >= len(remaining) - 1:
                if curr == test:
                    res += test
                    break
                continue

            curr = op.apply(curr, remaining[index + 1])

            if curr > test:
                continue

            for op in ops:
                q.append((curr, index + 1, op))

    return res


# Part 1

print(calibration_result(equations, [Add, Mul]))

# Part 2


class Concat(Op):
    ch = "*"

    @classmethod
    def apply(cls, a: int, b: int) -> int:
        return int(f"{a}{b}")


print(calibration_result(equations, [Add, Mul, Concat]))

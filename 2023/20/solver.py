import collections
import dataclasses
import enum
import inspect
import math
import os

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

with open(os.path.join(cwd, "example.txt"), "r") as f:
    lines = f.read().splitlines()


class Pulse(enum.Enum):
    NONE = -1
    LOW = 0
    HIGH = 1


@dataclasses.dataclass
class Module:
    name: str
    inputs: list = dataclasses.field(default_factory=list)
    outputs: list = dataclasses.field(default_factory=list)
    sent_amount: dict = dataclasses.field(
        default_factory=lambda: {Pulse.LOW: 0, Pulse.HIGH: 0}
    )
    last_signal: Pulse = Pulse.NONE

    def __repr__(self):
        return f"{type(self).__name__}({self.name})"

    def __hash__(self):
        return hash(self.name)

    def send(self, signal):
        for output in self.outputs:
            yield (self, signal, output)
            self.sent_amount[signal] += 1

    def receive(self, _, signal):
        return signal


@dataclasses.dataclass(eq=False, repr=False)
class Broadcast(Module):
    ...


@dataclasses.dataclass(eq=False, repr=False)
class Flip(Module):
    active: bool = False

    def receive(self, _, signal):
        if signal == Pulse.HIGH:
            return

        self.active = not self.active

        return Pulse.HIGH if self.active else Pulse.LOW


@dataclasses.dataclass(eq=False, repr=False)
class Conjunction(Module):
    inputs: dict = dataclasses.field(default_factory=dict)

    def receive(self, sender, signal):
        self.inputs[sender] = signal

        if any(signal == Pulse.LOW for signal in self.inputs.values()):
            return Pulse.HIGH

        return Pulse.LOW


@dataclasses.dataclass(eq=False, repr=False)
class RX(Module):
    ...


@dataclasses.dataclass(eq=False, repr=False)
class Empty(Module):
    ...


def get_modules(lines, rx=False):
    modules = {}

    for line in lines:
        module, _ = line.split(" -> ")

        match module[0]:
            case "b":
                modules[module] = Broadcast(name=module)
            case "%":
                modules[module[1:]] = Flip(name=module[1:])
            case "&":
                modules[module[1:]] = Conjunction(name=module[1:])

    for line in lines:
        module, outputs = line.split(" -> ")
        outputs = outputs.split(", ")
        module = module.replace("%", "").replace("&", "")

        for output in outputs:
            if output not in modules:
                modules[output] = (
                    RX(name=output) if output == "rx" and rx else Empty(name=output)
                )

            module_type = type(modules[output])

            if module_type == Conjunction:
                modules[output].inputs[modules[module]] = Pulse.LOW
            elif module_type in [Flip, RX]:
                modules[output].inputs.append(modules[module])

            modules[module].outputs.append(modules[output])

    return modules


# part 1


def push_button(m, n=1000):
    for _ in range(n):
        broadcasts = m["broadcaster"].send(Pulse.LOW)
        queue = [*broadcasts]

        while queue:
            sender, signal, to = queue.pop(0)
            # print(sender, signal, to)
            signal = to.receive(sender, signal)
            to.last_signal = signal

            if signal is None:
                continue

            queue.extend((sender, signal, to) for sender, signal, to in to.send(signal))

    return m


low_pulses = 1000
high_pulses = 0

for module in push_button(get_modules(lines)).values():
    low_pulses += module.sent_amount[Pulse.LOW]
    high_pulses += module.sent_amount[Pulse.HIGH]


print(low_pulses * high_pulses)

# part 2

modules = get_modules(lines, rx=True)
start = "rx"
module = modules[start]

visited = set()
required = collections.defaultdict(dict)
required[start] = {"signal": Pulse.HIGH, "branch": 0}
queue = [(module_input, module, 0) for module_input in module.inputs]

while queue:
    module, prev, branch = queue.pop(0)
    module_inputs = module.inputs

    if (module, prev) in visited:
        continue

    visited.add((module, prev))

    if type(module) in [Flip, Conjunction]:
        signal = Pulse.HIGH if required[prev.name] == Pulse.LOW else Pulse.LOW
        required[module.name] = {"signal": signal, "branch": branch}

    if type(module_inputs) == dict:
        module_inputs = module_inputs.keys()

    for b, input in enumerate(module_inputs):
        if prev.name == start:
            branch = b + 1

        queue.append((input, module, branch))

cycles = {}

for i in range(1, 5000):
    modules = push_button(modules, n=1)

    for module in modules:
        if (
            module not in required
            or modules[module].last_signal != required[module]["signal"]
            or module in cycles
        ):
            continue

        cycles[module] = i


max_cycles = [0, 0, 0, 0]

for module, cycle in cycles.items():
    branch = required[module]["branch"] - 1
    max_cycles[branch] = max(max_cycles[branch], cycle)

print(math.lcm(*max_cycles))

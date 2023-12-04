import inspect
import math
import os

cwd = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

games = []

with open(os.path.join(cwd, "example.txt"), "r") as f:
    for line in f.read().splitlines():
        game = line.split(": ")[1]
        moves = [
            [pair.split(" ") for pair in move.split(", ")] for move in game.split("; ")
        ]
        games.append(moves)

# part 1

res = 0

for game_id, game in enumerate(games):
    for moves in game:
        cube_count = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }

        for amount, cube in moves:
            cube_count[cube] -= int(amount)

        if any(count < 0 for count in cube_count.values()):
            break
    else:
        res += game_id

print(res)

# part 2

res = 0

for game in games:
    cube_max = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for moves in game:
        for amount, cube in moves:
            cube_max[cube] = max(cube_max[cube], int(amount))

    res += math.prod(cube_max.values())

print(res)

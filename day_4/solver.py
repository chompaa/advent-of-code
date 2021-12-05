from itertools import chain
from copy import deepcopy

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

numbers = lines[0].split(",")
numbers = [int(num) for num in numbers]
boards = list(filter(None, lines[1:]))
boards = [list(row) for row in zip(*[boards[n::5] for n in range(5)])]
boards = [[row.split() for row in board] for board in boards]
boards = [[list(map(int, row)) for row in board] for board in boards]

# day 1

win_vars = 0, 0
found = False
_boards = deepcopy(boards)

for num in numbers:
    for i in range(len(_boards)):
        for j in range(len(_boards[0])):
            for k in range(len(_boards[0][0])):
                if _boards[i][j][k] == num:
                    _boards[i][j][k] = -1

    for i in range(len(boards)):
        for j in range(len(_boards[0])):
            if _boards[i][j].count(-1) == 5:
                win_vars = i, num
                found = True
                break

            if sum(list(zip(*_boards[i]))[j]) == -5:
                win_vars = i, num
                found = True
                break
        else:
            continue
        break
    else:
        continue
    break

board_num, winning_num = win_vars
board_sum = sum(filter(lambda x: x != -1, chain.from_iterable(_boards[board_num])))
print(board_sum * winning_num)

# day 2

win_vars = 0, 0
found = False

for num in numbers:
    if found:
        break

    for i in range(len(boards)):
        for j in range(len(boards[0])):
            for k in range(len(boards[0][0])):
                if boards[i][j][k] == num:
                    boards[i][j][k] = -1

    queue = []
    for i in range(len(boards)):
        for j in range(len(boards[0])):
            if boards[i][j].count(-1) == 5:
                if len(boards) > 1:
                    queue.append(boards[i])
                else:
                    win_vars = i, num
                    found = True
                    break

            if sum(list(zip(*boards[i]))[j]) == -5:
                if len(boards) > 1:
                    queue.append(boards[i])
                else:
                    win_vars = i, num
                    found = True
                    break
        else:
            continue
        break

    for board in queue:
        try:
            boards.remove(board)
        except ValueError:
            pass

board_num, winning_num = win_vars
board_sum = sum(filter(lambda x: x != -1, chain.from_iterable(boards[board_num])))
print(board_sum * winning_num)

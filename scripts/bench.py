import os
import re
import sys
import timeit


def time_solver(year: int, day: int, n: int = 1000) -> tuple[float]:
    """
    Times the solver for the specified year and day, with a specified number of runs.

    Args:
        year (int): The year.
        day (int): The day.
        n (int): The number of runs.

    Returns:
        tuple[float]: The times for part 1 and part 2.

    Raises:
        FileNotFoundError: If the solver file does not exist.
    """

    os.chdir(f"./{year}/{day:02d}/")

    solver = open("solver.py").read()
    solver = re.split(r"^# part \d$", solver, flags=re.MULTILINE)

    setup, p_1, p_2 = solver

    p_1_time = timeit.timeit(stmt=p_1, setup=setup, globals=globals(), number=n) / n
    p_2_time = timeit.timeit(stmt=p_2, setup=setup, globals=globals(), number=n) / n

    times = (p_1_time, p_2_time)

    # convert times to milliseconds
    times = tuple(f"{time * (10**3):.2f}ms" for time in times)

    # be sure to go back to the root directory
    os.chdir("../../")

    return times

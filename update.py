import os
import re
import sys
import timeit

import requests

import util


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

    os.chdir(f"./{year}/day{day:02d}/")

    solver = open("solver.py").read()
    solver = re.split(r"^# part \d$", solver, flags=re.MULTILINE)

    setup, p_1, p_2 = solver

    p_1_time = timeit.Timer(stmt=p_1, setup=setup, globals=globals())
    p_2_time = timeit.Timer(stmt=p_2, setup=setup, globals=globals())

    times = (p_1_time.timeit(number=n) / n, p_2_time.timeit(number=n) / n)

    # convert times to microseconds
    times = tuple(f"{time * (10**6):.2f}µs" for time in times)

    #  be sure to go back to the root directory
    os.chdir("../../")

    return times


def update_readme(year: int, day: int, stars: int = 2, time: bool = True) -> None:
    """
    Updates the README.md file with the specified year, day, and number of stars.

    Args:
        year (int): The year.
        day (int): The day.
        stars (int): The number of stars.

    Returns:
        None

    Raises:
        RuntimeError: If the day is less than 1.
        RuntimeError: If the URL cannot be fetched.
        RuntimeError: If the request to fetch the title fails.
        RuntimeError: If the day already exists in README.md.
    """

    if day <= 1:
        raise RuntimeError("Day must be greater than 1")

    url = f"https://www.adventofcode.com/{year}/day/{day}"

    # don't bother if the day already exists
    with open("README.md", "r", encoding="utf8") as f:
        lines = f.readlines()

        for line in lines:
            if url in line:
                raise RuntimeError(f"Day {day} already exists in README")

    session_id = util.get_session_id()

    response = requests.get(
        url,
        headers={"User-Agent": "github.com/chompaa"},
        cookies={"session": session_id},
    )

    if not response.ok:
        raise RuntimeError(f"Failed to fetch URL: {response.reason}")

    # this is a bit hacky, but i don't want to use a html parser :)
    title = next(
        (
            line.split("---")[1][7 + len(str(day)) :].strip()
            for line in response.text.split("\n")
            if f"Day {day}:" in line
        ),
        "",
    )

    if not title:
        raise RuntimeError("Failed to fetch title")

    p_1_time, p_2_time = time_solver(year, day) if time else ("null", "null")

    entry = [
        "\t<tr>\n",
        f"\t\t<td><a href='{url}'>{day:02d} - {title}</a></td>\n",
        f"\t\t<td>{'⭐' * stars}</td>\n",
        f"\t\t<td><code>{p_1_time}</code></td>\n",
        f"\t\t<td><code>{p_2_time}</code></td>\n",
        f"\t</tr>\n",
    ]

    with open("README.md", "r+", encoding="utf8") as f:
        lines = f.readlines()

        for idx, line in enumerate(lines):
            if url.replace(f"day/{day}", f"day/{day - 1}") in line:
                offset = idx + len(entry) - 1

                lines[offset:offset] = entry

        f.seek(0)
        f.writelines(lines)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: update.py <year> <day>")
        sys.exit(1)

    year = int(sys.argv[1])
    day = int(sys.argv[2])

    update_readme(year, day)

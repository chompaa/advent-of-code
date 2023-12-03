import os.path
import shutil
import sys

import requests


def get_session_id() -> str:
    """
    Returns the session ID from the "session.cookie" file.

    Returns:
        str: The session ID.
    """

    with open("session.cookie", "r") as f:
        return f.read().strip()


def make_input(year: int, day: int, path: str) -> None:
    """
    Fetches the input for the specified year and day from the Advent of Code
    website and saves it to the specified path.

    Args:
        year (int): The year.
        day (int): The day.
        path (str): The path to save the input file.

    Raises:
        RuntimeError: If the request to fetch the input fails.

    Returns:
        None
    """

    session_id = get_session_id()

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    response = requests.get(
        url,
        headers={"User-Agent": "github.com/chompaa"},
        cookies={"session": session_id},
    )

    if not response.ok:
        raise RuntimeError(f"Failed to fetch input: {response.reason}")

    with open(f"{path}/input.txt", "w") as f:
        f.write(response.text[:-1])


def make_files(year, day) -> None:
    """
    Creates the necessary files and directories for the specified year and day
    of the Advent of Code challenge.

    Args:
        year (int): The year.
        day (int): The day.

    Returns:
        None
    """

    path = f"./{year}/day{day:02d}/"

    # make directories
    os.makedirs(path, exist_ok=True)

    if not os.path.isfile(f"{path}/solver.py"):
        # make solver file
        shutil.copyfile("./solver.tmp", f"{path}/solver.py")

    if not os.path.isfile(f"{path}/example.txt"):
        # make example file
        open(f"{path}/example.txt", "w").close()

    # make input file
    make_input(year, day, path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: make.py <year> <day>")
        sys.exit(1)

    year = int(sys.argv[1])
    day = int(sys.argv[2])

    make_files(year, day)

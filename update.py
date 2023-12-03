import sys

import requests

import util


def update_readme(year: int, day: int, stars: int) -> None:
    """
    Updates the README.md file with the specified year and day.

    Args:
        year (int): The year.
        day (int): The day.

    Returns:
        None
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

    with open("README.md", "r+", encoding="utf8") as f:
        lines = f.readlines()

        for idx, line in enumerate(lines):
            if url.replace(f"day/{day}", f"day/{day - 1}") in line:
                entry = [f"| [{day:02d} - {title}]({url}) | {'⭐' * stars} |\n"]
                lines = lines[: idx + 1] + entry + lines[idx + 1 :]

        f.seek(0)
        f.writelines(lines)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: update.py <year> <day> <stars>")
        sys.exit(1)

    year = int(sys.argv[1])
    day = int(sys.argv[2])
    stars = int(sys.argv[3])

    update_readme(year, day, stars)

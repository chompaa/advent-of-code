import sys


def use(year: int, day: int) -> None:
    with open(".env", "w") as f:
        f.write(f"DAY={year}/{day:02d}\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: use.py <year> <day>")
        sys.exit(1)

    year = int(sys.argv[1])
    day = int(sys.argv[2])

    use(year, day)

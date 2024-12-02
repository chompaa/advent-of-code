set dotenv-load

year := "2024"

alias m := make
alias u := use
alias t := test
alias r := run

make day:
  python3 scripts/make.py {{year}} {{day}}
  python3 scripts/use.py {{year}} {{day}}

use day:
  python3 scripts/use.py {{year}} {{day}}

test:
  python3 $DAY/solver.py < $DAY/example.txt

run:
  python3 $DAY/solver.py < $DAY/input.txt

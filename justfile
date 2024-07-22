set dotenv-load

year := "2023"

alias m := make
alias u := use
alias t := test
alias r := run

make day:
  python scripts/make.py {{day}}
  use

use day:
  python scripts/use.py {{year}} {{day}}

test:
  python $DAY/solver.py < $DAY/example.txt

run:
  python $DAY/solver.py < $DAY/input.txt

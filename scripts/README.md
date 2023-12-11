# Scripts

## `make.py`

I use the `make.py` script to make my directories and download my inputs
automatically. To use this, create a file called `session.cookie` in the root directory, and place your session cookie ID inside. Then, you can run:

```shell
python scripts/make.py <year> <day>
```

to create the directory structure. Note that files will not be overwritten, with
the exception of `input.txt`.

## `update.py`

The `update.py` script adds the challenge day to the root README and times the
solver.

The timer will look for two strings (case-sensitive): "# part 1" and
"# part 2". Everything below each part will be interpreted as code to be timed.
The rest will be used as setup.

There also needs to exist at least one day already, i.e. you need to setup the
table with at least one entry first. You also require a `session.cookie` file to
run this if you wish. It can be run using:

```shell
python scripts/update.py <year> <day>
```

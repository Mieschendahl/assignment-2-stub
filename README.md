# Assignment 2

## Task

Your task is to create a real compiler for a subset
of Python, the L_var language. For this, refer
to exercises 2-7 from the [course book](https://github.com/IUCompilerCourse/Essentials-of-Compilation). **IMPORTANT NOTE: In the newest
version of the book, L_var includes binary
subtraction, i.e. `exp - exp`. Your compiler
should support this, too.**

## Setup

```sh
pip3.10 install -r requirements.txt
```

You may need to get pip3.10 first:

```sh
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
```

## Testing

```sh
python3.10 run-tests.py
```

Test cases can be found in the `tests/var` directory.
Feel free to add your own tests. `.py` files are the
program to compile, `.in` the input, `.golden` the expected
output.


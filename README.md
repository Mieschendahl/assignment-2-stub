# Assignment 2

## Task

Your task is to create a real compiler for a subset
of Python, the L_var language. The concrete syntax of
L_var is defined as follows:

* `exp ::= int | input_int() | - exp | exp + exp | var`
* `stmt ::= print(exp) | exp | var = exp`
* `L_var = stmt*`

The abstract syntax of L_var:

* `exp ::= Constant(int) | Call(Name('input_int'),[]) | UnaryOp(USub(),exp) | BinOp(Add(),exp,exp) | Name(var)`
* `stmt ::= Expr(Call(Name('print'),[exp])) | Expr(exp) | Assign([Name(var)], exp)`
* `L_var ::= Module(stmt*)`

Your target language is x86.

## TODO MORE

## Setup

```sh
pip3.10 install -r requirements.txt
```

You may need to get pip3.10 first:

```sh
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
```

## Testing

Test cases can be found in the `tests/var` directory.
Feel free to add your own tests. `.py` files are the
program to compile, `.in` the input, `.golden` the expected
output.

```sh
python3.10 run-tests.py
```

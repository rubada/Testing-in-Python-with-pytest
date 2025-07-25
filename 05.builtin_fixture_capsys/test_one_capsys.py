# "capsys" Built-In Fixture:
# When running tests, pytest captures the stdout (standard output) and stderr
# (standard error) by default.

# For more information about "stdout" and "stderr", check out the
# "05. Python "stdin", "stdout", and "stderr" playlist in "Miscellaneous
# Subjects in Python" part in "@Intuidemy".

# One primary benefit of the default capturing of stdout/stderr output is that
# you can use print statements for debugging:

import sys
from os.path import dirname, join, abspath

sys.path.append(abspath(join(dirname(__file__), "../")))

from modules.mathoperations import MathOperations as mp
import pytest


# There is a setup function, to execute the "stdout" this function name is
# "setup_function".
# def setup_function(function):
#     print(f"This function failed {function.__name__}")


# def test_passed():
#     assert mp.addition(2, 3) == 5


# def test_failed():
#     assert mp.addition(2, 3) == 5


# How to access captured output from a test function?
# The "capsys", fixture can access the stdout/stderr output created during
# test execution.
def division(x, y):
    try:
        print(mp.division(x, y))
    except ZeroDivisionError:
        print("Division by Zero", file=sys.stderr)


@pytest.mark.parametrize("x, y, result", [(3, 1, "3.0"),
                                          (4, 0, "Division by Zero")])
def test_stdout(capsys, x, y, result):

    division(x, y)

    capture_std = capsys.readouterr()  # Capture stdout and stderr

    if result != "Division by Zero":
        assert capture_std.out.strip() == result
    else:
        assert capture_std.err.strip() == result


# There are also the "capsysbinary", "capfd", and "capfdbinary" fixtures,
# do the same thing as "capsys"
# "capsysbinary": Captures binary output sent to stdout and stderr for
# assertions.
# "capfd: Captures text output even if output (stdout and sterr) is redirected
# to a file descriptor.
# "capfdbinary": Captures binary output even if output (stdout and sterr) is
# redirected to a file descriptor.


# Why "capsys"  fixture is used:
# 1. Used to capture and assert text output printed to the console, as shown
# in the previous example.

# 2. Used to verify error messages or logging output, as shown in the previous
# example

# 3. Used with test functions that print results instead of returning them.

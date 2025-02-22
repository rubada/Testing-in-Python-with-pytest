# check page 24 and 25 in the book
# pytest:
# It is a third-party package that needs to be installed:
# pip install pytest

import math


# Let's take an example:
def add(x, y):
    return x + y


# Test files should be named test_<name>.py or <name>_test.py.
# Test methods and functions should be named test_<name>.
# Test classes should be named Test<name>.
# def test_add():
#     assert add(2, 3) == 5


# Using assert statements:
# In "pytest" assert statement is your main tool to communicate test failure.
# This is simple and efficient. This is why "pytest" is wide use by many
# developers over other frameworks.

# "pytest" Vs "unittest",
#
#          unittest                         pytest
#      assertEqual(x, y)                 assert x == y
#      assertNotEqual(x, y)              assert x != y
#            .....                          .....

# "unittest" has many methods to do assertion.
# With pytest, you can use assert statement with any expression, if the
# expression would evaluate to False or True (Boolean), the test would fail
# or pass.

# "pytest" supports running "unittest" test cases.

# def test_pow():
#     test1 = math.pow(3, 2)
#     test2 = 9
#     assert test1 != test2


# def test_dist():
#     test1 = math.dist((1, 2), (3, 4))
#     test2 = 1
#     assert test1 >= test2


# To run a test file type the following line in the termainal
# pytest .\01.creating_tests\test_one.py

# Or to run all the tests just type:
# pytest

def test_passed():
    assert [3, 5, 2] == [3, 5, 2]


def test_failed():
    print("Start testing")
    assert [1, 5, 2] == [3, 5, 2]


# To run a detailed test use Verbose mode "-v":
# pytest -v .\01.creating_tests\test_one.py
# for a more detailed test use "-vv"

# The detailed test add:
# "-" Shows the expected value.
# "+" Shows the actual value.
# "?" Points to the difference between the expected and actual values.
# "^" to show you where your code is failed.


# to show print output during test run use -s:
# pytest -v -s .\01.creating_tests\test_one.py

# To run a test on a specific test:
# pytest .\01.creating_tests\test_one.py::test_failed

# To run specific tests according to their names, you can use -k option,
# as follows:
# pytest -v -k <name>
# The above will run all the tests that have <name> in their name.
# "or", "and", and "not" can be used, such as:
# pytest -v -k <name1 or name2> ----> this will run both tests or one of them
# pytest -v -k <name1 and name2> ----> this will run both tests only
# pytest -v -k <not name1> ----> this will run all tests except name1
# pytest -v -k <name1 and not name2> ----> Runs tests with name1 and excludes
# those with name2.
# You can add whatever logic you want.


# Here are the possible outcomes of a test function:
# PASSED (.): The test ran successfully.
# FAILED (F): The test did not run successfully.
# SKIPPED (s): The test was skipped.
# XPASS (X): The test was not supposed to pass, ran, and passed.
# ERROR (E): The test raised an unexpected exception.

# Check "pytest --help" to learn all the options you can add with pytest in
# the command line.

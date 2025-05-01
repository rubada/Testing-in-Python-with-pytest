# Setup and Teardown in pytest
# To create a setup and teardown in pytest, follow these steps:
# 1. Create a pytest fixture
# 2. Use the yield keyword to separate the setup code (before yield) from the
# teardown code (after yield).
# Let's take an example:

import pytest
from os.path import dirname, join


@pytest.fixture
def setup_teardown():
    print("\nSetup the resources")
    resources = {"x": 2, "y": 3}
    yield resources
    print("\nTeardown the resources")


def add(x, y):
    return x + y


def test_add(setup_teardown):
    assert add(**setup_teardown) == 5

# To run the test we will use the following:
# pytest -v -s
# To print the "print" statement in the fixture.

# Let's take another example:

# 1. We created the function to test, which converted data to float numbers:
# def to_float(data):
#     try:
#         float_numbers = list(map(float, data))
#         return float_numbers

#     except ValueError:
#         raise ValueError("Data items should be numbers, not strings")


# # 3. Create the fixture that open a file and use it as a parameter in
# # "to_float" function:

# @pytest.fixture
# def open_file():
#     script_dir = dirname(__file__)
#     path_text = join(script_dir, "my_text.txt")

#     file = open(path_text)
#     data = file.readlines()
#     yield data
#     file.close()


# # 4. Create the test function:
# def test_exception(open_file):
#     try:
#         to_float(open_file)
#     except ValueError as e:
#         assert str(e) == "Data items should be numbers, not strings"


# pytest provides a command-line flag, "--setup-show", which is used to
# display information about the setup and teardown of fixtures during
# a test run.

# pytest --setup-show <file-name>

# F refers to the fixture scope, which is a function scope.
# Fixture scopes will be discussed later.

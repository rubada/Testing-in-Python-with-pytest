# Mocking in pytest.
# Mocking in pytest is a technique used to simulate objects, functions, or
# behaviors during testing. It allows you to isolate the code being tested
# from its dependencies, such as databases or external APIs, making tests more
# predictable and focused.

# Moking objects are used used to simulate the behavior of objects to:
# 1. Allow your test to verify that the code under test behaves correctly
# under different circumstances.
# 2. Eliminate the need for expensive operations, making tests faster.
# For example, if you want to do an API call (real connection) during testing,
# the test may take longer to run, slowing your test execution.

# To use moking technique in pytest we should install "pytest-mock" plugin in
# our virtual environment
# pip install pytest-mock

# The "mocker" fixture is used from "pytest-mock" plugin to create a mocking
# object, and it is related to "unittest.mock" module, as it builds upon its
# functionality (such as Mock, MagicMock, patch) to offer a more integrated
# and convenient experience for testing in Python.


# Let's take an example:
from my_functions import remove_file, create_file
import sys
from os.path import dirname, join, abspath

sys.path.append(abspath(join(dirname(__file__), "../")))
from modules import mathoperations as mp


# Testing the "os.remove" function without actually deleting a file from the
# disk, we will use the "mocker.patch" method to simulate the os.remove
# function.
# This is done by using the "mocker" fixture:
# def test_remove_file(mocker):

#     mocker.patch("os.remove")

#     # Calling the function under test, it will use the mocked function
#     # instead of the actual one.
#     remove_file("file")

#     # The "assert_called_once_with" method is used to validate that the
#     # os.remove function was called through the function:
#     os.remove.assert_called_once_with("file")


# let's take another example:

def test_create_file(mocker):
    # The "mocker.mock_open" method creates a mock object for the "open"
    # function, this allows to simulate file operations (like reading and
    # writing) without interacting with the actual filesystem.
    mock_file = mocker.mock_open()

    # Simulate the open function using "builtins.open" because the "open"
    # function is a built-in function in Python:
    mocker.patch("builtins.open", mock_file)

    # Calling the function under test, it will use the moked function instead
    # of the actual one.
    create_file("example.txt", "Testing write mode")

    # Verify that the "open" function was called with the expected arguments.
    mock_file.assert_called_once_with("example.txt", "w")

    # Verify the write mode was called with the correct data
    mock_file().write.assert_called_once_with("Testing write mode")


# The "moker" fixture supported methods are:

# mocker.patch: we talked about in the previous example.
# mocker.patch.object: patch a method or attribute or method of an object in
# your tests
# mocker.patch.multiple: patch multiple attributes, methods or functions at
# once.
# mocker.patch.dict: patch a dictionary.
# mocker.stopall: stop all patches.
# mocker.stop: stop a specific mock object.

# For more information about pytest-mock methods, check below link:
# https://pytest-mock.readthedocs.io/en/latest/usage.html#usage


# Let's take an example on mocker.patch.object:
def test_addition_method(mocker):

    mathop = mp.MathOperations()
    mock_response = 7

    # Patch the method
    mocker.patch.object(mathop, "addition", return_value=mock_response)

    assert mathop.addition(1, 8) == mock_response

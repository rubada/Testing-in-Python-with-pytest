# "autouse" fixture parameter:
# A fixture with the autouse parameter set to True is automatically applied
# to all tests within its scope, without requiring to add the fixture in
# the test functions or classes as a parameter.

# Let's take example:

import pytest
from os.path import dirname, join, exists, getsize


# @pytest.fixture(autouse=True)
# def fixture_with_autouse():
#     print("\nSetup connection")
#     yield
#     print("\nTeardown connection")


# def test_connection_one():
#     print("Running test_connection_one")
#     assert True


# def test_connection_two():
#     print("Running test_connection_two")
#     assert True


# Let's take another example, that we want to test if
# a file path exists, and check out the file size:

class FileSizeError(Exception):
    pass


def read_file(file_path, max_size):
    if not exists(file_path):
        raise FileExistsError("The file doesn't exist")
    if getsize(file_path) > max_size:
        raise FileSizeError(f"The file size must be less than {max_size}")
    with open(file_path, "r") as file:
        return file.read()


@pytest.fixture(autouse=True)
def check_file_path():
    # Make the file_path parameter accessible for all tests
    # when using the "global" keyword with autouse is true.
    global file_path
    script_dir = dirname(__file__)
    file_path = join(script_dir, "text3.txt")
    yield file_path
    print("Teardown is Completed")


def test_FileExistsError():
    file_size = 1000
    try:
        read_file(file_path, file_size)
    except FileExistsError as e:
        assert str(e) == "The file doesn't exist"


def test_FileSize():
    file_size = 1000
    try:
        read_file(file_path, file_size)
    except FileSizeError as e:
        assert str(e) == f"The file size must be less than {file_size}"

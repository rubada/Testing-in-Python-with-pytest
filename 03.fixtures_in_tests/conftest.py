# How do we share fixtures among different test files?
# As shown before we can define fixtures within the test file, but to share
# fixtures with multiple test files, you need to use the "conftest.py" file.
# By using the "conftest.py" file you can call your fixtures from different
# Python files.

# The directory where the "conftest.py" should be created, depends on your
# project, for example:
# 1. Having multiple test directories in the project root directory, and both
# tests use the same fixtures you can add the "conftest.py" in the root
# directory.

# main_project/
# ├── conftest.py               Fixtures available to all tests
# ├── test1/
# ├── test2/
# └── project/

# 2. In the test directory, to share fixtures between test files in the test
# directory and subdirectories:

# main_project/
# ├── test/
# │   ├── conftest.py           Fixtures available to tests directory
# |   |                         and its subdirectories
# │   ├── test_file1.py
# │   ├── subdir/
# │   │   ├── test_file2.py
# │   │   └── test_file3.py
# └── project/

# 3. In the subdirectories of the test directory, if the tests have different
# fixtures.

# main_project/
# ├── test/
# │   ├── ......
# │   ├── subdir1/
# │   |   ├── conftest.py        Fixtures available to subdir1
# │   │   ├── test_file2.py
# │   │   └── test_file3.py
# │   ├── subdir2/
# │   |   ├── conftest.py        Fixtures available to subdir2
# │   │   ├── test_file4.py
# │   │   └── test_file5.py
# └── project/
import pytest


@pytest.fixture
def add_data():
    data = {"x": 2, "y": 3}
    return data


# We can use multiple fixtures in the conftest.py file
@pytest.fixture
def sub_data():
    data = {"x": 5, "y": 4}
    return data

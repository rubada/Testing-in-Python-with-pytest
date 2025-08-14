import pytest
from add_sub import addition, subtraction
from mult_div import multiplication, division


# "doctest_namespace" is a standard dict object into which you place the
# objects you want to appear in the doctest namespace
@pytest.fixture()
def addition_function(doctest_namespace):
    doctest_namespace["add"] = addition


@pytest.fixture()
def subtraction_function(doctest_namespace):
    doctest_namespace["sub"] = subtraction


@pytest.fixture()
def multiply_function(doctest_namespace):
    doctest_namespace["multiply"] = multiplication


@pytest.fixture()
def division_function(doctest_namespace):
    doctest_namespace["division"] = division

# Note: the "conftest.py" needs to be in the same directory tree where your
# doctest with your source code is in. Otherwise your fixtures will not be
# discovered.
# my_project/
# ├── src/
# │   ├── my_module.py
# │   ├── conftest.py

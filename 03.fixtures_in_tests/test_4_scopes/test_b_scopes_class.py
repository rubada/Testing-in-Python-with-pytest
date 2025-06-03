# Fixtures Scopes:
# A fixture has a scope parameter.
# Scopes control the lifetime of a fixture which means controlling how often a
# fixture gets set up and torn down.

# pytest provides four types of scopes:
# 2. scope="class"
# It is used when you want to run a fixture on multiple test methods, which
# means the setup and teardown are run once for each test class.

# Let's take an example:
import pytest
from os.path import dirname, join
from operator import truediv


def to_float_divide_by(data, number):
    try:
        float_numbers = list(map(float, data))
        nums_list = [number] * len(float_numbers)
        nums_divide_by = list(map(truediv, float_numbers, nums_list))
        return nums_divide_by

    except ValueError:
        raise ValueError("Text file lines should be numbers, no strings")
    except ZeroDivisionError:
        raise ZeroDivisionError("Don't divide by zero")


@pytest.fixture(scope="class")
def open_file():
    script_dir = dirname(__file__)
    file1 = open(join(script_dir, "text1.txt"))
    data1 = file1.readlines()
    file2 = open(join(script_dir, "text2.txt"))
    data2 = file2.readlines()
    yield data1, data2
    file1.close()
    file2.close()


class TestExcep:

    def test_valueerror(self, open_file):
        try:
            to_float_divide_by(open_file[0], 3)
        except ValueError as e:
            assert str(e) == "Text file lines should be numbers, no strings"

    def test_divide_zero(self, open_file):
        try:
            to_float_divide_by(open_file[1], 0)
        except ZeroDivisionError as e:
            assert str(e) == "Don't divide by zero"


# when running the test using the "pytest --setup-show <file-name>", it will
# show the letter "C", which refers to the "class" scope.

# As mentioned before you add all your fixtures in the conttest.py file to
# share among different test files.

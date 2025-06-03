# Fixtures Scopes:
# A fixture has a scope parameter.
# Scopes control the lifetime of a fixture which means controlling how often a
# fixture gets set up and torn down.

# pytest provides four types of scopes:
# 4. scope="session"
# It is used when you want to run a fixture on multiple test functions or
# classes, which means the setup and teardown are run once for each test
# session.

# Here I added the fixture in the conftest.py to use it with multple test
# files.

# Let's take an example:

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
# show the letter "S", which refers to the "session" scope.

# pytest --setup-show <file1-name> <file2-name>

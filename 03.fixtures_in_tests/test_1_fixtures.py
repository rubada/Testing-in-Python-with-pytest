# What are pytest fixtures?
# Fixtures in pytest are powerful tools that are used:
# 1. To setup and teardown resources needed for your tests.
# The setup and teardown operations will be discussed later in detail.

# 2. Fixtures simplify writing tests by allowing code reuse across multiple
# tests.

# 3. Fixtures are used to provide the data required in our tests.

# Let's take an example:

import pytest


# Add the fixture decorator before your function:
# @pytest.fixture
# def create_data():
#     return "This is a fixture"


# def test_fix(create_data):
#     assert create_data == "This is a fixture"


# Fixtures are a great to store data to use for testing.
# And as mentioned above fixtures can be used with multiple tests.
# Let's take an example:
# def add(x, y):
#     return x + y


# @pytest.fixture
# def add_data():
#     data = {"x": 2, "y": 3}
#     return data


# def test_add(add_data):
#     assert add(**add_data) == 5


# Intialize objects:
class AddSub:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y


@pytest.fixture
def add_sub_obj():
    return AddSub(5, 6)


def test_add(add_sub_obj):
    assert add_sub_obj.add() == 11


def test_sub(add_sub_obj):
    assert add_sub_obj.sub() == -1

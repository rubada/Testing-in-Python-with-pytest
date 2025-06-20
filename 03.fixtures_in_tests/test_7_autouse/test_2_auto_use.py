# We discussed how to use multiple fixtures in a test, also fixtures can be
# requested by other fixtures.

import pytest


# @pytest.fixture
# def new_data():
#     return ["Mary", "five123"]


# @pytest.fixture
# def stored_data():
#     return {"user": ["John"], "password": ["hello"]}


# # Request more than one fixture at a time:
# @pytest.fixture
# def combine_data(stored_data, new_data):
#     stored_data["user"].append(new_data[0])
#     stored_data["password"].append(new_data[1])
#     return stored_data


# def test_final_settings(combine_data):
#     assert combine_data == {"user": ["John", "Mary"],
#                             "password": ["hello", "five123"]}


# def test_final_settings(combine_data, stored_data):
#     assert stored_data == {"user": ["John", "Mary"],
#                            "password": ["hello", "five123"]}


# Using "autouse" fixture parameter:
@pytest.fixture
def new_data():
    return ["Mary", "five123"]


@pytest.fixture
def stored_data():
    return {"user": ["John"], "password": ["hello"]}


@pytest.fixture(autouse=True)
def combine_data(stored_data, new_data):
    stored_data["user"].append(new_data[0])
    stored_data["password"].append(new_data[1])
    return stored_data


def test_final_settings(stored_data):
    assert stored_data == {"user": ["John", "Mary"],
                           "password": ["hello", "five123"]}


# Note: you can use multiple fixtures in the test function or class more than
# once as mentioned before.

# Hook Functions:
# Hooks are a powerful feature in Pytest, which provide a way to customize and
# extend the behavior of Pytest.
# They allow you to customize and influence various aspects of test execution,
# reporting, and behavior.
# Pytest provides a set of built-in hooks, and you can also create your custom
# hooks.

# Some of the Pytest hooks functions:
# pytest_runtest_setup(item): Called or invoked before each test is run, used
# to set up test environments.

# pytest_collection_modifyitems(session, config, items): Called after
# collection has been performed.
# Let's you filter or reorder test items during test collection.

# pytest_configure(config): Let's you perform initial configuration on pytest,
# it is called after command-line options have been parsed.

# pytest_runtest_teardown: Called after a test item’s teardown method is
# invoked. It allows you to perform additional cleanup or customization.

# Pytest docs link for all pytest built-in hooks functions:
# https://docs.pytest.org/en/stable/reference/reference.html#hooks

# The hooks functions should be added in the conftest.py file.

# Pytest docs link for writing a hook function:
# https://docs.pytest.org/en/stable/how-to/writing_hook_functions.html#writing-hook-functions

# Pytest link for declaring new hooks:
# https://docs.pytest.org/en/stable/how-to/writing_hook_functions.html#declaringhooks

# Let's take an example:
import pytest


# def test_add():
#     assert 2 + 3 == 5


@pytest.mark.connect_database
def test_with_database():
    assert True


@pytest.mark.get_data
def test_get_data_db():
    assert True

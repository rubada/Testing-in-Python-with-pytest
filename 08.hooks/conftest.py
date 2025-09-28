import pytest
# "pytest_report_header"
# Return a string or list of strings to be displayed as header info for
# terminal reporting.


# def pytest_report_header():
#     return "Hello, this test is executed by Pytest"


def pytest_runtest_setup(item):
    print(f"Setting up the test: {item.name}")

    if "connect_database" in item.keywords:
        pytest.skip("Connecting to the test database is skipped")

    elif "get_data" in item.keywords:
        pytest.skip("Skipping getting data.")

# @pytest.hookimpl() decorator:
# This decorator is used to mark a function as an implementation of
# a pytest hook.
# It is used to override or extend the behavior of one of the hooks,
# using the following parameters:
# 1. @pytest.hookimpl(tryfirst=True)
# Makes decorated hook functions with "tryfirst=True" executes earlier than
# others.

# 2. @pytest.hookimpl(trylast=True)
# Makes decorated hook functions with "trylast=True" executes last in the
# the sequence.

# 3. @pytest.hookimpl(hookwrapper=True)
# Hook wrappers allow you to perform additional actions before and after the
# execution of other hook implementations.
# The hook function that has this decorator should use the "yield" keyword:
# a. The code before the yield statement is the code that runs before other
# hook implementations.
# b. The yield statement will allow pytest to run other implementations of
# the same hook.
# c. The code after the yield statement is the code that runs after other hook
# implementations.

# 1st case:
# @pytest.hookimpl(tryfirst=True)
# def pytest_runtest_setup(items):
#     # will execute as early as possible
#     pass


# 2nd case:
# @pytest.hookimpl(trylast=True)
# def pytest_runtest_setup():
#     # will execute as late as possible
#     pass


# 3rd case:
# @pytest.hookimpl(wrapper=True)
# def pytest_runtest_setup(items):

#     # will execute before the tryfirst one

#     yield "Code here"

#     # will execute after all hooks are executed

# Note: The above function are separate plugins or files, functions of the same
# name shouldn't be defined in the same script.

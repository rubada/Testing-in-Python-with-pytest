# What is "monkeypatch" built-in fixture in "pytest"?
# The monkeypatch built-in fixture in pytest is used for modifying attributes,
# dictionary items, environment variables, and even sys.path during tests.
# It allows you to safely override functionality without permanently affecting
# the codebase.

# All modifications made using monkeypatch are automatically undone after the
# test function completes, ensuring a clean test environment.

import my_func


# Several methods are used to do this:
# 1. monkeypatch.setattr(target: object,
#                        name: str,
#                        value: object,
#                        raising: bool=True)

# Let's take an example:
# def test_my_string(monkeypatch):
#     monkeypatch.setattr(my_func, "my_string", lambda: "Hello, Python")
#     assert my_func.my_string() == "Hello, Python"


# Another way to define a function, without using lambda:
# def test_my_string(monkeypatch):
#     def mock_func():
#         return "Hello, Python"
#     monkeypatch.setattr(my_func, "my_string", mock_func)
#     assert my_func.my_string() == "Hello, Python"

# Common Cases where "monkeypatch.setattr" is used:
# a. Along with functions "monkeypatch.setattr" can be used with classes
# attributes or methods, to replace attributes or methods with a mock
# implementation to control their behavior during testing.

# b. Replace external connections, such as API requests, database queries, etc.
# with predefined responses to avoid making real connections during tests.

# Let's take an example:

# Mock "myfunc.get_user_data" function to replace "requests.get":
def mock_ext_data(id=1):
    return {"id": 1, "name": "John Doe"}


def test_request_user(monkeypatch):
    # Use monkeypatch to replace "requests.get":
    monkeypatch.setattr(my_func, "get_user_data", mock_ext_data)

    # Call the function that we want to test
    result = my_func.get_user_data(1)

    # Assert the result
    assert result == {"id": 1, "name": "John Doe"}

# Other "monkeypatct" methods:
# 2. monkeypatch.delattr(obj, name, raising=True)
# 3. monkeypatch.setitem(dic, name, value)
# 4. monkeypatch.delitem(obj, name, raising=True)
# 5. monkeypatch.setenv(name, value, prepend=None)
# 6. monkeypatch.delenv(name, raising=True)
# 7. monkeypatch.syspath_prepend(path)
# 8. monkeypatch.chdir(path)
# 9. monkeypatch.context()

# To learn more about these methods check out the below link in the
# "pytest" docs:
# https://docs.pytest.org/en/stable/how-to/monkeypatch.html

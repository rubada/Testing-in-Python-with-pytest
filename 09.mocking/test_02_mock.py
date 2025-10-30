# "mocker.Mock":
# "mocker.Mock" is a feature provided by pytest-mock that allows you to create
# mock objects easily within a pytest testing environment.
# You can create a mock object that behaves like a real one, but with
# controlled responses.
# Works smoothly within pytest, ensuring proper teardown after tests.

# Let's take an example:
from my_functions import get_user_data, APIClient
import requests


# def test_get_user_data(mocker):
#     # Create a mock response object:
#     mock_response = mocker.Mock()

#     # The "mocker.Mock()" object should invoke or call the method we are
#     # testing in our case "json" method.
#     # With the "mocker.Mock()" method "return_value", we can set the return
#     # value for the "json" method.
#     mock_response.json.return_value = {"id": 1,
#                                        "name":"Tom Scott",
#                                        "age": 28}

#     # Patch requests.get to return the mock response
#     mocker.patch("requests.get", return_value=mock_response)

#     # Call the function under test
#     user_data = get_user_data(1)

#     # This will validate or assert that the "requests.get" function is called
#     requests.get.assert_called_once_with("https://api.userdata.com/1")

#     # Verify that the mocked responce data:
#     assert user_data == {"id": 1,
#                          "name": "Tom Scott",
#                          "age": 28}


# Another example on testing a user defined class.

def test_api_client(mocker):

    # Create a mock instance
    mock_api = mocker.Mock(spec=APIClient)

    # Define the return value for get_data method:
    mock_api.get_data.return_value = {"id": 1,
                                      "name": "Tom Scott",
                                      "age": 28}

    # Call the mocked method
    response = mock_api.get_data(1)

    # Assertions
    assert response == {"id": 1,
                        "name": "Tom Scott",
                        "age": 28}


# Why use mocker.Mock()?
# Quick and flexible: It lets you create a mock object without needing
# a real class or function to base it on.
# Such as a generic mock to simulate a callback, a logger, or some external
# dependency that hasn’t been written yet.

# Useful for callbacks, event handlers, or dynamic behavior where you don’t
# care about enforcing a strict interface.

# Thus, if you just want a placeholder that accepts any call with any arguments
# and returns something without raise errors, mocker.Mock() is perfect.


# Differnces between `mocker.patch` and `mocker.Mock()`
# | Feature            | `mocker.patch`       | `mocker.Mock()`            |
# |--------------------|----------------------|----------------------------|
# | Purpose            | Replace existing     | Create a new mock object   |
# |                    | object in code       |                            |
# |                    |                      |                            |
# | Use case           | Mocking functions or | Simulating dependencies or |
# |                    | classes in modules   | callbacks                  |
# |                    |                      |                            |
# | Scope              | Temporary override   | Fully controlled by you    |
# |                    | during test          |                            |
# |                    |                      |                            |
# | Tied to real code? | Yes                  | Not necessarily            |

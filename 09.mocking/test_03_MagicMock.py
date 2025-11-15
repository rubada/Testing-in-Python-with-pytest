# "mocker.MagicMock"
# mocker.MagicMock is a subclass of Mock; the difference between "Mock" and
# "MagicMock" is:
# "Mock" can mock any object or function, but it does not automatically
# simulate magic methods, (Dunder Methods)
# "MagicMock" Automatically handles magic methods (Dunder Methods)

# As mentioned before, the "mock" module is related to "unittest.mock" module,
# in our example, we will use the "unittest.mock" to show the difference
# between "Mock" and "MagicMock":

from unittest.mock import Mock, MagicMock
from my_functions import APIClient, fetch_from_cache

mock1 = MagicMock()
# mock1 = Mock()
mock1.__iter__ .return_value = ['a', 'b', 'c']
# print(list(mock1))

mock2 = MagicMock()
# mock2 = Mock()
mock2.__str__ .return_value = "Hello"

# print(mock2)


# Let's take an example where "MagicMock" is used in testing:

# You can use it with user-defined methods:
# def test_api_client(mocker):

#     # Create a mock instance
#     mock_api = mocker.MagicMock(spec=APIClient)

#     # Define the return value for get_data method:
#     mock_api.get_data.return_value = {"status": "failed", "data": [42]}

#     # Call the mocked method
#     response = mock_api.get_data()
#     # Assertions
#     assert response == {"status": "failed", "data": [42]}


# Let's take another example.
# In this example, we will use the "side_effect" method instead of the
# "return_value".

# The side_effect attribute of a Mock or MagicMock object is a powerful tool
# for controlling how a mocked object behaves when called.

# Its purpose is to simulate various behaviors of a mocked object during
# testing, including:

# 1. Calling a function:
# You can assign a callable function to side_effect, with its return value
# becoming the mock's return value.
# 2. Returning different values on consecutive calls:
# You can assign an iterable to side_effect, and each call to the mock will
# return the next value from the iterable.
# 3. Raising exceptions:
# You can assign an exception class or instance to side_effect, and the mock
# will raise that exception when called.

# 1. A function to be called when the mock is called.
# class TestCache:

#     def test_cache_retrieval(self, mocker):
#         # Create a MagicMock that acts like a dictionary
#         mock_cache = mocker.MagicMock()

#         # Define behavior for __getitem__
#         mock_cache.__getitem__.side_effect = lambda key: f"Key is: {key}"

#         # Call the function with the mock
#         result = fetch_from_cache(mock_cache, "user_1232")

#         # Assertions
#         assert result == "Key is: user_123"


# 2. An iterable.
# def test_cache_retrieval_mult(mocker):
#     mock_cache = mocker.MagicMock()

#     mock_cache.__getitem__.side_effect = [
#         "user1",
#         "user2",
#         "user3"
#     ]

#     assert fetch_from_cache(mock_cache, "user2") == "user1"
#     assert fetch_from_cache(mock_cache, "user2") == "user2"
#     assert fetch_from_cache(mock_cache, "user3") == "user3"


# 3. An exception to be raised.
def test_cache_retrieval_error(mocker):
    mock_cache = mocker.MagicMock()

    mock_cache.__getitem__.side_effect = ValueError("Unvalid key")

    assert fetch_from_cache(mock_cache, "not key") == "Error: Unvalid key"

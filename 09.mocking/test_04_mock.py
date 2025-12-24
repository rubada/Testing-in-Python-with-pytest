# "spec" and "autospec" parameters:
# "spec" and "autospec" are options that help ensure your mock objects mimic
# the behavior of the objects they are replacing.

# 1. spec
# When you pass an object to the spec argument, the mock object will only
# allow attributes/methods that exist on the original object, this prevents
# you from accidentally calling or accessing attributes/methods that doesn't
# exist on the real object.

# Limitation: It doesn't enforce the correct signature for methods. You can
# call mocked methods with any arguments, even if the real method has a
# stricter signature.

# A stricter signature refers to a function or method definition that
# explicit and limited parameters, meaning it expects a specific number
# and type of arguments — and will raise an error if called incorrectly.

from my_functions import APIClient


# def test_greet_with_spec(mocker):
#     mock_greeter = mocker.Mock(spec=APIClient)

#     id1 = {"id": 1,
#            "name": "Tom Scott",
#            "age": 28}

# #     id2 = {"id": 2,
# #            "name": "Mary Davis",
# #            "age": 35}

# #     mock_greeter.get_data(id1)
# #     mock_greeter.get_data(id1, id2)
#     mock_greeter.hello(id1)

# #     mock_greeter.get_data.assert_called_with(id1)
# #     mock_greeter.get_data.assert_called_with(id1, id2)
#     mock_greeter.hello.assert_called_with(id1)


# 2. autospec
# "autospec" is stricter than spec. It not only limits the mock to the
# attributes and methods of the original object but also enforces the
# correct method signatures. This ensures that mocked methods can only be
# called with arguments that match the real method's signature.
# How to use: You can pass autospec=True to patch or use create_autospec() to
# create a mock with this behavior.
# Benefit: It provides better safety and accuracy in your tests.

def test_greet_with_autospec(mocker):
    mock_greeter = mocker.patch('my_functions.APIClient', autospec=True)

    id1 = {"id": 1,
           "name": "Tom Scott",
           "age": 28}

    id2 = {"id": 2,
           "name": "Mary Davis",
           "age": 35}

#     mock_greeter.get_data(id1)
    mock_greeter.get_data(id1, id2)

#     mock_greeter.get_data.assert_called_with(id1)
    mock_greeter.get_data.assert_called_with(id1, id2)

# ✅ When to use which?
# - Use spec when you want basic attribute/method validation.
# - Use autospec when you want stricter signature mocks, especially
# useful for catching bugs.

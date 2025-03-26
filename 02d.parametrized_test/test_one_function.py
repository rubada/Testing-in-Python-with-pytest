# How do you add parameters to a test?
# It is done by using the "parametrize" marking, as follows:
# @pytest.mark.parametrize(argnames, argvalues)
# argnames: A string or list of argument names for the test function.
# argvalues: A list of values, tuples or dictionaries, where each tuple
# contains a set of values corresponding to the argnames.

# Let's take an example:
import sys
from os.path import dirname, join, abspath

sys.path.append(abspath(join(dirname(__file__), "../")))

import pytest
from modules.mathoperations import MathOperations as mp


# 1. Adding a single parameter or argument:

# @pytest.mark.parametrize("x", [1, 2])
# def test_addition(x):
#     assert mp.addition(x) == 1


# 2. Adding Multiple arguments:

# @pytest.mark.parametrize("x, y, c, result", [(1, 3, 2, -4), (8, 5, 1, 2)])
# def test_subtraction(x, y, c, result):
#     assert mp.subtraction(x, y, c) == result


# 3. Adding Multiple arguments with exceptions:

# @pytest.mark.parametrize("dividend, divisor, quotient",
#                          [(8, 0, None), (4, 2, 2)])
# def test_division(dividend, divisor, quotient):
#     try:
#         assert mp.division(dividend, divisor) == quotient
#     except ZeroDivisionError as e:
#         assert str(e) == "The divisor shouldn't be zero"


# 4. Provide descriptive IDs for each test case to improve readability.

# @pytest.mark.parametrize("data",
#                          ["Ruba", 4, -1.5],
#                          ids=["string", "integer", "float"])
# def test_data_type(data):
#     assert isinstance(data, (str, int, float))


# 5. Adding multiple @pytest.mark.parametrize decorators for testing all
# combinations of inputs.
# @pytest.mark.parametrize("x", [1, 3])
# @pytest.mark.parametrize("y", [2, 4])
# def test_multiplication(x, y):
#     expected_result = x * y
#     assert mp.multiplication(x, y) == expected_result


# 6. Parameters as dictionaries:
# @pytest.mark.parametrize("data",
#                          [{"numbers": [2, 4, 1], "result": 7},
#                           {"numbers": (3, 6, 8, 9), "result": 26}])
# def test_addition_data(data):
#     assert mp.addition(*data["numbers"]) == data["result"]

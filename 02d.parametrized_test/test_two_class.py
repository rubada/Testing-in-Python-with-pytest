# How do you add parameters to a test?
# It is done by using the "parametrize" marking, as follows:
# @pytest.mark.parametrize(argnames, argvalues)
# argnames: A string or list of argument names for the test function.
# argvalues: A list of tuples, where each tuple contains a set of values
# corresponding to the argnames.

import sys
from os.path import join, dirname, abspath

sys.path.append(abspath(join(dirname(__file__), "../")))

import modules.mathoperations as mp
import pytest


# The pytest marker can be used with the class
@pytest.mark.parametrize("data",
                         [{"numbers": [2, 4, 1], "result": 7},
                          {"numbers": (3, 6, 8, 9), "result": 26}])
class TestMathoperation:

    def test_addition(self, data):

        # Create the class object:
        mathoper = mp.MathOperations

        # Call the object method:
        assert mathoper.addition(*data["numbers"]) == data["result"]


# The pytest marker can be used with methods
# class TestMathoperationRev:

#     @pytest.mark.parametrize("data", [{"numbers": [2, 4, 1], "result": 7}])
#     def test_addition(self, data):

#         mathoper = mp.MathOperations
#         assert mathoper.addition(*data["numbers"]) == data["result"]

#     @pytest.mark.parametrize("new_data", [{"nums": [3, 4, 2], "output": -3}])
#     def test_subtraction(self, new_data):

#         mathoper = mp.MathOperations
#         assert mathoper.subtraction(*new_data["nums"]) == new_data["output"]

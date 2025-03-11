# Marking Test Functions:
# To create markers on function we use the following decorator syntax:
# @pytest.mark.<markername>

# To execute the test with a single marker
# python -v -m <markername>

# Let's create a marker:
import pytest


# Here I defined a marker called "calmath"
# To execute it:
# python -v -m calmath
# @pytest.mark.calmath
# def test_sub():
#     assert 4 - 5 == -1

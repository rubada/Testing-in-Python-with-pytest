# Marking Test Functions:
# To create markers on a test function we use the following decorator syntax:
# @pytest.mark.<markername>

# To execute the test with a marker
# pytest -v -m <markername>

# Let's create a marker:
import pytest


# Here I defined a marker called "calmath"
# To execute it:
# pytest -v -m calmath
@pytest.mark.calmath
def test_add():
    assert 4 + 5 == 10

# Parametrizing fixtures:
# Fixtures can be parametrized to write concise and readable tests.

# This approach is beneficial when dealing with various database connections,
# multiple files, and so on.

# Let's take an example:

import pytest
from os.path import dirname, join, abspath
import sys
sys.path.append(abspath(join(dirname(__file__), "../")))

from modules import circle


@pytest.fixture(params=[254, 79, 201, 12])
def area_data(request):
    return request.param


def circle_area():
    radius_list = [9, 5, 8, 2]
    return list(map(round, map(circle.area, radius_list)))


# A Test function using a fixture with parameters is called multiple times,
# executing with a different argument each time.
def test_circle_area(area_data):
    areas = circle_area()
    assert area_data in areas

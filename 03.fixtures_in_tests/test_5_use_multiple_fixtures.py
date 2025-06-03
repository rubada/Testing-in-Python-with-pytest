# Using Multiple Fixtures in one test:

import pytest
from os.path import dirname, join, abspath
import sys
sys.path.append(abspath(join(dirname(__file__), "../")))

from modules import circle


# The function that I want to test, using the circle module:
def circle_area(data):
    try:
        float_numbers = map(float, data)
        area_circle = list(map(round, map(circle.area, float_numbers)))
        return area_circle

    except ValueError:
        raise ValueError("Data items should be numbers, not strings")


@pytest.fixture
def open_file():
    script_dir = dirname(__file__)
    path_text = join(script_dir, "circle_radius.txt")

    file = open(path_text)
    yield file
    file.close()


@pytest.fixture
def area_data():
    areas = [254, 79, 201, 13]
    return areas


def test_circle_area(open_file, area_data):
    test_areas_1 = circle_area(open_file)
    test_areas_2 = area_data
    assert test_areas_1 == test_areas_2

# Writing a test class:
# To group all your test you can group them into one class
# Also we can call a single test method:
# pytest <script-name>::<class-name>::<method-name>

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             "../")))

import modules.rectangle as rect
import modules.circle as cir
import pytest


class TestRectangle:

    def test_area(self):
        assert rect.area(2, 3) == 6

    def test_perimeter(self):
        assert rect.perimeter(2, 3) == 10

    def test_data_type(self):
        try:
            rect.area("2", 4)
        except TypeError as e:
            assert str(e) == "Rectangel length, width should be integers or\
    float"


@pytest.mark.circle_area
class TestCircle:

    def test_return_value_type(self):
        "area() should return a float"
        test_one = cir.area(3)
        assert type(test_one) is float

    def test_arguments(self):
        try:
            cir.perimeter(-4)
        except ValueError as e:
            assert str(e) == "Circle raduis should be greater than zero"

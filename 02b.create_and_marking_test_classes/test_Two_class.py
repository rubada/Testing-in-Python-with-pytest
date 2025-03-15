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

    @pytest.mark.area
    def test_area(self):
        assert rect.area(2, 3) == 6

    @pytest.mark.perimeter
    def test_perimeter(self):
        assert rect.perimeter(2, 3) == 10


class TestCircle:

    @pytest.mark.area
    def test_area(self):
        assert round(cir.area(4), 2) == 50.27

    @pytest.mark.perimeter
    def test_perimeter(self):
        assert round(cir.perimeter(4), 2) == 25.13


# Registering marks
# You can register custom marks in your "pytest.ini".
# Unregistered marks will always emit a warning to avoid silently doing
# something surprising due to mistyped names.
# For example, if you want to use the "@pytest.mark.perimeter" with other
# tests and misspell it "@pytest.mark.perimetr" pytest will raise a
# warning that this marker is not registered.

# If the markers are not registered, uswhen using the “--strict-markers” flag,
# it will raise an error, instead of warning and you will know which markers
# are not registered.
# pytest --strict-markers -m "marker_name"

# If you want to run "--strict-markers" by default when running a test, to
# raise an error if the marker is not registered,
# add "addopts = --strict-markers" to the "pytest.ini".

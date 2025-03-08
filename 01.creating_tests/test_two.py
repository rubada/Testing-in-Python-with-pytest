# When testing your project, your test folder should be in the project's main
# project folder:

# main_project_folder/
# │
# ├── project_folder/
# |
# ├── tests_folder
# |
# └── setup, readme, license, etc.

# When testing your project files, these files should be imported as modules,
# and this is done in two ways:
# 1. Install your project as a package.
# 2. Make your project folder a module by adding its path to the list of paths,
# where the interpreter searches for a module.

# To know more about the above check the module section in the Python course
# part three.
import sys
from os.path import dirname, join, abspath

sys.path.append(abspath(join(dirname(__file__), "../")))
from modules import circle


# Test the returned value type:
def test_return_value_type():
    "area() should return a float"
    test_one = circle.area(3)
    assert type(test_one) is float


# Test that the arguments are greater than zero, the circle module functions
# have "raise" statements if the parameters are equal or less than zero, an
# exception is raised.
# We will test this:
def test_arguments():
    try:
        circle.perimeter(-4)
    except ValueError as e:
        assert str(e) == "Circle raduis should be greater than zero"
        # assert e == "Circle raduis should be greater than zero"

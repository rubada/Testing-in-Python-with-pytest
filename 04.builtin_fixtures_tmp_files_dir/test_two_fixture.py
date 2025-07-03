# Temporary directories and files in tests
# pytest temporary directories and files are quite useful in testing,
# especially when you need to create, modify, or delete files without
# affecting the actual filesystem.
# Advantages:
# 1. Eliminates the need for manual cleanup.
# 2. Ensures an isolated environment for each test run.

# There are two fixtures in pytest for temporary directories and files:
# 1. The "tmp_path" fixture and the tmp_path_factory fixture:
# Both fixtures are "pathlib.Path" objects, generally making them faster.
# b. "tmp_path_factory" fixture is session-scoped fixture used to create
# arbitrary temporary directories from other fixture.

# b. "tmp_path_factory" is used to create multiple temporary directories within
# a test session.

# To use the "tmp_path_factory":
# 1. Define a fixture in "conftest.py", with the "tmp_path_factory" as a
# parameter.
# 2. Use pytest fixture decorator to create a fixture.
# 3. Use the fixture scope you prefer.

# Let's take an example:

from my_functions import (circle_area,
                          write_to_file,
                          read_file)


def test_write_read_one(temp_files):
    # Define test data
    areas = ["13\n", "113\n", "28\n", "79\n"]

    # Writing data to the "tmp_file"
    write_to_file(areas, temp_files)

    # Assert that the file was created in the tmp_path
    assert temp_files.exists()

    test_areas = read_file(temp_files)

    # Assert that the data read from the file matches the data is calculated
    # by "circle_area" function.
    assert circle_area([2, 6, 3, 5]) == test_areas


def test_write_read_two(temp_files):
    # Define test data
    areas = ["28\n", "201\n", "50\n", "254\n"]

    # Writing data to the "tmp_file"
    write_to_file(areas, temp_files)

    # Assert that the file was created in the tmp_path
    assert temp_files.exists()

    test_areas = read_file(temp_files)

    # Assert that the data read from the file matches the data is calculated
    # by "circle_area" function.
    assert circle_area([3, 8, 4, 9]) == test_areas


# 2. The "tmpdir" and "tmpdir_factory" fixtures:
# The "tmpdir" and "tmpdir_factory" fixtures are similar to "tmp_path" and
# "tmp_path_factory", but they use "py.path.local" objects, (Requires "py"
# library) while "tmp_path" and "tmp_path_factory" use the standard
# "pathlib.Path" objects and they are preferred for modern Python development.

# Temporary directories and files in tests
# pytest temporary directories and files are quite useful in testing,
# especially when you need to create, modify, or delete files without
# affecting the actual filesystem.
# Advantages:
# 1. Eliminates the need for manual cleanup.
# 2. Ensures an isolated environment for each test run.

# There are two fixtures in pytest for temporary directories and files:
# 1. The "tmp_path" fixture and the tmp_path_factory fixture:
# Both fixtures are "pathlib.Path" objects, generally making them faster,
# and you can use all the methods and properties available in the
# "pathlib.Path" module.

# a. "tmp_path" fixture makes pytest automatically create a unique temporary
# directory before the test begins and clean it up after completion.

# tmp_path is used for creating temporary directories per single test
# function.

from my_functions import (circle_area,
                          write_to_file,
                          read_file)


# # Test function:
# def test_write_read(tmp_path):
#     # Define test data
#     areas = ["13\n", "113\n", "28\n", "79\n"]

#     # Create a temporary file within the "tmp_path" directory:
#     tmp_file = tmp_path / "test_areas.txt"

#     # Writing data to the "tmp_file"
#     write_to_file(areas, tmp_file)

#     # Assert that the file was created in the tmp_path
#     assert tmp_file.exists()

#     test_areas = read_file(tmp_file)

#     # Assert that the data read from the file matches the data is calculated
#     # by "circle_area" function.
#     assert circle_area([2, 6, 3, 5]) == test_areas


# Also you can create multiple directories and files in the
# "tmp_path"
def test_write_read_mult(tmp_path):
    # Define test data
    areas = ["13\n", "113\n", "28\n", "79\n"]

    # Create two separate temporary directories
    temp_dir_1 = tmp_path / "DirOne"
    temp_dir_2 = tmp_path / "DirTwo"
    temp_dir_1.mkdir()
    temp_dir_2.mkdir()

    # Create two temporary files within the temporary directories:
    tmp_file_1 = temp_dir_1 / "areas1.txt"
    tmp_file_2 = temp_dir_2 / "areas2.txt"

    # Writing data to the "tmp_file"
    write_to_file(areas, tmp_file_1)
    write_to_file(areas, tmp_file_2)

    # Assert that the files were created in the temporary directories:
    assert tmp_file_1.exists()
    assert tmp_file_2.exists()

    test_areas1 = read_file(tmp_file_1)
    test_areas2 = read_file(tmp_file_2)

    # Assert that the data read from the files is the same.
    assert test_areas1 == test_areas2

import pytest


# Create a fixture with "tmp_path_factory" to be used with multiple
# test functions, classes.
# @pytest.fixture(scope="session")
# # @pytest.fixture(scope="module")
# # @pytest.fixture
# def temp_files(tmp_path_factory):
#     # Make a temporary directory and file:
#     tmp_dir = tmp_path_factory.mktemp("tempdir") / "test_areas.txt"
#     return tmp_dir


# @pytest.fixture(scope="session")
# @pytest.fixture(scope="module")
@pytest.fixture
def temp_files(tmp_path):
    tmp_file = tmp_path / "test_areas.txt"
    return tmp_file

from os.path import dirname, join, abspath
import pytest


@pytest.fixture(scope="session")
def open_file():
    script_dir = dirname(__file__)
    file1 = open(abspath(join(script_dir, "../text1.txt")))
    file2 = open(abspath(join(script_dir, "../text2.txt")))
    yield file1, file2
    file1.close()
    file2.close()

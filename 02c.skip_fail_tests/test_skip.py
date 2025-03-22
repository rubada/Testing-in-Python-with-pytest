# Skipping Tests
# why do need to skip tests?
# 1. Incompatible Python version.
# 2. Incompatible package version.
# 3. Platform requirements such as Windows, Mac, or Linux.
# 4. Incomplete tests.
# 5. External resource dependencies such as database or API.
# 6. Etcetera.

# To skip a test two built-in markers are used:
# skip, skipif
# @pytest.mark.skip

# Let's take different examples:
import pytest
import sys
import math
import platform


@pytest.mark.skip(reason="This module is not completed yet.")
def test_add():
    assert None


@pytest.mark.skipif(sys.platform == "win32",
                    reason="App does not run on Windows.")
def test_myapp():
    assert math.pow(2, 3) == 8
    assert math.dist((2, 4), (4, 6)) == 5


@pytest.mark.skipif(platform.python_version() != "3.12.3",
                    reason="Python version should be 3.12.3")
def test_pack():
    assert math.pow(2, 3) == 8

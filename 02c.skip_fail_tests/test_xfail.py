# Marking Tests as "expected to fail"
# Why do we need “expected to fail” tests?
# 1. It is useful for keeping track of bugs that have been reported and are
# yet to be fixed, ensuring they're not accidentally overlooked.
# 2. Adding a reason to a test that is expected to fail, will help to document
# why the test failed, making it easier for other developers to understand
# the context.
# 3. If an "expected to fail" test suddenly starts passing, it could indicate
# that there is unexpected behavior that should be checked.

# This done by using the "xfail" marker
# There are two outputs:
# xfail (Expected Fail): The test is expected to fail because of a known bug,
# unimplemented feature, or other issues.
# xpass (Unexpected Pass): The test that is expected to fail, but it has
# unexpectedly passed, that indicates:
# 1. The bug might be fixed.
# 2. Review to confirm the output, and check for other issues.

import pytest


def division(x, y):
    return x / y


@pytest.mark.xfail(reason="ZeroDivisionError is not handled")
def test_division():
    assert division(3, 0)


@pytest.mark.xfail(reason="ZeroDivisionError is not handled but passed")
def test_division_zero():
    with pytest.raises(ZeroDivisionError):
        division(3, 0)

# The above test is xpass but the bug is not fixed.

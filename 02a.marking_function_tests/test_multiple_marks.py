# To execute tests with multiple markers in pytest, logical
# expressions (and, or, not) can be used in the -m option.
# As follows:
# pytest -v -m "mark1 or mark2 or mark3 ..."
# pytest -v -m "mark1 and mark2 and mark3 ..."
# pytest -m "(mark1 or mark2) and not mark3"
# etc.,


# Let's take an example:
import pytest


@pytest.mark.add
def test_add():
    assert 3 + 1 == 4


@pytest.mark.sub
def test_sub():
    assert 25 - 2 == 23


@pytest.mark.add
@pytest.mark.sub
def test_add_sub():
    assert 30 + 3 == 33
    assert 4 - 5 == -1


@pytest.mark.multiply
def test_multiply():
    assert 4 * 3 == 12


# pytest -v -m "add or sub or multiply"
# pytest -v -m "add or sub"
# pytest -v -m "add and sub
# pytest -v -m "not add"
# pytest -v -m "(add or sub) and not multiply"

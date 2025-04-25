# Sharing Data:

# Let's take an example:

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def test_add(add_data):
    assert add(**add_data) == 5


def test_sub(sub_data):
    assert sub(**sub_data) == 1

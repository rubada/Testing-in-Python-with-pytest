def addition(*args):
    """
    The addition function is used to sum multiple numbers
    >>> addition(2, 3)
    5
    >>> addition(-1, 5, 2, 6)
    12
    """
    num = 0
    for i in args:
        num += i
    return num


def subtraction(*args):
    """
    The subtraction function is used to subtract multiple numbers
    >>> subtraction(5, 3)
    2
    >>> subtraction(-1, 5, 2, 6)
    -14
    """
    num = args[0]
    for i in range(1, len(args)):
        num = num - args[i]
    return num

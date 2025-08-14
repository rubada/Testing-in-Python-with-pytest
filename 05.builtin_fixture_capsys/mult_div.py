def multiplication(*args):
    """
    The multiplication function is used to multiply multiple numbers
    >>> multiplication(2, 3)
    6
    >>> multiplication(4, 5, 2, 6)
    240
    """
    num = args[0]
    for i in range(1, len(args)):
        num = num * args[i]
    return num


def division(*args):
    """
    The division function is used to divide two numbers
    >>> division(6, 3)
    2.0
    >>> division(12, 0)
    The divisor shouldn't be zero
    """
    try:
        return (args[0] / args[1])
    except ZeroDivisionError:
        print("The divisor shouldn't be zero")

# print(division(12, 0))

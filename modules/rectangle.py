
def area(length, width):
    val_type = (int, float)
    try:
        if isinstance(length, val_type) and isinstance(width, val_type):
            return length * width
    except TypeError:
        raise TypeError("Rectangel length, width should be integers or float")


def perimeter(length, width=2):
    return 2 * (length + width)


if __name__ == "__main__":
    print(f"The Rectangel Area = {area(2, 3)}")
    print(f"The Rectangel Perimeter = {perimeter(2, 4)}")

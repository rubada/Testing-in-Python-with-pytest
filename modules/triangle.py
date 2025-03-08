
def area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Triangle length, width should be greater than zero")
    return 0.5 * length * width


def perimeter(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3:
        raise ValueError("Triangle sides should be greater than zero")
    return side1 + side2 + side3


if __name__ == "__main__":
    print(f"The Triangle Area = {area(6, 4)}")
    print(f"The Triangle Perimeter = {perimeter(7, 4, 5)}")

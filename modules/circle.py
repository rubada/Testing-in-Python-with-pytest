import math


def area(radius):
    if radius <= 0:
        raise ValueError("Circle raduis should be greater than zero")
    radius_pow = math.pow(radius, 2)
    area = math.pi * radius_pow
    return area


def perimeter(radius):
    if radius <= 0:
        raise ValueError("Circle raduis should be greater than zero")
    return 2 * math.pi * radius


if __name__ == "__main__":
    print(f"The Circle Area = {area(1)}")
    print(f"The Circle Perimeter = {perimeter(1)}")

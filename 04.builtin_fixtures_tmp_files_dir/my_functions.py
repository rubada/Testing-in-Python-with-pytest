from math import pi, pow


# The functions to test
def circle_area(data):
    float_numbers = list(map(float, data))
    area_circle = list(map(lambda x: pi * pow(x, 2), float_numbers))
    return list(map(round, area_circle))


def write_to_file(data, file_path):
    with open(file_path, 'w') as file:
        file.writelines(data)


def read_file(file_path):
    with open(file_path) as file:
        data = list(map(int, file.readlines()))
        return data

from point import Point


def read_input_data_file(input_data_file):
    points_array = []
    with open(input_data_file, "r") as data_file:
        for line in data_file:
            key, x, y = "".join(line.split()).split(",")
            points_array.append(Point(key, float(x), float(y)))
    return points_array


def write_output_file(points_array, output_data_file):
    with open(output_data_file, "wb") as data_file:
        output = ",".join((point.get_key() for point in points_array))
        data_file.write(bytes(output))

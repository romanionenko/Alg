import ioutil
from grahamscanalgorithm import graham_scan


def main():
    points_array = ioutil.read_input_data_file("input_data.txt")
    convex_hull = graham_scan(points_array)
    ioutil.write_output_file(convex_hull, "output.txt")


main()

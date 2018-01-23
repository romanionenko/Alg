# distance
def min_edit_distance_1(string_1, string_2):
    """Calculate min edit distance string_1->string_2."""

    string_1_length = len(string_1)
    string_2_length = len(string_2)

    # matrix creation, values[i][j] = 0
    matrix_height = string_1_length + 1
    matrix_width = string_2_length + 1
    matrix = [None] * matrix_height
    for i in range(matrix_height):
        matrix[i] = [0] * matrix_width

    # initial horizontal and vertical values
    for i in range(1, matrix_height):
        matrix[i][0] = i
    for j in range(1, matrix_width):
        matrix[0][j] = j

    # best values calculation
    for i in range(1, matrix_height):
        for j in range(1, matrix_width):
            cost = 1
            prev_i = i - 1
            prev_j = j - 1
            if string_1[prev_i] == string_2[prev_j]:
                cost = 0
            replace_cost = matrix[prev_i][prev_j] + cost
            remove_cost = matrix[prev_i][j] + 1
            insert_cost = matrix[i][prev_j] + 1
            matrix[i][j] = min(replace_cost, remove_cost, insert_cost)
    return matrix, matrix[string_1_length][string_2_length]


REPLACE = 0
REMOVE = 1
INSERT = 2


# distance with operations
def min_edit_distance_2(string_1, string_2):
    """Calculate min edit distance and operations string_1->string_2."""
    string_1_length = len(string_1)
    string_2_length = len(string_2)

    # matrix creation, values[i][j] = 0
    matrix_height = string_1_length + 1
    matrix_width = string_2_length + 1
    height = [None] * matrix_height
    distance_matrix = height
    operations_matrix = height
    for i in range(matrix_height):
        distance_matrix[i] = [0] * matrix_width
        operations_matrix[i] = [-1] * matrix_width

    # initial horizontal and vertical values
    for i in range(1, matrix_height):
        distance_matrix[i][0] = i
    for j in range(1, matrix_width):
        distance_matrix[0][j] = j

    # best values calculation
    for i in range(1, matrix_height):
        for j in range(1, matrix_width):
            cost = 1
            prev_i = i - 1
            prev_j = j - 1
            if string_1[prev_i] == string_2[prev_j]:
                cost = 0
            replace_cost = distance_matrix[prev_i][prev_j] + cost
            remove_cost = distance_matrix[prev_i][j] + 1
            insert_cost = distance_matrix[i][prev_j] + 1
            costs = [replace_cost, remove_cost, insert_cost]
            distance_matrix[i][j] = min(costs)
            operations_matrix[i][j] = costs.index(distance_matrix[i][j])
    operations = []
    i = string_1_length
    j = string_2_length
    while i != 0 or j != 0:
        prev_i = i - 1
        prev_j = j - 1
        if operations_matrix[i][j] == REMOVE or j == 0:
            operations.append("Remove {} char {} of {}".format(i, string_1[prev_i], string_1))
            i = i - 1
        elif operations_matrix[i][j] == INSERT or j == 0:
            operations.append("Insert {} char {} of {}".format(j, string_2[prev_j], string_2))
            j = j - 1
        else:
            if distance_matrix[prev_i][prev_j] < distance_matrix[i][j]:
                format_string = "Replace {} char of {} ({}) with {}"
                operations.append(format_string.format(i, string_1, string_1[prev_i], string_2[prev_j]))
            i, j = i - 1, j - 1
    return distance_matrix, distance_matrix[string_1_length][string_2_length], operations


def print_matrix(matrix):
    print("\n".join(["".join(["{:4}".format(item) for item in row]) for row in matrix]))


def print_delimiter(count):
    print('-' * count)


if __name__ == "__main__":
    input_string_1 = "GCTAC"
    input_string_2 = "CTCA"
    distance_matrix_1, value_1 = min_edit_distance_1(input_string_1, input_string_2)
    print_matrix(distance_matrix_1)
    minor_delimiter = 5
    print_delimiter(minor_delimiter)
    print(value_1)
    print_delimiter(20)
    distance_matrix_2, value_2, operation_string = min_edit_distance_2(input_string_1, input_string_2)
    print_matrix(distance_matrix_1)
    print_delimiter(minor_delimiter)
    print(value_2)
    print_delimiter(minor_delimiter)
    print(", ".join(operation_string))

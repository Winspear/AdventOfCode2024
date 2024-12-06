import copy

def build_matrix():
    matrix = []
    with open('input_sample.txt', 'r') as file:
        for line in file:
            matrix.append(list(line.strip()))
    return matrix

def find_start_position(matrix):
    for row, line in enumerate(matrix):
        for column, character in enumerate(line):
            if character == '^':
                return row, column

def has_walked_before(row, column, start_value, matrix):
    print(start_value)
    if start_value[0] == row and start_value[1] ==column:
        while True:
            if matrix[row - 1][column] == ".":
                return False
            if matrix[row - 1][column] == "X":
                row = row - 1
            if matrix[row - 1][column] == "#":
                return True

def part1(matrix):
    x_counter = 0
    row, column = find_start_position(matrix)
    start_value = []
    start_value.append(row)
    start_value.append(column)
    while True:
        if row < 0:
            return False, x_counter
        if has_walked_before(row, column, start_value, matrix):
            print('Returning True, this is matrix: ')
            for line in matrix:
                print(line)
            return True, x_counter
        if matrix[row - 1][column] in [".", "X"]:
            matrix[row][column] = "X"
            if matrix[row - 1][column] == '.':
                x_counter += 1
            matrix[row - 1][column] = "X"
            row = row - 1
        else:
            matrix[row][column] = "^"
            matrix_with_tuples = list(zip(*matrix))[::-1]
            matrix = [list(line) for line in matrix_with_tuples]
            row, column = find_start_position(matrix)

def part2():
    obstacle_count = 0
    matrix = build_matrix()
    rows = len(matrix)
    columns = len(matrix[0])

    for row_index in range(len(matrix)):
        matrix = build_matrix()
        print('This is the new matrix: ', matrix)
        for column_index in range(len(matrix[0])):
            if matrix[row_index][column_index] in ['^', '#']:
                continue
            matrix[row_index][column_index] = '#'
            bool_res, _ = part1(matrix)
            if bool_res:
                obstacle_count += 1
    print(obstacle_count)

    





if __name__ == '__main__':
    print(part1(build_matrix()))
    # print(part2())
def build_matrix():
    matrix = []
    with open('input.txt', 'r') as file:
        for line in file:
            matrix.append(list(line.strip()))
    return matrix

def try_going_backwards(row, column_number):
    if column_number < 3:
        return 0
    if row[column_number] + row[column_number - 1] + row[column_number - 2] + row[column_number - 3] == 'XMAS':
        return 1
    return 0

def try_going_forwards(row, column_number):
    if column_number > len(row) - 4:
        return 0
    if row[column_number] + row[column_number + 1] + row[column_number + 2] + row[column_number + 3] == 'XMAS':
        return 1
    return 0


def try_going_up(row, row_number, column_number, matrix):
    if row_number < 3:
        return 0
    if matrix[row_number][column_number] + matrix[row_number - 1][column_number] + matrix[row_number - 2][column_number] + matrix[row_number - 3][column_number] == "XMAS":
        return 1
    return 0

def try_going_down(row, row_number, column_number, matrix):
    if row_number > len(matrix) - 4:
        return 0
    if matrix[row_number][column_number] + matrix[row_number + 1][column_number] + matrix[row_number + 2][column_number] + matrix[row_number + 3][column_number] == "XMAS":
        return 1
    return 0


def try_going_northeast(row, row_number, column_number, matrix):
    if row_number < 3 or column_number > len(row) - 4:
        return 0
    if matrix[row_number][column_number] + matrix[row_number - 1][column_number + 1] + matrix[row_number - 2][column_number + 2] + matrix[row_number - 3][column_number + 3] == "XMAS":
        return 1
    return 0

def try_going_northwest(row, row_number, column_number, matrix):
    if row_number < 3 or column_number < 3:
        return 0
    if matrix[row_number][column_number] + matrix[row_number - 1][column_number - 1] + matrix[row_number - 2][column_number - 2] + matrix[row_number - 3][column_number - 3] == "XMAS":
        return 1
    return 0

def try_going_southeast(row, row_number, column_number, matrix):
    if row_number > len(matrix) - 4 or column_number > len(row) - 4:
        return 0
    if matrix[row_number][column_number] + matrix[row_number + 1][column_number + 1] + matrix[row_number + 2][column_number + 2] + matrix[row_number + 3][column_number + 3] == "XMAS":
        return 1
    return 0


def try_going_southwest(row, row_number, column_number, matrix):
    if row_number > len(matrix) - 4 or column_number < 3:
        return 0
    if matrix[row_number][column_number] + matrix[row_number + 1][column_number - 1] + matrix[row_number + 2][column_number - 2] + matrix[row_number + 3][column_number - 3] == "XMAS":
        return 1
    return 0


def find_letter_northeast(row, row_number, column_number, matrix):
    if row_number < 1 or column_number > len(row) - 2:
        return '.'
    return matrix[row_number - 1][column_number + 1]

def find_letter_southwest(row, row_number, column_number, matrix):
    if row_number > len(matrix) - 2 or column_number < 1:
        return '.'
    return matrix[row_number + 1][column_number - 1]

def find_letter_northwest(row, row_number, column_number, matrix):
    if row_number < 1 or column_number < 1:
        return '.'
    return matrix[row_number - 1][column_number - 1]

def find_letter_southeast(row, row_number, column_number, matrix):
    if row_number > len(matrix) - 2 or column_number > len(row) - 2:
        return '.'
    return matrix[row_number + 1][column_number + 1]











def part1():
    xmas_total_count = 0
    matrix = build_matrix()
    for row_number, row in enumerate(matrix):
        for column_number, character in enumerate(row):
            if character == "X":
                xmas_total_count += try_going_backwards(row, column_number)
                xmas_total_count += try_going_forwards(row, column_number)
                xmas_total_count += try_going_up(row, row_number, column_number, matrix)
                xmas_total_count += try_going_down(row, row_number, column_number, matrix)
                xmas_total_count += try_going_northeast(row, row_number, column_number, matrix)
                xmas_total_count += try_going_northwest(row, row_number, column_number, matrix)
                xmas_total_count += try_going_southeast(row, row_number, column_number, matrix)
                xmas_total_count += try_going_southwest(row, row_number, column_number, matrix)
    return xmas_total_count


def part2():
    xmas_total_count = 0
    matrix = build_matrix()
    for row_number, row in enumerate(matrix):
        for column_number, character in enumerate(row):
            if character == "A":
                first_letter = find_letter_northeast(row, row_number, column_number, matrix)
                if first_letter in ['S', 'M']:
                    second_letter = find_letter_southwest(row, row_number, column_number, matrix)
                    if (first_letter == "S" and second_letter == "M") or (first_letter == "M" and second_letter == "S"):
                        third_letter = find_letter_northwest(row, row_number, column_number, matrix)
                        if third_letter in ['S', 'M']:
                            fourth_letter = find_letter_southeast(row, row_number, column_number, matrix)
                            if (third_letter == "S" and fourth_letter == "M") or (third_letter == "M" and fourth_letter == "S"):
                                xmas_total_count += 1
    return xmas_total_count





                

        



if __name__ == '__main__':
    print("pt1 answer: ", part1())
    print("p2 answer: ", part2())







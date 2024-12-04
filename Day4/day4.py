"""
--- Day 4: Ceres Search ---

"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....

The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

Take a look at the little Elf's word search. How many times does XMAS appear?
--- Part Two ---

The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S

Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?

"""
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







def get_difference(sorted_first_list, sorted_second_list):
    difference = 0
    for iterator in range(0, len(sorted_first_list)):
        first_number = int(sorted_first_list[iterator])
        second_number = int(sorted_second_list[iterator])
        if first_number > second_number:
            difference += (first_number - second_number)
        else:
            difference += (second_number - first_number)
    return difference


def get_similarity(sorted_first_list, sorted_second_list):
    score = 0
    for number in sorted_first_list:
        times_appeared = sorted_second_list.count(number)
        score += (number * times_appeared)
    return score

def day1():
    first_list = []
    second_list = []
    with open('input.txt', 'r') as file:
        for line in file:
            first_number, second_number = line.split("  ")
            first_list.append(int(first_number))
            second_list.append(int(second_number))
    sorted_first_list = sorted(first_list)
    sorted_second_list = sorted(second_list)

    print('Solution to part 1: ')
    print(get_difference(sorted_first_list, sorted_second_list))
    print('----------')
    print('Solution to part 2')
    print(get_similarity(sorted_first_list, sorted_second_list))


if __name__ == '__main__':
    print(day1())

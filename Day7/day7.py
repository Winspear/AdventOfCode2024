import itertools

def part1():
    with open("input.txt", "r") as file:
        final_total = 0
        for line in file:
            required_total, numbers_string = line.split(":")
            numbers_list = [number for number in numbers_string.strip().split(' ')]
            all_operator_combinations = list(itertools.product(['*', '+'], repeat=len(numbers_list) -1))
            for operator_combination in all_operator_combinations:
                current_total = int(numbers_list[0])
                for index in range(len(operator_combination)):
                    current_total = eval(f"{current_total}{operator_combination[index]}{numbers_list[index + 1]}")
                if current_total == int(required_total):
                    final_total += current_total
                    break
    return final_total

def part2():
    with open("input.txt", "r") as file:
        final_total = 0
        for line in file:
            required_total, numbers_string = line.split(":")
            numbers_list = [number for number in numbers_string.strip().split(' ')]
            all_operator_combinations = list(itertools.product(['*', '+', '||'], repeat=len(numbers_list) -1))
            for operator_combination in all_operator_combinations:
                current_total = int(numbers_list[0])
                for index in range(len(operator_combination)):
                    if operator_combination[index] in ['*', '+']:
                        current_total = eval(f"{current_total}{operator_combination[index]}{numbers_list[index + 1]}")
                    else:
                        current_total = int(str(current_total) + numbers_list[index + 1])
                if current_total == int(required_total):
                    final_total += current_total
                    break
    return final_total
            
if __name__ == '__main__':
    print("pt1 answer: ", part1())
    print("pt2 answer: ", part2())


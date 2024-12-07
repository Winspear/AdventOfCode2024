import itertools

def part1():
    with open("input_sample.txt", "r") as file:
        final_total = 0
        for line in file:
            print('Should be here')
            required_total, numbers_string = line.split(":")
            numbers_list = [number for number in numbers_string.strip().split(' ')]
            print('This is numbers list: ', numbers_list)
            all_operator_combinations = list(itertools.product(['*', '+'], repeat=len(numbers_list) -1))
            print(all_operator_combinations) 
            for operator_combination in all_operator_combinations:
                equation = ''
                for index in range(len(operator_combination)):
                    equation = equation + numbers_list[index] + operator_combination[index]
                equation = equation + numbers_list[-1]
                equation_total = eval(equation)
                print('equation is: ', equation)
                if equation_total == int(required_total):
                    final_total += equation_total
                    break
    return final_total
            
if __name__ == '__main__':
    print("pt1 answer: ", part1())


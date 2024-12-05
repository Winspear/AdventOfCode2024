import re

def mul(x, y):
    return x * y

def check_if_should_eval(start_character, ignored_ranges):
    for each_range in ignored_ranges:
        if start_character in ignored_ranges:
            return False
    return True

def part1():
    with open('input_sample.txt', 'r') as file:
        day_1_total = 0
        for line in file:
            matches = re.findall(r"mul\(\d+,\d+\)", line)
            for function in matches:
                day_1_total += eval(function)

        return day_1_total


def part2():
    with open('input.txt', 'r') as file:
        day_2_total = 0
        enabled = True
        pattern = re.compile(r"mul\(\d+,\d+\)|don't\(\)|do\(\)")
        for line in file:
            for match in re.finditer(pattern,line):
                if match.group(0) == "do()":
                    enabled = True
                elif match.group(0) == "don't()":
                    enabled = False
                elif enabled:
                    day_2_total += eval(match.group(0))
        return day_2_total



if __name__ == '__main__':
    print(part1())
    print(part2())

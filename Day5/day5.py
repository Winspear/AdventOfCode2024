import re

def get_rules_and_safety_manuals():
    rules = {}
    safety_manuals = []
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if re.match(r"\d+\|\d+", line):
                key, value = line.split('|')
                if not rules.get(int(key)):
                    rules[int(key)] = []
                rules[int(key)].append(int(value))
            else:
                if line:
                    safety_manuals.append([int(number) for number in line.split(',')])
    return rules, safety_manuals


def check_numbers_before(numbers_to_check, numbers_that_should_not_be_found):
    intersection = numbers_to_check.intersection(numbers_that_should_not_be_found)
    if intersection:
        return True
    return False

def sort_manuals_into_safe_and_unsafe(safety_manuals, rules):
    manuals_marked_safe = []
    manuals_marked_unsafe = []
    for manual in safety_manuals:
        for index, number in enumerate(manual):
            if number in rules.keys():
                breaks_rules = check_numbers_before(set(manual[:index]), set(rules[number]))
                if breaks_rules:
                    manuals_marked_unsafe.append(manual)
                    break
        if not breaks_rules:
            manuals_marked_safe.append(manual)
    return manuals_marked_safe, manuals_marked_unsafe

def get_safe_total(manuals_marked_safe):
    safe_total = 0
    for safe_manual in manuals_marked_safe:
        safe_total += safe_manual[len(safe_manual) // 2]
    return safe_total


def fix_unsafe_manuals(manuals_marked_unsafe, rules, fixed_manuals = []):
    manuals_to_remove = []
    manuals_to_add = []
    for manual_index, manual in enumerate(manuals_marked_unsafe):
        manuals_to_remove.append(manual)
        for index, number in enumerate(manual):
            if number in rules.keys():
                breaks_rules = check_numbers_before(set(manual[:index]), set(rules[number]))
                if breaks_rules:
                    manual.pop(index)
                    manual.insert(index - 1, number)
                    manuals_to_add.append(manual)
                    break
        if not breaks_rules:
            fixed_manuals.append(manual)
    for manual_to_remove in manuals_to_remove:
        manuals_marked_unsafe.remove(manual_to_remove)
    for manual_to_add in manuals_to_add:
        manuals_marked_unsafe.append(manual_to_add)

    if manuals_marked_unsafe:
        fix_unsafe_manuals(manuals_marked_unsafe, rules, fixed_manuals)

    return fixed_manuals




def part1():
    unsafe_total = 0
    rules, safety_manuals = get_rules_and_safety_manuals()
    manuals_marked_safe, manuals_marked_unsafe = sort_manuals_into_safe_and_unsafe(safety_manuals, rules)
    safe_total = get_safe_total(manuals_marked_safe)
    unsafe_total = get_safe_total(fix_unsafe_manuals(manuals_marked_unsafe, rules))

    print("Part1 total: ", safe_total)
    print("Part2 total: ", unsafe_total)


if __name__ == '__main__':
    part1()
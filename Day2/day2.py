def day2():
    safe_count = 0
    with open('input.txt', 'r') as file:
        for line in file:
            report = []
            for item in line.split(" "):
                report.append(int(item))
            if is_report_safe(report):
                safe_count += 1


def is_report_safe(report):
    is_increasing = check_is_increasing(report)
    return check_next_number(0, report, is_increasing, has_error=False)


def check_is_increasing(report):
    return report[0] < report[1]


def check_next_number(current_index, report, is_increasing, has_error):
    if len(report) == current_index + 1:
        return True
    first_number = report[current_index]
    second_number = report[current_index+1]
    if is_increasing:
        if _compare_numbers(second_number, first_number):
            return check_next_number(current_index+1, report, is_increasing, has_error)
        else:
            if not has_error:
                return _try_again_with_error_tolerance(current_index, report, is_increasing)
            return False
    if _compare_numbers(first_number, second_number):
        return check_next_number(current_index+1, report, is_increasing, has_error)
    else:
        if not has_error:
            return _try_again_with_error_tolerance(current_index, report, is_increasing)
    return False


def _try_again_with_error_tolerance(current_index, report, is_increasing):
    
    first_index_removed_report = report.copy()
    first_index_removed_report.pop(0)

    removed_first_index = check_next_number(0, first_index_removed_report, check_is_increasing(first_index_removed_report), True)
    if removed_first_index:
        return removed_first_index
    current_index_removed_report = report.copy()
    current_index_removed_report.pop(current_index)
    removed_current_index = check_next_number(0, current_index_removed_report, check_is_increasing(first_index_removed_report), True)
    if removed_current_index:
        return removed_current_index

    report.pop(current_index+1)
    return removed_current_index or check_next_number(0, report, check_is_increasing(report), True)


def _compare_numbers(first_number, second_number):
    return first_number > second_number and (first_number - second_number) <= 3

if __name__ == '__main__':
    print(day2())
def parse_numbers():
    with open("inputs/d09.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    return [int(line) for line in lines]


def is_valid(numbers, index):
    value = numbers[index]
    for i, num1 in enumerate(numbers[index-25:index]):
        for num2 in numbers[index-25+i:index]:
            if num1 + num2 == value:
                return True
    return False


def get_valid_contiguous_list(numbers, index):
    target_value = numbers[index]
    values_sum = i_min = i_max = 0
    while values_sum != target_value:
        while values_sum < target_value:
            values_sum += numbers[i_max]
            i_max += 1
        while values_sum > target_value:
            values_sum -= numbers[i_min]
            i_min += 1
    values = numbers[i_min:i_max]
    return min(values), max(values)


def run_09a():
    numbers = parse_numbers()
    index = 25
    while is_valid(numbers, index):
        index += 1
    print(index)
    print(numbers[index])
    return index


def run_09b():
    numbers = parse_numbers()
    first_invalid_index = run_09a()
    i1, i2 = get_valid_contiguous_list(numbers, first_invalid_index)
    print(i1 + i2)

import functools


def parse_forms(lines, join_operation):
    split_indexes = [i for i, val in enumerate(lines) if val == ""]
    total_count = sum([
        len(grouped_form) for grouped_form in
        (functools.reduce(join_operation, form) for form in
        (map(lambda str_form: {char for char in str_form}, str_forms_group) for str_forms_group in
        (lines[i+1:j] for i, j in zip([-1] + split_indexes, split_indexes + [len(lines)]))))
    ])
    return total_count


def run_06():
    with open("inputs/d06.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    count_1 = parse_forms(lines, lambda a, b: a | b)
    print(count_1)
    count_2 = parse_forms(lines, lambda a, b: a & b)
    print(count_2)
    return

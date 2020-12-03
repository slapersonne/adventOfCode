import re


def read_input():
    with open("inputs/d02.txt") as f:
        return f.readlines()


def parse_line(line):
    regexp = r"(\d+)-(\d+) (\w): (\w+)"
    match = re.match(regexp, line)
    return match.groups()


def validate_first_rule(min_digits, max_digits, required_letter, password):
    letter_count = password.count(required_letter)
    return int(min_digits) <= letter_count <= int(max_digits)


def validate_second_rule(first_index, second_index, required_letter, password):
    is_letter_first_index = password[int(first_index) - 1] == required_letter
    is_letter_second_index = password[int(second_index) - 1] == required_letter
    return is_letter_first_index != is_letter_second_index


def get_matching_passwords(validation):
    lines = read_input()
    matching_passwords = [
        args[3] for args in (
            parse_line(line) for line in lines)
        if validation(*args)
    ]
    return matching_passwords


def run_02a():
    matching_passwords = get_matching_passwords(validate_first_rule)
    print(len(matching_passwords))


def run_02b():
    matching_passwords = get_matching_passwords(validate_second_rule)
    print(len(matching_passwords))

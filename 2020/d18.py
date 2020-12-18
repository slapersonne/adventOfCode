import functools
import re


def parse_operation_part(part, b_mode):
    if b_mode:
        while "+" in part:
            match = re.search(r"(\d+) \+ (\d+)", part)
            addition = sum([int(n) for n in match.groups()])
            part = part.replace(match.group(0), str(addition), 1)
    while "+" in part or "*" in part:
        match = re.search(r"(\d+) [\+\*] (\d+)", part)
        numbers = [int(n) for n in match.groups()]
        operation = int.__add__ if "+" in match.group(0) else int.__mul__
        part = part.replace(match.group(0), str(functools.reduce(operation, numbers)), 1)
    return int(part)


def parse_full_operation(line, b_mode):
    while "(" in line:
        final_sub_parts = re.findall(r"\(([^()]+)\)", line)
        for sub_part in final_sub_parts:
            line = line.replace("(" + sub_part + ")", str(parse_operation_part(sub_part, b_mode)), 1)
    result = parse_operation_part(line, b_mode)
    print(result)
    return result


def run(b_mode=False):
    lines = parse_lines()
    print(sum([parse_full_operation(line, b_mode) for line in lines]))
    return


def run_18a():
    run(b_mode=False)


def run_18b():
    run(b_mode=False)


def parse_lines():
    with open("inputs/d18.txt") as f:
        return [(line.strip()) for line in f.readlines()]
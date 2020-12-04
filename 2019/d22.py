import re


def stack(nb_cards, pos):
    return nb_cards - 1 - pos


def cut(nb_cards, pos, n):
    if n < 0:
        n = nb_cards + n
    if n <= pos:
        return pos - n
    else:
        return nb_cards - (n - pos)


def increment(nb_cards, pos, n):
    return pos*n % nb_cards


def parse_instruction(instruction):
    regexp = r".*(?P<instruction>increment|stack|cut) ?(?P<value>-?\d*).*"
    match = re.match(regexp, instruction)
    return match['instruction'], int(match['value'] if match['value'] else 0)


def run_22a():
    with open("inputs/d22.txt") as f:
        instructions = f.readlines()
    nb_cards = 10007
    pos = 2019
    for instruction in instructions:
        i, n = parse_instruction(instruction)
        if i == "stack":
            pos = stack(nb_cards, pos)
        elif i == "cut":
            pos = cut(nb_cards, pos, n)
        elif i == "increment":
            pos = increment(nb_cards, pos, n)
    print(pos)

import math
import re


def is_valid(str):
    adjacents = []
    for i in range(len(str) - 1):
        if str[i] > str[i + 1]:
            return False
        if str[i] == str[i+1]:
            if len(adjacents) == 0 or str[i] not in adjacents[len(adjacents) - 1]:
                adjacents.append(str[i] + str[i+1])
            else:
                adjacents[len(adjacents) - 1] = adjacents[len(adjacents) - 1] + str[i]
    return len([value for value in adjacents if len(value) == 2]) > 0


def run_04():
    valid_passwords = [i for i in range(359282, 799999) if is_valid(str(i))]
    print(len(valid_passwords))
    return

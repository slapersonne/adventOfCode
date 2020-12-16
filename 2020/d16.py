import functools
import re


class Rule:
    def __init__(self, name, first_range_start, first_range_end, second_range_start, second_range_end):
        self.name = name
        self.first_range = (int(first_range_start), int(first_range_end))
        self.second_range = (int(second_range_start), int(second_range_end))

    def is_valid(self, value):
        return self.first_range[0] <= value <= self.first_range[1] or \
               self.second_range[0] <= value <= self.second_range[1]


def check_value(rules, value):
    return any(map(lambda r: r.is_valid(value), rules))


def check_tickets(rules, tickets):
    invalid_values_sum = 0
    valid_tickets = []
    for ticket in tickets:
        if all(map(lambda v: check_value(rules, v), ticket)):
            valid_tickets.append(ticket)
            continue
        for value in ticket:
            if not check_value(rules, value):
                invalid_values_sum += value
    return valid_tickets, invalid_values_sum


def run_16a():
    rules, my_ticket, nearby_tickets = parse_lines()
    _, invalid_values_sum = check_tickets(rules, nearby_tickets)
    print(invalid_values_sum)
    return


def run_16b():
    rules, my_ticket, nearby_tickets = parse_lines()
    nearby_tickets, _ = check_tickets(rules, nearby_tickets)
    rules_candidates = {rule.name: [] for rule in rules}
    for rule in rules:
        for i in range(len(my_ticket)):
            if all(map(lambda v: rule.is_valid(v), [t[i] for t in nearby_tickets])):
                rules_candidates[rule.name].append(i)
    sorted_keys = sorted(rules_candidates, key=lambda r: len(rules_candidates[r]))
    rules_mappings, used_indexes = dict(), list()
    for key in sorted_keys:
        index = [i for i in rules_candidates[key] if i not in used_indexes][0]
        used_indexes.append(index)
        rules_mappings[key] = index
    selected_keys = [key for key in sorted_keys if key.startswith("departure")]
    selected_indexes = [rules_mappings[k] for k in selected_keys]
    print(functools.reduce(int.__mul__, [my_ticket[i] for i in selected_indexes]))


def parse_lines():
    with open("inputs/d16.txt") as f:
        lines = [""] + [line.strip() for line in f.readlines()]
    rules = [parse_rule(line) for line in lines[1:21]]
    my_ticket = parse_ticket(lines[23])
    nearby_tickets = [parse_ticket(line) for line in lines[26:]]
    return rules, my_ticket, nearby_tickets


def parse_rule(line):
    match = re.match(r"([ \w]+): (\d+)-(\d+) or (\d+)-(\d+)", line)
    return Rule(*match.groups())


def parse_ticket(line):
    return [int(value) for value in line.split(',')]

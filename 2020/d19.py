import re


def construct_regex_11_loop(rules, nb_loops=10):
    if nb_loops == 0:
        return f"({construct_regex_content(rules, 42)}{construct_regex_content(rules, 31)})?"
    return f"{construct_regex_content(rules, 42)}({construct_regex_11_loop(rules, nb_loops-1)})?{construct_regex_content(rules, 31)}"


def construct_regex_content(rules, index=0, b_mode=False):
    if b_mode:
        if index == 8:
            return f"({construct_regex_content(rules, 42, b_mode)})+"
        if index == 11:
            return construct_regex_11_loop(rules)
    final_match = re.match(r"\"([a-z])\"", rules[index])
    if final_match:
        return final_match.group(1)
    groups_match = re.match(r"^(?P<one_1>\d+)( (?P<one_2>\d+))?( \| (?P<two_1>\d+)( (?P<two_2>\d+))?)?$", rules[index])
    regexp = construct_regex_content(rules, int(groups_match['one_1']), b_mode)
    if groups_match["one_2"]:
        regexp = regexp + construct_regex_content(rules, int(groups_match['one_2']), b_mode)
    if groups_match["two_1"]:
        regexp = f"({regexp}|{construct_regex_content(rules, int(groups_match['two_1']), b_mode)})"
        if groups_match["two_2"]:
            regexp = regexp[:-1] + construct_regex_content(rules, int(groups_match['two_2']), b_mode) + ")"
    return regexp


def run_19(b_mode=False):
    rules, data = parse_lines()
    rules_regex = re.compile(f"^{construct_regex_content(rules, 0, b_mode)}$")
    regexp_count = sum([1 for line in data if rules_regex.match(line)])
    print(regexp_count)
    return


def run_19a():
    run_19(b_mode=False)


def run_19b():
    run_19(b_mode=True)


def parse_lines():
    with open("inputs/d19.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    separator_line = [i for i, v in enumerate(lines) if v == ""][0]
    rules, data = lines[:separator_line], lines[separator_line+1:]
    return parse_rules(rules), data


def parse_rules(rules_lines):
    return {
        int(key): value.strip()
        for key, value in (
        line.split(":") for line in rules_lines)}

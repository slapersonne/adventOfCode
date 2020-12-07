import functools
import re


def parse_rules():
    with open("inputs/d07.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    rules = dict()
    for line in lines:
        container, contents = re.match(r"([a-z]+ [a-z]+) bags contain (.*)\.", line).groups()
        parsed_contents = []
        if contents != "no other bags":
            for content in contents.split(", "):
                content_nb, content = re.match(r"(\d) ([a-z]+ [a-z]+) bags?", content).groups()
                content_nb = int(content_nb)
                parsed_contents.append((content_nb, content))
        rules[container] = parsed_contents
    return rules


def run_07a():
    rules = parse_rules()
    direct_parents = {key: set() for key in rules.keys()}
    for container, contents in rules.items():
        for _, content in contents:
            direct_parents[content].add(container)

    def get_all_parents(item):
        item_parents = direct_parents[item]
        if len(item_parents) == 0:
            return set()
        return functools.reduce(set.union, [
            {parent} | get_all_parents(parent)
            for parent in item_parents
        ])

    shiny_gold_parents = get_all_parents("shiny gold")
    print(len(shiny_gold_parents))
    return


def run_07b():
    rules = parse_rules()

    def get_needed_bags_count(item):
        contents = rules[item]
        if len(contents) == 0:
            return 0
        return sum([nb + nb * get_needed_bags_count(item) for nb, item in contents])

    total_bags = get_needed_bags_count("shiny gold")
    print(total_bags)

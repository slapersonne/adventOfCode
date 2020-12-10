import functools
from typing import List, Dict, Tuple


def run_10a():
    values = parse_values()
    diffs = [values[i+1] - value for i, value in enumerate(values[:-1])]
    one_diffs = len([diff for diff in diffs if diff == 1])
    three_diffs = len([diff for diff in diffs if diff == 3])
    print(f"{one_diffs} * {three_diffs} = {one_diffs * three_diffs}")


def run_10b():
    values = parse_values()
    values_chains = {
        value: [next_value for next_value in values[i+1:i+4] if next_value - value <= 3]
        for i, value in enumerate(values)
    }
    possible_sub_paths = [
        parse_subpath(values_chains, start, end)
        for start, end in get_crossroads_borders(values_chains)
    ]
    possible_paths = functools.reduce(int.__mul__, possible_sub_paths)
    print(possible_paths)


def parse_values() -> List[int]:
    with open("inputs/d10.txt") as f:
        sorted_lines = sorted([int(line.strip()) for line in f.readlines()])
    return [0] + sorted_lines + [sorted_lines[-1] + 3]


def parse_subpath(values_chains: Dict[int, List[int]], start: int, end: int) -> int:
    if start == end:
        return 1
    return sum([parse_subpath(values_chains, next_value, end) for next_value in values_chains[start]])


def get_crossroads_borders(values_chains: Dict[int, List[int]]) -> List[Tuple[int, int]]:
    crossroads_borders = list()
    for i, (value, next_values) in enumerate(values_chains.items()):
        if len(next_values) <= 1:
            continue
        if len(crossroads_borders) == 0 or value > crossroads_borders[-1][-1]:
            crossroads_borders.append((value, next_values[-1]))
            continue
        crossroads_borders[-1] = crossroads_borders[-1][0], next_values[-1]
    return crossroads_borders

import functools


def get_lines():
    with open("inputs/d03.txt") as f:
        return [line[:-1] for line in f.readlines()]


def count_encountered_trees(lines, right, down=1):
    lines_length = len(lines[0])
    encountered_trees = [
        "#"
        for i, line in enumerate(lines)
        if (i % down) == 0 and line[int((i * right / down) % lines_length)] == "#"
    ]
    return len(encountered_trees)


def run_03a():
    lines = get_lines()
    count = count_encountered_trees(lines, 3, 1)
    print(count)
    return


def run_03b():
    lines = get_lines()
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    counts = [
        count_encountered_trees(lines, *slope)
        for slope in slopes
    ]
    print(counts)
    total_count = functools.reduce(lambda a, b: a*b, counts)
    print(total_count)
    return

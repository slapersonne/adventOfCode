numbers = [2, 0, 6, 12, 1, 3]


def run(end):
    pass_numbers = {n: i+1 for i, n in enumerate(numbers[:-1])}
    last_number = numbers[-1]
    for i in range(6, end):
        current = i - pass_numbers[last_number] if last_number in pass_numbers else 0
        pass_numbers[last_number] = i
        last_number = current
    print(last_number)


def run_15a():
    run(end=2020)


def run_15b():
    run(end=30000000)

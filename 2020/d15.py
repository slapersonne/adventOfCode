numbers = [2, 0, 6, 12, 1, 3]


def run(end):
    pass_numbers = {n: i+1 for i, n in enumerate(numbers[:-1])}
    last_number = numbers[-1]
    for i in range(6, end):
        pass_numbers[last_number], last_number = i,  i - pass_numbers.get(last_number, i)
    print(last_number)


def run_15a():
    run(end=2020)


def run_15b():
    run(end=30000000)

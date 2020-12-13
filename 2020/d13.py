import functools


def run_13a():
    timestamp, bus_ids = parse_schedule()
    bus_ids = [int(v) for v in bus_ids if v != "x"]
    waiting_times = {
        bus_id: bus_id - (timestamp % bus_id)
        for bus_id in bus_ids
    }
    print(waiting_times)


def run_13b():
    _, bus_ids = parse_schedule()
    bus_ids_with_t = [(int(bus_id), t_diff) for t_diff, bus_id in enumerate(bus_ids) if bus_id != 'x']
    expected_moduli = {bus_id: (bus_id - t_diff) % bus_id for bus_id, t_diff in bus_ids_with_t}
    n = functools.reduce(int.__mul__, expected_moduli.keys())
    # ni = bus_id
    ni_hats = {ni: int(n/ni) for ni in expected_moduli.keys()}
    eis = {ni: next(vi * ni_hat for vi in range(ni) if (vi * ni_hat) % ni == 1)
           for ni, ni_hat in ni_hats.items()}
    t = functools.reduce(int.__add__, [expected_moduli[ni] * ei for ni, ei in eis.items()]) % n
    print(t)


def parse_schedule():
    with open("inputs/d13.txt") as f:
        timestamp = int(f.readline().strip())
        bus_ids = [v for v in f.readline().strip().split(',')]
        return timestamp, bus_ids

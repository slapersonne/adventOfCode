import re


def run_14a():
    lines = parse_instructions()
    mask = dict()
    memory = dict()
    for line in lines:
        if line.startswith("mask"):
            mask = parse_mask(line)
        else:
            address, value = parse_mem(line)
            value = get_masked_value(value, mask)
            memory[int(address)] = value
    print(sum(memory.values()))


def run_14b():
    lines = parse_instructions()
    mask = dict()
    memory = dict()
    for line in lines:
        if line.startswith("mask"):
            mask = parse_mask(line, ignore_x=False)
        else:
            address, value = parse_mem(line)
            addresses = get_masked_addresses(address, mask)
            for address in addresses:
                memory[address] = int(value)
    print(sum(memory.values()))


def parse_instructions():
    with open("inputs/d14.txt") as f:
        lines = [line.strip() for line in f.readlines()]
        return lines


def parse_mask(line, ignore_x=True):
    mask = line[7:]
    return {
        36 - i: c
        for i, c in enumerate(mask)
        if (c != "X" if ignore_x else True)
    }


def parse_mem(line):
    return re.match(r"mem\[(\d+)\] = (\d+)", line).groups()


def get_masked_value(value, mask):
    bits = list(format(int(value), "b"))
    for i, b in mask.items():
        if i > len(bits):
            bits = [b] + ["0" for _ in range(len(bits)+1, i)] + bits
        else:
            bits[-i] = b
    return int("".join(bits), 2)


def get_masked_addresses(address, mask):
    bits = list(format(int(address), "b").zfill(36))
    for i, b in mask.items():
        if b in "1X":
            bits[-i] = b
    masked_address = "".join(bits).lstrip("0")
    addresses = [""]
    for b in masked_address:
        new_addresses = []
        for start in addresses:
            for _b in ("01" if b == "X" else b):
                address = start + _b
                new_addresses.append(address)
        addresses = new_addresses
    return [int(address, 2) for address in addresses]

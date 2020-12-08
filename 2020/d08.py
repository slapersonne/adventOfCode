class Runner:

    def __init__(self, instructions=None):
        if not instructions:
            instructions = parse_instructions()
        self.acc = 0
        self.i = 0
        self.instructions = instructions
        self.parsed_instructions = set()

    def run(self):
        while True:
            if self.i in self.parsed_instructions:
                print(self.acc)
                return False
            if self.i >= len(self.instructions):
                print(self.acc)
                return True
            self.parsed_instructions.add(self.i)
            command, value = self.instructions[self.i]
            if command == "nop":
                self.i += 1
            elif command == "acc":
                self.i += 1
                self.acc += value
            elif command == "jmp":
                self.i += value


def parse_instructions():
    with open("inputs/d08.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    return [(line[:3], int(line[4:])) for line in lines]


def run_08a():
    runner = Runner()
    runner.run()


def run_08b():
    default_instructions = parse_instructions()
    nop_jmp_instructions = [i for i, (command, _) in enumerate(default_instructions) if command in ["nop", "jmp"]]
    for i in nop_jmp_instructions:
        alt_instructions = [instruction for instruction in default_instructions]
        command, value = default_instructions[i]
        command = "nop" if command == "jmp" else "jmp"
        alt_instructions[i] = command, value
        alt_runner = Runner(alt_instructions)
        is_success = alt_runner.run()
        if is_success:
            print(alt_runner.acc)
            return

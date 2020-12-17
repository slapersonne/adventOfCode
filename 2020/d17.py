class Life:
    def __init__(self, lines, nb_dimensions):
        self.nb_dimensions = nb_dimensions
        self.x_range = range(len(lines[0]))
        self.y_range = range(len(lines))
        self.z_range = range(1)
        self.w_range = range(1)
        self.actives = set(
            (x, y, 0, 0)
            for y, line in enumerate(lines)
            for x, value in enumerate(line)
            if value == "#")

    def get_neighbours(self, x, y, z, w):
        return [(a, b, c, d)
            for a in range(x-1, x+2)
            for b in range(y-1, y+2)
            for c in range(z-1, z+2)
            for d in range(w-1, w+2)
            if (a, b, c, d) != (x, y, z, w)]

    def get_active_neighbours(self, x, y, z, w):
        return [n for n in self.get_neighbours(x, y, z, w) if n in self.actives]

    def extend_ranges(self):
        self.x_range = range(self.x_range[0] - 1, self.x_range[-1] + 2)
        self.y_range = range(self.y_range[0] - 1, self.y_range[-1] + 2)
        self.z_range = range(self.z_range[0] - 1, self.z_range[-1] + 2) if self.nb_dimensions >= 3 else range(1)
        self.w_range = range(self.w_range[0] - 1, self.w_range[-1] + 2) if self.nb_dimensions >= 4 else range(1)

    def run(self):
        self.extend_ranges()
        deactivating = {
            cube
            for cube in self.actives
            if not 2 <= sum(1 for _ in self.get_active_neighbours(*cube)) <= 3
        }
        activating = {
            (a, b, c, d)
            for a in self.x_range
            for b in self.y_range
            for c in self.z_range
            for d in self.w_range
            if 3 == sum(1 for _ in self.get_active_neighbours(a, b, c, d))
        }
        for cube in deactivating:
            self.actives.remove(cube)
        for cube in activating:
            self.actives.add(cube)
        return self


def run(nb_dimensions):
    lines = parse_lines()
    life = Life(lines, nb_dimensions)
    for i in range(6):
        life.run()
    print(len(life.actives))
    return


def run_17a():
    run(nb_dimensions=3)


def run_17b():
    run(nb_dimensions=4)


def parse_lines():
    with open("inputs/d17.txt") as f:
        return [(line.strip()) for line in f.readlines()]
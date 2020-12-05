class Life:
    def __init__(self, alives):
        self.alives = alives
        self.height = len(alives)
        self.width = len(alives[0])

    def get_alive_neighbours(self, i, j):
        return [(x, y) for x, y in get_neighbours(i, j) if self[x, y]]

    def run(self):
        dying = {
            (i, j)
            for i in range(self.width)
            for j in range(self.height)
            if self[i, j] and sum(1 for _ in self.get_alive_neighbours(i, j)) != 1
        }
        popping = {
            (i, j)
            for i in range(self.width)
            for j in range(self.height)
            if not self[i, j] and sum(1 for _ in self.get_alive_neighbours(i, j)) in [1, 2]
        }
        for (i, j) in dying:
            self[i, j] = False
        for (i, j) in popping:
            self[i, j] = True

    def print(self):
        print()
        for j in range(self.height):
            print("".join(map(lambda b: "#" if b else ".", self.alives[j])))
        print(f"Life count: {self.count()}")

    def count(self):
        return sum([
            2 ** (self.width * i + j)
            for i in range(self.height)
            for j in range(self.width)
            if self[i,j]
        ])

    def __getitem__(self, i_j):
        return self.alives[i_j[0]][i_j[1]]

    def __setitem__(self, i_j, value):
        self.alives[i_j[0]][i_j[1]] = value


def get_neighbours(i, j):
    return [
        (x, y)
        for x in range(i-1, i+2)
        for y in range(j-1, j+2)
        if 0 <= x <= 4 and 0 <= y <= 4 and ((x == i) != (y == j))]


def run_24a():
    with open("inputs/d24.txt") as f:
        life = Life([
            list(map(lambda c: c == '#', line))
            for line in map(str.strip, f.readlines())])
    met_biodiversity = {life.count()}
    while True:
        life.run()
        count = life.count()
        if count in met_biodiversity:
            life.print()
            return
        else:
            met_biodiversity.add(count)


import copy


class Seats:
    def __init__(self, lines, b_version=False):
        self.height = len(lines)
        self.width = len(lines[0])
        self.occupied = [list(map(lambda c: None if c == "." else c == "#", line)) for line in lines]
        self.b_version = b_version

    def get_b_neighbours(self, i, j):
        neighbours = dict()
        for dist in range(1, max(self.width, self.width)):
            if i + dist < self.width and (None, True) not in neighbours and self[i + dist, j] is not None:
                neighbours[(None, True)] = (i + dist, j)
            if i + dist < self.width and j + dist < self.height and (False, True) not in neighbours \
                    and self[i + dist, j + dist] is not None:
                neighbours[(False, True)] = (i + dist, j + dist)
            if j + dist < self.height and (False, None) not in neighbours and self[i, j + dist] is not None:
                neighbours[(False, None)] = (i, j + dist)
            if i - dist >= 0 and j + dist < self.height and (False, False) not in neighbours \
                    and self[i - dist, j + dist] is not None:
                neighbours[(False, False)] = (i - dist, j + dist)
            if i - dist >= 0 and (None, False) not in neighbours and self[i - dist, j] is not None:
                neighbours[(None, False)] = (i - dist, j)
            if i - dist >= 0 and j - dist >= 0 and (True, False) not in neighbours \
                    and self[i - dist, j - dist] is not None:
                neighbours[(True, False)] = (i - dist, j - dist)
            if j - dist >= 0 and (True, None) not in neighbours and self[i, j - dist] is not None:
                neighbours[(True, None)] = (i, j - dist)
            if i + dist < self.width and j - dist >= 0 and (True, True) not in neighbours \
                    and self[i + dist, j - dist] is not None:
                neighbours[(True, True)] = (i + dist, j - dist)
            if len(neighbours) == 8:
                break
        return list(neighbours.values())

    def get_neighbours(self, i, j):
        return self.get_b_neighbours(i, j) if self.b_version else [
            (x, y)
            for x in range(i-1, i+2)
            for y in range(j-1, j+2)
            if 0 <= x < self.width and 0 <= y < self.height and (i, j) != (x, y)]

    def get_occupied_neighbours(self, i, j):
        return [(x, y) for x, y in self.get_neighbours(i, j) if self[x, y]]

    def get_occupied_seats_count(self):
        return sum([
            1 if self[i, j] else 0
            for j in range(self.height)
            for i in range(self.width)])

    def run(self):
        leaving = {
            (i, j)
            for i in range(self.width)
            for j in range(self.height)
            if self[i, j] and sum(1 for _ in self.get_occupied_neighbours(i, j)) >= (5 if self.b_version else 4)
        }
        occupying = {
            (i, j)
            for i in range(self.width)
            for j in range(self.height)
            if self[i, j] is False and sum(1 for _ in self.get_occupied_neighbours(i, j)) == 0
        }
        for (i, j) in leaving:
            self[i, j] = False
        for (i, j) in occupying:
            self[i, j] = True
        return self

    def __getitem__(self, i_j):
        return self.occupied[i_j[0]][i_j[1]]

    def __setitem__(self, i_j, value):
        self.occupied[i_j[0]][i_j[1]] = value

    def __eq__(self, other):
        return all([
            self[i, j] == other[i, j]
            for j in range(self.height)
            for i in range(self.width)
        ])


def run_11(b_version=False):
    lines = parse_lines()
    seats = Seats(lines, b_version)
    previous_seats = copy.deepcopy(seats)
    is_ended = False
    while not is_ended:
        print(seats.get_occupied_seats_count())
        seats.run()
        is_ended = (seats == previous_seats)
        previous_seats = copy.deepcopy(seats)
    print(seats.get_occupied_seats_count())


def parse_lines():
    with open("inputs/d11.txt") as f:
        return [(line.strip()) for line in f.readlines()]
def run_12a():
    instructions = parse_instructions()
    x, y = 0, 0
    course = 90
    for instruction in instructions:
        order, value = instruction[:1], int(instruction[1:])
        if order == "N":
            y += value
        elif order == "E":
            x += value
        elif order == "W":
            x -= value
        elif order == "S":
            y -= value
        elif order == "L":
            course = (course - value) % 360
        elif order == "R":
            course = (course + value) % 360
        elif order == "F":
            if course == 0:
                y += value
            elif course == 90:
                x += value
            elif course == 270:
                x -= value
            elif course == 180:
                y -= value
            else:
                raise ValueError(f"course is {course}")
        else:
            raise ValueError(f"order is {order}")
    print(f"distance for ({x}, {y}) is {abs(x) + abs(y)}")



def run_12b():
    instructions = parse_instructions()
    wx, wy = 10, 1
    x, y = 0, 0
    for instruction in instructions:
        order, value = instruction[:1], int(instruction[1:])
        if order == "N":
            wy += value
        elif order == "E":
            wx += value
        elif order == "W":
            wx -= value
        elif order == "S":
            wy -= value
        elif order in ["L", "R"]:
            if order == "L":
                value = (360 - value) % 360
            else:
                value = value % 360
            if value == 90:
                wx, wy = wy, -wx
            elif value == 180:
                wx, wy = -wx, -wy
            elif value == 270:
                wx, wy = -wy, wx
        elif order == "F":
            x += (wx * value)
            y += (wy * value)
        else:
            raise ValueError(f"order is {order}")
    print(f"distance for ({x}, {y}) is {abs(x) + abs(y)}")


def parse_instructions():
    with open("inputs/d12.txt") as f:
        return [line.strip() for line in f.readlines()]

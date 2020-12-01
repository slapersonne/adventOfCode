import math
import re


map = [
    ".#......##.#..#.......#####...#..",
    "...#.....##......###....#.##.....",
    "..#...#....#....#............###.",
    ".....#......#.##......#.#..###.#.",
    "#.#..........##.#.#...#.##.#.#.#.",
    "..#.##.#...#.......#..##.......##",
    "..#....#.....#..##.#..####.#.....",
    "#.............#..#.........#.#...",
    "........#.##..#..#..#.#.....#.#..",
    ".........#...#..##......###.....#",
    "##.#.###..#..#.#.....#.........#.",
    ".#.###.##..##......#####..#..##..",
    ".........#.......#.#......#......",
    "..#...#...#...#.#....###.#.......",
    "#..#.#....#...#.......#..#.#.##..",
    "#.....##...#.###..#..#......#..##",
    "...........#...#......#..#....#..",
    "#.#.#......#....#..#.....##....##",
    "..###...#.#.##..#...#.....#...#.#",
    ".......#..##.#..#.............##.",
    "..###........##.#................",
    "###.#..#...#......###.#........#.",
    ".......#....#.#.#..#..#....#..#..",
    ".#...#..#...#......#....#.#..#...",
    "#.#.........#.....#....#.#.#.....",
    ".#....#......##.##....#........#.",
    "....#..#..#...#..##.#.#......#.#.",
    "..###.##.#.....#....#.#......#...",
    "#.##...#............#..#.....#..#",
    ".#....##....##...#......#........",
    "...#...##...#.......#....##.#....",
    ".#....#.#...#.#...##....#..##.#.#",
    ".#.#....##.......#.....##.##.#.##"]

width = len(map[0])
height = len(map)

asteroids = [
    (x, y)
    for x in range(0, width)
    for y in range(0, height) if map[y][x] == "#"
]
# print(asteroids)


def get_asteroids_with_tan(center, other_asteroids):
    x, y = center
    asteroids_with_tan = {}
    for i, j in other_asteroids:
        key = (y - j)/(x - i) if (x - i) != 0 else -99
        if key in asteroids_with_tan:
            asteroids_with_tan[key].append((i,j))
        else:
            asteroids_with_tan[key] = [(i,j)]
    for same_tan_asteroids in asteroids_with_tan.values():
        same_tan_asteroids.sort(key=lambda asteroid: abs(x - asteroid[0]) + abs(y - asteroid[1]), reverse=True)
    return asteroids_with_tan


def get_left_asteroids(asteroid):
    x, y = asteroid
    left_asteroids = [(i, j) for i, j in asteroids if i < x or (i == x and j > y)]
    return get_asteroids_with_tan(asteroid, left_asteroids)
    

def get_right_asteroids(asteroid):
    x, y = asteroid
    right_asteroids = [(i, j) for i, j in asteroids if i > x or (i == x and j < y)]
    return get_asteroids_with_tan(asteroid, right_asteroids)


def run_10a():
    maximum = 0
    best_asteroid = (0, 0)
    for asteroid in asteroids:
        upper_visible_asteroids = get_left_asteroids(asteroid)
        lower_visible_asteroids = get_right_asteroids(asteroid)
        visible_asteroids_nb = len(upper_visible_asteroids) + len(lower_visible_asteroids)
        print(visible_asteroids_nb)
        if visible_asteroids_nb > maximum:
            print("New maximum !")
            maximum = visible_asteroids_nb
            best_asteroid = asteroid

    print(f"Maximum = {maximum} ({best_asteroid})")


def destroy_asteroid(asteroids, key):
    asteroid_to_destroy = asteroids[key].pop()
    print(f"Destroying {asteroid_to_destroy} (angle = {key})")


def run_10b():
    best_asteroid = (29, 28)
    left_asteroids = get_left_asteroids(best_asteroid)
    left_asteroids = {key: left_asteroids[key] for key in sorted(left_asteroids)}
    right_asteroids = get_right_asteroids(best_asteroid)
    right_asteroids = {key: right_asteroids[key] for key in sorted(right_asteroids)}
    i = 0
    print(right_asteroids)
    print(left_asteroids)
    while True:
        for key in sorted(right_asteroids):
            i += 1
            print(f"i = {i}")
            destroy_asteroid(right_asteroids, key)
            if i == 200:
                return
        right_asteroids = {key: value for key, value in right_asteroids.items() if len(value) > 0}
        for key in sorted(left_asteroids):
            i += 1
            print(f"i = {i}")
            destroy_asteroid(left_asteroids, key)
            if i == 200:
                return
        left_asteroids = {key: value for key, value in left_asteroids.items() if len(value) > 0}

        


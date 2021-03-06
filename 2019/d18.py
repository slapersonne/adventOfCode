import math
import re
from random import randrange

map_str = [
    "#################################################################################",
    "#.................C...#...#.......#.....#.#.........#.R.....#.....B............t#",
    "#.###################.#.#.###.#.###.#.#V#.#.#####.#.#.#####.#.#####.###########.#",
    "#...Z...#.......#.....#.#...#.#...#.#.#.#.#.#.#...#.#.#...#...#...#.#.....#.#...#",
    "#.#####.#.#####.#.#####.###.#.###.#.#.###.#.#.#.#####.#.#.#####.#.#.#.###.#.#.###",
    "#.#.....#k..#...#...#...#.#.#...#...#...#...#.#.......#.#.....#.#n#.....#.#...#.#",
    "#.#.#.#####.#.#####.#.#.#.#.#.#########.#.###.#########.#.#####.#.#######.#.###.#",
    "#.#.#.#.....#.#...F.#.#.#...#.#...#...#.#.#............m#.#.....#.......#.#.#...#",
    "#.#.###.#####.#.#######.#.#####.#.#.#.#.#.#####.#####.#####.###########.#.#.#.#.#",
    "#.#...#.#.....#...#.....#.......#.#.#.#.#.....#.#...#.#.....#.....#.......#.#.#.#",
    "#.###.#.#.#######.#.#############.#.#.#.#####.#.#.#.###.#####.###.#########.#.#.#",
    "#.#...#.#.......#.#...#...#.....#.#.#.#.#...#...#.#.#...#..q..#.#.#.....#.....#.#",
    "#.#.###.#######.#.#.#.###.#.#.###.#.#.#.#.#.#.###.#.#.###.#####.#.#.###.#######.#",
    "#.#...........#.#.#.#...#...#...#.#.#...#.#.#.#...#...#...#.....#...#.#w..#...#i#",
    "#.###########.#.#.#####.#.#####.#.#.###U###.#.#.#######.###.#########.###.#.#.###",
    "#...#.#.....#.#.#.......#.#...#.#.#...#.#...#.#.....#...#.........#.....#...#...#",
    "###.#.#.###.#.#.#########.###.#.#.#.#.#.#.###.#####.#.#.#####.#.###.#.#########.#",
    "#.#.#.#.#.#.#.#.#.......#.....#.#.#.#.#.#...#.#...#.#.#.#...#.#.#...#s......#...#",
    "#.#.#.#.#.#.###.#####.#.#####.#.#.###.#.#.#.#.#.###.#.###.#.#.#.#.#######.###.###",
    "#.....#.#.......#...#.#...#...#...#...#.#.#...#...#.#.....#.#.#...#..x..#....d#.#",
    "#######.#########.#.#####.#.#######.###.#.#######.#.#######J###.###.###.#######.#",
    "#.....#...#...#.S.#.#j..#...........#.#.#.#.......#.#.....#...#...#.#.#.#.#.....#",
    "#.###.###.#.#.#.###.###.#############.#.#.#.#####.#.#.#.#########.#.#.#.#.#.#.#.#",
    "#.#.....#.#.#.....#...#.......#.........#...#.....#...#.........#...#...#.#.#.#.#",
    "#.#####.#.#.#######.#.#######.###.###########.###########.#.#########.###.#.#.###",
    "#.#.E.#.#.#.#...#...#...#...#...#.....#.#.....#...........#.#.....#...#..e..#...#",
    "#.#.#.#.#H#X#.#.#.#.#####W#.###Q#####.#.#.#####.###.#########.###.#.###########.#",
    "#...#.#...#.#.#.#.#.#...#.#...#.#...#.#.#...#.#...#.#...#...#.#.#.#.............#",
    "#####.#####.#.#.#.###.#.#.###.#.#.###.#.###.#.###.#.#.#.#.#.#.#.#.#############.#",
    "#...#.#.....#.#.#...D.#...#.#.#.#.....#.#...#...#.#.#.#...#...#.#.#...........#.#",
    "###.#.#.#####.#############.#.#.#.#####.#.#####.#.###.#########.#.#.###.#.#####.#",
    "#...#...#..........o........#...#......g#.....#.#.....#...#.#...#.#.#.K.#.#....h#",
    "#.#.#####.###########.#################.#####.#.#######.#.#.#.#.#.#.#.#####.#####",
    "#.#.....#.#.....#...#.........#.......#.#.#...#.....#...#.#...#.#...#...#...#...#",
    "#.#######.###.#.#.#.#######.#.#######.#.#.#.###.###.#.###.#####.#######.#.#####.#",
    "#.#.....#...#.#...#...#...#.#.........#.#.#...#...#.#.#...........#.....#.....#.#",
    "#.#.###.###.#.#######.#.###.#####.#####.#.###.#.#.#.#.###########.#.#########.#.#",
    "#.#.#.#...#...#.#.....#...#.....#.#.....#.#...#.#.#.#...#.........#.#.........#.#",
    "#.#.#.###.#####.#.#######.#####.###.#####.#.#####.#.###.#.#########.#.#########.#",
    "#.......#.....................#...................#.....#.........#.............#",
    "#######################################.@.#######################################",
    "#.......#...........#.....#.....................#.....#.......#...........#.....#",
    "#.#######.#.#######.#.###.#.#####.#####.#.#.#####.#.#.#######.#.#########.#####.#",
    "#.#.......#.....#...#...#.#.#...#.....#.#.#.......#.#.........#.#.......#...#...#",
    "#.#.###########.#.#####.###.#.#.#####.#.#.#####.###.###########.#.###.#.###.#.###",
    "#b..#...........#.....#...#.#.#.#.#...#.#.#...#...#...#.........#.#...#.#...#...#",
    "#.###.###############.###.#.#.#.#.#.###.###.#.#######.#.#########.#.#.###.#####.#",
    "#...#...........#...#.#...#.#.#...#.#...#...#.......#.#.#.......#.#.#.#...#.....#",
    "###.###########.###.#.#.#.#.#.###.#.###.#.#########.#.#.#.#####.###.#.#.###.###.#",
    "#.............#...#.....#.#...#...#...#.#.#.#.....#.#.#.#.#...#.....#.#....l#...#",
    "#.#########.#####.#####.#######.#####G#.#.#.#.#O###.#.#.#.#.#.#.#####.#######.###",
    "#.#...#...#.#...#...#...#.....#...#...#.#.#.#.#...#...#.#.#.#.#.#.Y.#.......#.#.#",
    "#.#.#.#.#.###.#.#.#.###.#.###.###.#.###.#.#.#.###.#.###.#.#.#.###.#.#######.#.#.#",
    "#.#.#a..#.....#.#.#...#.#.#.#.....#.#.#.#.#.#...#...#...#.#.#.....#.....#...#.#.#",
    "###.###########.#####.###.#.#####.#.#.#.#.#.###.#####.###.#.###########.#.###.#.#",
    "#...#..y#.....#.#...#.......#...#.#.#...#.#.........#.#.......#.#.......#.#...#.#",
    "#.###.#.#.#.#.#.#.#.#.#######.#.#.#.###.#.#.#########.#######.#.#.#######.#.###.#",
    "#.....#.#.#.#.#...#.#.#.......#.#.#...#.#.#.#.......#.....#z#.#.#.#.....#.#p..#.#",
    "#######.###.#######.#.#.#######.#####.###.###.#####.#####.#.#.#.#A#.###.#.###.#.#",
    "#.....#.....#.....#.#.#.....#.......#...#...#...#.....#...#.....#.#...#.....#.#.#",
    "#.###.#####.#.###.#.#######.#######.###.#.#.#.###.###.#.#######.#.#.#########.#.#",
    "#...#.......#.#.#...#.....#...#...#...#.#.#...#...#...#.......#.#.#.#.........#.#",
    "###.#########.#.#.#######.#.#.###.###.#.#.#####.###.###########.#.###.#########.#",
    "#...#...#...P.#...#.......#.#...#.#...#.#.#.....#...#.......#.#.#.....#...#.....#",
    "#.###.###.###.#####.#########.#.#.#.###.#.#.#######.#.#####.#.#.#######.#.#####.#",
    "#.....#...#...#.....#.......#.#.#...#...#.#.......#...#...#...#.#.......#.......#",
    "#####.#.###.###.#####.#####.###.###.#.#.#.#######.#####.#.###.#.###.###.#########",
    "#...#c#...#.#...#.....#...#...#...#.#.#u#.#.....#.....#.#.....#...#...#.#.......#",
    "###.#.###.###.###.#####.#####.###.#.#.#.#.#.###.#####.#.#########.###.#.#.#####.#",
    "#...#...#.L.#.#.#...#.......#.#...#...#.#.#.#.#.#...#.#.....#...#.#...#.......#.#",
    "#.#####.###.#.#.#.#.#.#####.#.#.#######.#.#.#.#.###.#.#####.#.#.#.#.#####.#####.#",
    "#...#...#.#...#...#.#.....#.#.#.#.....#.#.#.#.#.....#...#...#.#...#.#...#.#...#.#",
    "###.#.###.#########.###.###.#.#.#####.#.#.#.#.#####.###.#.###.#######.#.###.#.#.#",
    "#...#...#.........#...#.#...#...#.....#.#...#.#...#.#.#.#.#...#.....#.#...N.#.#.#",
    "#.#####.#.#####.#.###.#.#.#######.#####.#####.#.#.#.#.#.###.###.###.#.#######.#T#",
    "#.I.#...#.#.....#.....#.#...#...#.......#.#.....#.#.#.#...#.#.....#...#...#...#.#",
    "#.#.#.###.#.###############.#.#.#.#######.#.#####.#.#.###.#.#####.#####.#.#.###.#",
    "#.#...#...#.#.....#.........#.#.#...#...#...#...#.#.#...#.#f......#.#...#.#.....#",
    "#.#########.#.#####.###.#####.#.###.#.#.#.###.#.#.#.###.#.#########.#.#.#######.#",
    "#...........#..r....M.#.......#v......#.#.....#.#.......#.............#.........#",
    "#################################################################################"
]
map_str_2 = [
    "#################",
    "#i.G..c...e..H.p#",
    "########.########",
    "#j.A..b...f..D.o#",
    "########@########",
    "#k.E..a...g..B.n#",
    "########.########",
    "#l.F..d...h..C.m#",
    "#################"
]
map_str_b = [
    "#################################################################################",
    "#.................C...#...#.......#.....#.#.........#.R.....#.....B............t#",
    "#.###################.#.#.###.#.###.#.#V#.#.#####.#.#.#####.#.#####.###########.#",
    "#...Z...#.......#.....#.#...#.#...#.#.#.#.#.#.#...#.#.#...#...#...#.#.....#.#...#",
    "#.#####.#.#####.#.#####.###.#.###.#.#.###.#.#.#.#####.#.#.#####.#.#.#.###.#.#.###",
    "#.#.....#k..#...#...#...#.#.#...#...#...#...#.#.......#.#.....#.#n#.....#.#...#.#",
    "#.#.#.#####.#.#####.#.#.#.#.#.#########.#.###.#########.#.#####.#.#######.#.###.#",
    "#.#.#.#.....#.#...F.#.#.#...#.#...#...#.#.#............m#.#.....#.......#.#.#...#",
    "#.#.###.#####.#.#######.#.#####.#.#.#.#.#.#####.#####.#####.###########.#.#.#.#.#",
    "#.#...#.#.....#...#.....#.......#.#.#.#.#.....#.#...#.#.....#.....#.......#.#.#.#",
    "#.###.#.#.#######.#.#############.#.#.#.#####.#.#.#.###.#####.###.#########.#.#.#",
    "#.#...#.#.......#.#...#...#.....#.#.#.#.#...#...#.#.#...#..q..#.#.#.....#.....#.#",
    "#.#.###.#######.#.#.#.###.#.#.###.#.#.#.#.#.#.###.#.#.###.#####.#.#.###.#######.#",
    "#.#...........#.#.#.#...#...#...#.#.#...#.#.#.#...#...#...#.....#...#.#w..#...#i#",
    "#.###########.#.#.#####.#.#####.#.#.###U###.#.#.#######.###.#########.###.#.#.###",
    "#...#.#.....#.#.#.......#.#...#.#.#...#.#...#.#.....#...#.........#.....#...#...#",
    "###.#.#.###.#.#.#########.###.#.#.#.#.#.#.###.#####.#.#.#####.#.###.#.#########.#",
    "#.#.#.#.#.#.#.#.#.......#.....#.#.#.#.#.#...#.#...#.#.#.#...#.#.#...#s......#...#",
    "#.#.#.#.#.#.###.#####.#.#####.#.#.###.#.#.#.#.#.###.#.###.#.#.#.#.#######.###.###",
    "#.....#.#.......#...#.#...#...#...#...#.#.#...#...#.#.....#.#.#...#..x..#....d#.#",
    "#######.#########.#.#####.#.#######.###.#.#######.#.#######J###.###.###.#######.#",
    "#.....#...#...#.S.#.#j..#...........#.#.#.#.......#.#.....#...#...#.#.#.#.#.....#",
    "#.###.###.#.#.#.###.###.#############.#.#.#.#####.#.#.#.#########.#.#.#.#.#.#.#.#",
    "#.#.....#.#.#.....#...#.......#.........#...#.....#...#.........#...#...#.#.#.#.#",
    "#.#####.#.#.#######.#.#######.###.###########.###########.#.#########.###.#.#.###",
    "#.#.E.#.#.#.#...#...#...#...#...#.....#.#.....#...........#.#.....#...#..e..#...#",
    "#.#.#.#.#H#X#.#.#.#.#####W#.###Q#####.#.#.#####.###.#########.###.#.###########.#",
    "#...#.#...#.#.#.#.#.#...#.#...#.#...#.#.#...#.#...#.#...#...#.#.#.#.............#",
    "#####.#####.#.#.#.###.#.#.###.#.#.###.#.###.#.###.#.#.#.#.#.#.#.#.#############.#",
    "#...#.#.....#.#.#...D.#...#.#.#.#.....#.#...#...#.#.#.#...#...#.#.#...........#.#",
    "###.#.#.#####.#############.#.#.#.#####.#.#####.#.###.#########.#.#.###.#.#####.#",
    "#...#...#..........o........#...#......g#.....#.#.....#...#.#...#.#.#.K.#.#....h#",
    "#.#.#####.###########.#################.#####.#.#######.#.#.#.#.#.#.#.#####.#####",
    "#.#.....#.#.....#...#.........#.......#.#.#...#.....#...#.#...#.#...#...#...#...#",
    "#.#######.###.#.#.#.#######.#.#######.#.#.#.###.###.#.###.#####.#######.#.#####.#",
    "#.#.....#...#.#...#...#...#.#.........#.#.#...#...#.#.#...........#.....#.....#.#",
    "#.#.###.###.#.#######.#.###.#####.#####.#.###.#.#.#.#.###########.#.#########.#.#",
    "#.#.#.#...#...#.#.....#...#.....#.#.....#.#...#.#.#.#...#.........#.#.........#.#",
    "#.#.#.###.#####.#.#######.#####.###.#####.#.#####.#.###.#.#########.#.#########.#",
    "#.......#.....................#........@#@........#.....#.........#.............#",
    "#################################################################################",
    "#.......#...........#.....#............@#@......#.....#.......#...........#.....#",
    "#.#######.#.#######.#.###.#.#####.#####.#.#.#####.#.#.#######.#.#########.#####.#",
    "#.#.......#.....#...#...#.#.#...#.....#.#.#.......#.#.........#.#.......#...#...#",
    "#.#.###########.#.#####.###.#.#.#####.#.#.#####.###.###########.#.###.#.###.#.###",
    "#b..#...........#.....#...#.#.#.#.#...#.#.#...#...#...#.........#.#...#.#...#...#",
    "#.###.###############.###.#.#.#.#.#.###.###.#.#######.#.#########.#.#.###.#####.#",
    "#...#...........#...#.#...#.#.#...#.#...#...#.......#.#.#.......#.#.#.#...#.....#",
    "###.###########.###.#.#.#.#.#.###.#.###.#.#########.#.#.#.#####.###.#.#.###.###.#",
    "#.............#...#.....#.#...#...#...#.#.#.#.....#.#.#.#.#...#.....#.#....l#...#",
    "#.#########.#####.#####.#######.#####G#.#.#.#.#O###.#.#.#.#.#.#.#####.#######.###",
    "#.#...#...#.#...#...#...#.....#...#...#.#.#.#.#...#...#.#.#.#.#.#.Y.#.......#.#.#",
    "#.#.#.#.#.###.#.#.#.###.#.###.###.#.###.#.#.#.###.#.###.#.#.#.###.#.#######.#.#.#",
    "#.#.#a..#.....#.#.#...#.#.#.#.....#.#.#.#.#.#...#...#...#.#.#.....#.....#...#.#.#",
    "###.###########.#####.###.#.#####.#.#.#.#.#.###.#####.###.#.###########.#.###.#.#",
    "#...#..y#.....#.#...#.......#...#.#.#...#.#.........#.#.......#.#.......#.#...#.#",
    "#.###.#.#.#.#.#.#.#.#.#######.#.#.#.###.#.#.#########.#######.#.#.#######.#.###.#",
    "#.....#.#.#.#.#...#.#.#.......#.#.#...#.#.#.#.......#.....#z#.#.#.#.....#.#p..#.#",
    "#######.###.#######.#.#.#######.#####.###.###.#####.#####.#.#.#.#A#.###.#.###.#.#",
    "#.....#.....#.....#.#.#.....#.......#...#...#...#.....#...#.....#.#...#.....#.#.#",
    "#.###.#####.#.###.#.#######.#######.###.#.#.#.###.###.#.#######.#.#.#########.#.#",
    "#...#.......#.#.#...#.....#...#...#...#.#.#...#...#...#.......#.#.#.#.........#.#",
    "###.#########.#.#.#######.#.#.###.###.#.#.#####.###.###########.#.###.#########.#",
    "#...#...#...P.#...#.......#.#...#.#...#.#.#.....#...#.......#.#.#.....#...#.....#",
    "#.###.###.###.#####.#########.#.#.#.###.#.#.#######.#.#####.#.#.#######.#.#####.#",
    "#.....#...#...#.....#.......#.#.#...#...#.#.......#...#...#...#.#.......#.......#",
    "#####.#.###.###.#####.#####.###.###.#.#.#.#######.#####.#.###.#.###.###.#########",
    "#...#c#...#.#...#.....#...#...#...#.#.#u#.#.....#.....#.#.....#...#...#.#.......#",
    "###.#.###.###.###.#####.#####.###.#.#.#.#.#.###.#####.#.#########.###.#.#.#####.#",
    "#...#...#.L.#.#.#...#.......#.#...#...#.#.#.#.#.#...#.#.....#...#.#...#.......#.#",
    "#.#####.###.#.#.#.#.#.#####.#.#.#######.#.#.#.#.###.#.#####.#.#.#.#.#####.#####.#",
    "#...#...#.#...#...#.#.....#.#.#.#.....#.#.#.#.#.....#...#...#.#...#.#...#.#...#.#",
    "###.#.###.#########.###.###.#.#.#####.#.#.#.#.#####.###.#.###.#######.#.###.#.#.#",
    "#...#...#.........#...#.#...#...#.....#.#...#.#...#.#.#.#.#...#.....#.#...N.#.#.#",
    "#.#####.#.#####.#.###.#.#.#######.#####.#####.#.#.#.#.#.###.###.###.#.#######.#T#",
    "#.I.#...#.#.....#.....#.#...#...#.......#.#.....#.#.#.#...#.#.....#...#...#...#.#",
    "#.#.#.###.#.###############.#.#.#.#######.#.#####.#.#.###.#.#####.#####.#.#.###.#",
    "#.#...#...#.#.....#.........#.#.#...#...#...#...#.#.#...#.#f......#.#...#.#.....#",
    "#.#########.#.#####.###.#####.#.###.#.#.#.###.#.#.#.###.#.#########.#.#.#######.#",
    "#...........#..r....M.#.......#v......#.#.....#.#.......#.............#.........#",
    "#################################################################################"
]
all_distances = {}
shortest_paths = {}
keys_positions = {}
full_map = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"


def run_18(input_str):
    for y, line in enumerate(input_str):
        for x in range(0, len(line)):
            full_map[(x, y)] = line[x]
    keys_positions.update({value: position for position, value in full_map.items() if value in alphabet})


def get_dependencies(origin):
    access_paths = {origin: ""}
    not_ended = True

    while not_ended:
        not_ended = False

        for position, value in full_map.items():

            if value == "#" or position not in access_paths:
                continue

            if value in alphabet.upper() and value not in access_paths[position]:
                not_ended = True
                access_paths[position] = access_paths[position] + value

            current_access_paths = access_paths[position]
            x, y = position
            neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

            for neighbour in neighbours:
                neighbour_value = full_map[neighbour]
                if neighbour_value == "#":
                    continue

                if neighbour not in access_paths:
                    not_ended = True
                    if neighbour_value in alphabet.upper():
                        access_paths[neighbour] = current_access_paths + neighbour_value
                    else:
                        access_paths[neighbour] = current_access_paths

                else:
                    neighbour_access_paths = access_paths[neighbour]
                    value = "" if value == "." else value
                    neighbour_value = "" if neighbour_value == "." else neighbour_value
                    if not (current_access_paths == neighbour_access_paths
                            or current_access_paths == neighbour_access_paths + value
                            or neighbour_access_paths == current_access_paths + neighbour_value):
                        print("WARNING!! POTENTIAL LOOP DETECTED!")
                        print(f"Position = {position}")
                        print(f"N. Position = {neighbour}")
                        print(f"Value = {value}")
                        print(f"N. Value = {neighbour_value}")
                        print(f"Access paths : {access_paths[position]}")
                        print(f"N. Access paths : {access_paths[neighbour]}")

    return access_paths


def get_accessible_keys(key_dependencies, available_keys):
    accessible_keys = []
    for key in key_dependencies:
        if key in available_keys:
            continue
        is_key_available = True
        for dependency in key_dependencies[key]:
            if not dependency.lower() in available_keys:
                is_key_available = False
                break
        if is_key_available:
            accessible_keys.append(key)
    return accessible_keys


def get_key_distances(origin):
    origin_value = full_map[origin]
    needed_keys = "".join([key for key in alphabet if key != origin_value])
    keys_distances = {}
    for key in needed_keys:
        key_position = keys_positions[key]
        p1, p2 = sorted((origin, key_position))
        if (p1, p2) in all_distances:
            keys_distances[key] = all_distances[(p1, p2)]
    distance = 0
    computed_values = {origin: full_map[origin]}
    if len(keys_distances) < len(needed_keys):
        print(f"New key computed : {origin_value} ({len(keys_distances)} already computed.)")
    while len(keys_distances) != len(needed_keys):
        distance += 1
        new_computed_values = {}
        for position, value in computed_values.items():
            x, y = position
            neighbours = [neighbour
                          for neighbour in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
                          if full_map[neighbour] != "#" and neighbour not in computed_values]
            for neighbour in neighbours:
                neighbour_value = full_map[neighbour]
                new_computed_values[neighbour] = neighbour_value
        for position, value in new_computed_values.items():
            if value in needed_keys:
                p1, p2 = sorted((origin, position))
                all_distances[(p1, p2)] = distance
                keys_distances[value] = distance
        computed_values.update(new_computed_values)
    return keys_distances


def get_shortest_path(key_dependencies, position, available_keys):
    if randrange(0, 100000) == 42:
        print(f"Keys path = {available_keys}")
    accessible_keys = get_accessible_keys(key_dependencies, available_keys)

    if len(accessible_keys) == 0:
        final_path = ("", 0)
        if len(available_keys) < 26:
            print(f"ERROR, missing keys ({len(available_keys)} < 26)")
        return final_path

    accessible_keys_distances = []
    for key in accessible_keys:
        p1, p2 = sorted((position, keys_positions[key]))
        distance = all_distances[(p1, p2)]
        accessible_keys_distances.append((key, distance))

    current_key = full_map[position]
    remaining_keys = "".join([letter for letter in alphabet if letter not in available_keys])
    remaining_path = current_key + remaining_keys
    if len(remaining_path) > 1 and remaining_path in shortest_paths:
        shortest_path = shortest_paths[remaining_path]
        print(f"Get already computed path for {remaining_path} : {shortest_path}")
        return shortest_path

    shortest_path, min_distance = (None, 9999)
    for key, distance in accessible_keys_distances:
        shortest_sub_path, sub_distance = get_shortest_path(key_dependencies, keys_positions[key], available_keys + key)
        path_distance = distance + sub_distance

        if path_distance < min_distance:
            shortest_path, min_distance = current_key + shortest_sub_path, path_distance

    if len(remaining_path) > 1:
        shortest_paths[remaining_path] = shortest_path, min_distance
    return shortest_path, min_distance


def run_18a():
    run_18(map_str)
    origin = [position for position, value in full_map.items() if value == "@"].pop()
    get_key_distances(origin)
    for key in alphabet:
        get_key_distances(keys_positions[key])

    dependencies = get_dependencies(origin)
    key_dependencies = {full_map[key]: value for key, value in dependencies.items() if
                        full_map[key] in alphabet}

    for key in sorted(key_dependencies):
        print(f"{key}: {key_dependencies[key]}")

    shortest_path = get_shortest_path(key_dependencies, origin, "")

    print()
    print()
    print(f"Best path : {shortest_path}")


def run_18b():
    run_18(map_str_b)
    print(full_map)
    print(full_map[(40, 40)])
    print(full_map[(40, 39)])
    print(full_map[(40, 41)])
    return

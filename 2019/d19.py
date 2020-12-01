import math
import re

from intcode import IntCodeRunner

initial_instructions = [109,424,203,1,21101,0,11,0,1106,0,282,21102,1,18,0,1106,0,259,2101,0,1,221,203,1,21101,0,31,0,1106,0,282,21101,0,38,0,1106,0,259,21001,23,0,2,21202,1,1,3,21102,1,1,1,21102,1,57,0,1106,0,303,2102,1,1,222,20102,1,221,3,21001,221,0,2,21102,1,259,1,21102,80,1,0,1106,0,225,21102,106,1,2,21102,91,1,0,1105,1,303,1201,1,0,223,21001,222,0,4,21101,259,0,3,21102,1,225,2,21101,225,0,1,21101,0,118,0,1106,0,225,20101,0,222,3,21102,42,1,2,21101,133,0,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21101,0,148,0,1106,0,259,1201,1,0,223,21001,221,0,4,20101,0,222,3,21101,10,0,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,195,0,0,106,0,108,20207,1,223,2,20102,1,23,1,21101,-1,0,3,21101,214,0,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1202,-4,1,249,22102,1,-3,1,22101,0,-2,2,21202,-1,1,3,21101,250,0,0,1105,1,225,21202,1,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2105,1,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22102,1,-2,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21202,-2,1,3,21101,343,0,0,1106,0,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22101,0,-4,1,21102,384,1,0,1106,0,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22102,1,1,-4,109,-5,2105,1,0]


def new_runner():
    return IntCodeRunner(
        memory=[instruction for instruction in initial_instructions],
        verbose=False,
        reverse=False
    )


def run_19a():
    i = 0
    for x in range(0, 50):
        for y in range(0, 50):
            runner = new_runner()
            output = runner.run([x, y]).pop()
            if output == 1:
                i += 1
    print(i)
    return


def is_square_fitted(x, y, width=100):
    width_diff = width - 1
    bl_x, bl_y = x, y + width_diff
    is_bottom_left_inside = new_runner().run([bl_x, bl_y]).pop() == 1
    tr_x, tr_y = x + width_diff, y
    is_top_right_inside = new_runner().run([tr_x, tr_y]).pop() == 1
    is_inside = is_bottom_left_inside and is_top_right_inside
    if not is_inside:
        print(f"Square does not fit.")
        return -1

    is_bottom_left_fitted_bottom = new_runner().run([bl_x, bl_y + 1]).pop() == 0
    is_bottom_left_fitted_left = new_runner().run([bl_x - 1, bl_y]).pop() == 0
    is_bottom_left_fitted = is_bottom_left_fitted_bottom and is_bottom_left_fitted_left
    is_top_right_fitted_top = new_runner().run([tr_x, tr_y - 1]).pop() == 0
    is_top_right_fitted_right = new_runner().run([tr_x + 1, tr_y]).pop() == 0
    is_top_right_fitted = is_top_right_fitted_top and is_top_right_fitted_right
    is_fitted = is_bottom_left_fitted and is_top_right_fitted
    if not is_fitted:
        print(f"Square fit is too large.")
        return 1

    print("Perfectly fitted.")
    return 0

def check(a, b):
    return new_runner().run([a, b]).pop()

def run_19b():
    # x = 20000
    # y = 0
    # start_ray = 11682
    # end_ray = 13568
    # while True:
    #     if y % 1000 == 0:
    #         print(f"y = {y}")
    #     runner = IntCodeRunner(
    #         memory=initial_instructions,
    #         verbose=False
    #     )
    #     output = runner.run([x, y]).pop()
    #     if start_ray == 0 and output == 1:
    #         start_ray = y
    #     if start_ray != 0 and end_ray == 0 and output == 0:
    #         end_ray = y
    #         break
    #     y += 1
    # print(start_ray)
    # print(end_ray)
    # tan_alpha = start_ray / x
    # tan_beta = x / end_ray
    # print(tan_alpha)
    # print(tan_beta)

    # alpha_rad = math.atan(tan_alpha)
    # beta_rad = math.atan(tan_beta)
    # gamma_rad = math.pi / 2 - alpha_rad - beta_rad
    #
    # alpha_deg = alpha_rad / math.pi * 180
    # beta_deg = beta_rad / math.pi * 180
    # gamma_deg = 90 - alpha_deg - beta_deg
    # print(f"Alpha = {alpha_rad} ({alpha_rad / math.pi} * π : {alpha_deg}°) ")
    # print(f"Beta = {beta_rad} ({beta_rad / math.pi} * π : {beta_deg}°) ")
    # print(f"Gamma = {gamma_rad} ({gamma_rad / math.pi} * π : {gamma_deg}°) ")

    x = 1030
    start_ray = 1300
    width = 100
    y_top_left = 0
    while True:
        is_found = False
        y = start_ray
        start_ray = end_ray = 0
        while end_ray == 0:
            output = new_runner().run([x, y]).pop()
            if start_ray == 0 and output == 1:
                start_ray = y
            if start_ray != 0 and end_ray == 0 and output == 0:
                end_ray = y - 1
                y_top_left = y - width
                print(f"x = {x}, y = {y_top_left}")
                is_found = is_square_fitted(x, y_top_left, width) >= 0
            y += 1
        if is_found:
            y = y_top_left
            break
        x += 1

    # x = y = 0
    # while not check(x+99, y):
    #     y += 1
    #     if not check(x, y+99):
    #         x += 1
    # print(x*10000 + y)
    #
    # for i in range(x, x+100):
    #     for j in range(y, y+100):
    #         output = new_runner().run([i, j]).pop()
    #         if output != 1:
    #             print(f"ERROR ! ({(i, j)}")

    print("End")



    # tan_alpha_gamma = math.tan(alpha_rad + gamma_rad)
    # print(tan_alpha_gamma)
    # for x in range (100, 10000):
    #     if x%100 == 0:
    #         print(f"x = {x}")
    #     y = tan_alpha*x
    #     possible_height = x * tan_alpha_gamma - y
    #     if possible_height >= 159:
    #         break

    print()
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"Total = {x*10000 + y}")
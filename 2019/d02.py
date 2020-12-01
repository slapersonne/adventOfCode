import math
import re


initial_instructions = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,2,23,10,27,1,27,5,31,1,31,6,35,1,6,35,39,2,39,13,43,1,9,43,47,2,9,47,51,1,51,6,55,2,55,10,59,1,59,5,63,2,10,63,67,2,9,67,71,1,71,5,75,2,10,75,79,1,79,6,83,2,10,83,87,1,5,87,91,2,9,91,95,1,95,5,99,1,99,2,103,1,103,13,0,99,2,14,0,0]


def run_02(instructions):
    for i in range(0, len(instructions), 4):
        operation = instructions[i]
        if operation == 99:
            break
        else:
            input1 = instructions[instructions[i+1]]
            input2 = instructions[instructions[i+2]]
            instructions[instructions[i+3]] = input1 + input2 if operation == 1 else input1 * input2
    return instructions


def run_02a():
    instructions = initial_instructions
    instructions[1] = 12
    instructions[2] = 2
    instructions = run_02(instructions)

    print(f"Position 0 : {[instructions[0]]}")


def run_02b():
    for i in range(0, min(100, len(initial_instructions))):
        for j in range(0, min(100, len(initial_instructions))):
            print(f"i = {i}")
            print(f"j = {j}")
            instructions = [value for value in initial_instructions]
            instructions[1] = i
            instructions[2] = j
            instructions = [value for value in run_02(instructions)]
            print(f"output = {instructions[0]}")
            if instructions[0] == 19690720:
                print(f"100 * {i} + {j} = {100 * i + j}")
                return

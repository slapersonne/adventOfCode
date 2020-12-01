import math
import re


initial_instructions = [3,8,1001,8,10,8,105,1,0,0,21,34,51,64,73,98,179,260,341,422,99999,3,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,1001,9,4,9,1002,9,3,9,1001,9,5,9,4,9,99,3,9,101,5,9,9,102,5,9,9,4,9,99,3,9,101,5,9,9,4,9,99,3,9,1002,9,5,9,1001,9,3,9,102,2,9,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99]
current_amp_status = {}


def extract_instruction(instruction):
    instruction_parts = list(str(instruction))
    operator = int(instruction_parts.pop())
    if len(instruction_parts) > 0:
        second_digit = instruction_parts.pop()
        if operator == 9 and int(second_digit) == 9:
            operator = 99
    first_parameter_mode = int(instruction_parts.pop()) if len(instruction_parts) > 0 else 0
    second_parameter_mode = int(instruction_parts.pop()) if len(instruction_parts) > 0 else 0
    third_parameter_mode = int(instruction_parts.pop()) if len(instruction_parts) > 0 else 0
    return operator, first_parameter_mode, second_parameter_mode, third_parameter_mode


def run_07(instructions, global_inputs=[], i=0):
    global_outputs = []
    while True:
        instruction_input = instructions[i]
        operator, first_parameter_mode, second_parameter_mode, third_parameter_mode = extract_instruction(instruction_input)

        print(f"Operator = {operator} ({instruction_input}), i = {i}")

        if operator == 99:
            print("END OF PROGRAM")
            break

        elif operator == 1 or operator == 2:
            input1 = instructions[instructions[i+1]] if first_parameter_mode == 0 else instructions[i+1]
            input2 = instructions[instructions[i+2]] if second_parameter_mode == 0 else instructions[i+2]
            output_adr = instructions[i+3] if third_parameter_mode == 0 else i+3
            output = input1 + input2 if operator == 1 else input1 * input2
            instructions[output_adr] = output
            i += 4

        elif operator == 3:
            parameter = instructions[i+1] if first_parameter_mode == 0 else i+1
            if len(global_inputs) > 0:
                input = global_inputs.pop()
                instructions[parameter] = input
                i += 2
            else:
                print("Waiting for a new input...")
                break

        elif operator == 4:
            parameter = instructions[i+1] if first_parameter_mode == 0 else i+1
            output = instructions[parameter]
            print(f"Output : {output}")
            global_outputs.append(output)
            i += 2

        elif operator == 5:
            parameter = instructions[instructions[i+1]] if first_parameter_mode == 0 else instructions[i+1]
            if parameter != 0:
                i = instructions[instructions[i+2]] if second_parameter_mode == 0 else instructions[i+2]
            else:
                i += 3

        elif operator == 6:
            parameter = instructions[instructions[i+1]] if first_parameter_mode == 0 else instructions[i+1]
            if parameter == 0:
                i = instructions[instructions[i+2]] if second_parameter_mode == 0 else instructions[i+2]
            else:
                i += 3

        elif operator == 7:
            input1 = instructions[instructions[i+1]] if first_parameter_mode == 0 else instructions[i+1]
            input2 = instructions[instructions[i+2]] if second_parameter_mode == 0 else instructions[i+2]
            output_adr = instructions[i+3] if third_parameter_mode == 0 else i+3
            instructions[output_adr] = 1 if input1 < input2 else 0
            i += 4

        elif operator == 8:
            input1 = instructions[instructions[i+1]] if first_parameter_mode == 0 else instructions[i+1]
            input2 = instructions[instructions[i+2]] if second_parameter_mode == 0 else instructions[i+2]
            output_adr = instructions[i+3] if third_parameter_mode == 0 else i+3
            instructions[output_adr] = 1 if input1 == input2 else 0
            i += 4

        else:
            print(f"ERROR ! Operator = {operator}")
            break

    return operator, instructions, global_outputs, i


def get_all_permutations(inputs):
    all_permutations = []
    get_permutations(all_permutations, inputs, list())
    return all_permutations


def get_permutations(all_permutations, inputs, previous_inputs):
    if len(inputs) <= 1:
        all_permutations.append(previous_inputs + inputs)
        return
    for input in inputs:
        head = input
        tail = [value for value in inputs if value != input]
        get_permutations(all_permutations, tail, previous_inputs + [head])



def run_07a():
    phase_settings = [0,1,2,3,4]
    all_permutations = get_all_permutations(phase_settings)
    print(all_permutations)
    maximum = 0
    best_configuration = None
    for phase_setting in all_permutations:
        input = 0
        for phase in phase_setting:
            print(f"Phase {phase} : Input = {input}")
            instructions = [instruction for instruction in initial_instructions]
            input = run_07(instructions, [input, phase])[0]
            print(f"OUTPUT = {input}")
        if input > maximum:
            maximum = input
            best_configuration = phase_setting
        print(f"Max : {maximum} ({best_configuration})")


def run_07b():
    phase_settings = [5,6,7,8,9]
    all_permutations = get_all_permutations(phase_settings)
    maximum = 0
    best_configuration = None
    for phase_setting in all_permutations:
        input = 0
        current_amp_status = dict()
        while True:
            for index, phase in enumerate(phase_setting):
                print(f"Phase {phase} : Input = {input}")
                previous_outputs = []
                if index not in current_amp_status.keys():
                    instructions = [instruction for instruction in initial_instructions]
                    operator, instructions, global_outputs, i = run_07(instructions, [input, phase])
                else:
                    _1, instructions, previous_outputs, i = current_amp_status[index]
                    operator, instructions, global_outputs, i = run_07(instructions, [input], i)
                current_amp_status[index] = operator, instructions, previous_outputs + global_outputs, i
                input = global_outputs.pop() if len(global_outputs) > 0 else None
                print(f"OUTPUT = {input}")
            if len([status for status, _2, _3, _4 in current_amp_status.values() if status != 99]) == 0:
                break
        print(current_amp_status)
        last_amp_status = current_amp_status[4]
        _1, _2, outputs, _4 = last_amp_status
        output = outputs.pop()
        if output > maximum:
            maximum = output
            best_configuration = phase_setting
        print(f"Max : {maximum} ({best_configuration})")

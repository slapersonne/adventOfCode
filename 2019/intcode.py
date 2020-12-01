import math
import re


class Instruction:

    def __init__(self, instruction_input):
        instruction_parts = list(str(instruction_input))
        self.operator = int(instruction_parts.pop())
        if len(instruction_parts) > 0:
            second_digit = instruction_parts.pop()
            if self.operator == 9 and int(second_digit) == 9:
                self.operator = 99
        self.first_parameter_mode = int(instruction_parts.pop()) if len(instruction_parts) > 0 else 0
        self.second_parameter_mode = int(instruction_parts.pop()) if len(instruction_parts) > 0 else 0
        self.third_parameter_mode = int(instruction_parts.pop()) if len(instruction_parts) > 0 else 0


class IntCodeRunner:

    def __init__(self, **attributes):
        self.memory = {index: value for index, value in enumerate(attributes.get("memory"))}
        self.index = attributes.get("index", 0)
        self.relative_index = attributes.get("relative_index", 0)
        self.input = attributes.get("input", [])
        self.reverse = attributes.get("reverse", False)
        self.output = []
        self.status = -1
        self.verbose = attributes.get("verbose", True)

    def get_parameter(self, parameter_mode, parameter_index, address_mode = False):
        if parameter_mode == 0:
            address = self.memory.get(self.index + parameter_index, 0)
        elif parameter_mode == 1:
            address = self.index + parameter_index
        else:
            address = self.relative_index + self.memory.get(self.index + parameter_index, 0)
        return address if address_mode else self.memory.get(address, 0)

    def run(self, input=None):

        if input is not None:
            self.input = input

        if not self.reverse:
            self.input = list(reversed(self.input))

        while True:
            instruction_input = self.memory.get(self.index, 0)
            instruction = Instruction(instruction_input)
            self.status = instruction.operator

            if instruction.operator == 99:
                if self.verbose:
                    print("END OF PROGRAM")
                break

            elif instruction.operator == 1 or instruction.operator == 2:
                input1 = self.get_parameter(instruction.first_parameter_mode, 1)
                input2 = self.get_parameter(instruction.second_parameter_mode, 2)
                output_adr = self.get_parameter(instruction.third_parameter_mode, 3, address_mode=True)
                output = input1 + input2 if instruction.operator == 1 else input1 * input2
                self.memory[output_adr] = output
                self.index += 4

            elif instruction.operator == 3:
                parameter = self.get_parameter(instruction.first_parameter_mode, 1, address_mode=True)
                if len(self.input) > 0:
                    input = self.input.pop()
                    self.memory[parameter] = input
                    self.index += 2
                else:
                    if self.verbose:
                        print("Waiting for a new input...")
                    break

            elif instruction.operator == 4:
                parameter = self.get_parameter(instruction.first_parameter_mode, 1, address_mode=True)
                output = self.memory[parameter]
                if self.verbose:
                    print(f"Output : {output}")
                self.output.append(output)
                self.index += 2

            elif instruction.operator == 5 or instruction.operator == 6:
                parameter = self.get_parameter(instruction.first_parameter_mode, 1)
                is_zero = (parameter == 0)
                test = is_zero if instruction.operator == 6 else not is_zero
                if test:
                    self.index = self.get_parameter(instruction.second_parameter_mode, 2)
                else:
                    self.index += 3

            elif instruction.operator == 7 or instruction.operator == 8:
                input1 = self.get_parameter(instruction.first_parameter_mode, 1)
                input2 = self.get_parameter(instruction.second_parameter_mode, 2)
                output_adr = self.get_parameter(instruction.third_parameter_mode, 3, address_mode=True)
                test = (input1 < input2) if instruction.operator == 7 else (input1 == input2)
                self.memory[output_adr] = 1 if test else 0
                self.index += 4

            elif instruction.operator == 9:
                input1 = self.get_parameter(instruction.first_parameter_mode, 1)
                self.relative_index += input1
                self.index += 2

            else:
                raise ValueError(f"ERROR ! Operator = {instruction.operator}")

        return self.output

import math
import re

# signal = "12345678"
# signal = "03036732577212944063491565474664"
signal = "59712692690937920492680390886862131901538154314496197364022235676243731306353384700179627460533651346711155314756853419495734284609894966089975988246871687322567664499495407183657735571812115059436153203283165299263503632551949744441033411147947509168375383038493461562836199103303184064429083384309509676574941283043596285161244885454471652448757914444304449337194545948341288172476145567753415508006250059581738670546703862905469451368454757707996318377494042589908611965335468490525108524655606907405249860972187568380476703577532080056382150009356406585677577958020969940093556279280232948278128818920216728406595068868046480073694516140765535007"
pattern = [0, 1, 0, -1]
pattern_length = len(pattern)


def run_16a():
    signal_digits = [int(signal[i]) for i in range(0, len(signal))]
    for phase in range(0, 100):
        result = ""
        for i in range(1, len(signal_digits) + 1):
            digits_with_pattern = [
                (digit, int(math.floor((position + 1) / i)) % pattern_length)
                for position, digit in enumerate(signal_digits)
            ]
            transformed_digits = [
                digit if pattern_value == 1 else -digit
                for digit, pattern_value in digits_with_pattern if pattern_value in [1, 3]
            ]
            total = sum(transformed_digits)
            last_sum_digit = str(total)[-1:]
            result = result + last_sum_digit
        signal_digits = [int(result[i]) for i in range(0, len(result))]
    print("".join([str(d) for d in signal_digits]))


def compute_offsets(phase, input_signal, offsets):
    print(f"Phase = {phase}")
    if phase == 0:
        signal_digits = [int(input_signal[i]) for i in range(0, len(input_signal))]
        return {offset: signal_digits[offset] for offset in offsets}
    else:
        offsets = sorted(offsets)
        previous_phase_offsets_needed = dict()
        # offset_pattern_values = dict()
        for position in range(offsets[0], len(input_signal)):
            previous_phase_offsets_needed[position] = True
        # for position in range(offsets[0], len(input_signal)):
        #     for offset in offsets:
        #         pattern_value = int(math.floor((position + 1) / (offset + 1))) % pattern_length
        #         if pattern_value == 1 or pattern_value == 3:
        #             previous_phase_offsets_needed[position] = True
        #             offset_pattern_values[offset][position] = pattern_value
        # for offset in offsets:
        #     pattern_values = dict()
        #     for position in range(0, len(input_signal)):
        #         pattern_value = int(math.floor((position + 1) / (offset + 1))) % pattern_length
        #         if pattern_value == 1 or pattern_value == 3:
        #             previous_phase_offsets_needed[position] = True
        #             pattern_values[position] = pattern_value
        #     offset_pattern_values[offset] = pattern_values
        previous_phase_values = compute_offsets(phase - 1, input_signal, previous_phase_offsets_needed.keys())
        offset_values = dict()
        print(f"Phase {phase} : {len(offsets)} offsets requested.")
        total = 0
        for position in range(len(input_signal) - 1, offsets[0] - 1, -1):
            total += previous_phase_values[position]
            offset_values[position] = int(str(total)[-1:])
        # for index, offset in enumerate(offsets):
            # print(f"Offset n°{index}")
            # positives, negatives = [], []
            # for position, pattern_value in offset_pattern_values[offset].items():
            #     if pattern_value == 1:
            #         positives.append(previous_phase_values[position])
            #     else:
            #         negatives.append(previous_phase_values[position])
            # total = sum(positives) - sum(negatives)
            # total = sum([previous_phase_values[position] for position in range(offset, len(input_signal))])
            # offset_values[offset] = int(str(total)[-1:])
        return {key: value for key, value in offset_values.items() if key in offsets} if phase == 100 else offset_values


def run_16b():
    # input_signal = signal
    # first_offset = 400
    input_signal = ""
    for i in range(0, 10000):
        input_signal = input_signal + signal
    first_offset = int(signal[0:7])
    print(first_offset)
    needed_offsets = [i for i in range(first_offset, first_offset + 8)]
    values = compute_offsets(100, input_signal, needed_offsets)
    print("".join([str(values[key]) for key in sorted(values)]))
    return

import lib.AoC_lib as AoC
from collections import deque


def moving_window_sum_three(input_list):
    return [(first+second+third) for first, second, third in zip(input_list, input_list[1:], input_list[2:])]

@AoC.timer
def first_part(input_file):
    result = 0

    for prev, curr in zip(input_file, input_file[1:]):
        if curr > prev:
            result += 1

    return result


@AoC.timer
def second_part(input_file):
    result = 0

    moving_list = moving_window_sum_three(input_file)

    for prev, curr in zip(moving_list, moving_list[1:]):
        if curr > prev:
            result += 1

    return result


if __name__ == '__main__':
    DAY = '01'
    USE_TEST_INPUT = False
    # Read the input file.

    if USE_TEST_INPUT:
        with open('inputs/dummy.txt', 'r') as input_file:
            input = [int(i.rstrip('\n')) for i in input_file.readlines()]
    else:
        with open('inputs/input' + DAY + '.txt', 'r') as input_file:
            input = [int(i.rstrip('\n')) for i in input_file.readlines()]

    #print(input)

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part(input)))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part(input)))

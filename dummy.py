import lib.AoC_lib as AoC
from collections import deque
import copy

@AoC.timer
def first_part(input_file):
    result = 0

    return result


@AoC.timer
def second_part(input_file):
    result = 0

    return result


if __name__ == '__main__':
    DAY = 'DUMMY'
    USE_TEST_INPUT = True
    # Read the input file.

    if USE_TEST_INPUT:
        filename = 'inputs/dummy.txt'
    else:
        filename = 'inputs/input' + DAY + '.txt'
    
    with open(filename, 'r') as input_file:
            input = [AoC.split_string_to_int_list(i.rstrip('\n')) for i in input_file.readlines()]

    #print(input)

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part(copy.deepcopy(input))))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part(copy.deepcopy(input))))

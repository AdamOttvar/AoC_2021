import lib.AoC_lib as AoC
from collections import deque

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

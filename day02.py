import lib.AoC_lib as AoC
from collections import deque

@AoC.timer
def first_part(input_file):
    horisontal = 0
    depth = 0

    with open(input_file, 'r') as input:
        for line in input:
            if 'forward' in line.rstrip('\n').split(' ')[0]:
                horisontal += int(line.rstrip('\n').split(' ')[1])
            elif 'down' in line.rstrip('\n').split(' ')[0]:
                depth += int(line.rstrip('\n').split(' ')[1])
            elif 'up' in line.rstrip('\n').split(' ')[0]:
                depth -= int(line.rstrip('\n').split(' ')[1])

    return horisontal*depth


@AoC.timer
def second_part(input_file):
    horisontal = 0
    depth = 0
    aim = 0

    with open(input_file, 'r') as input:
        for line in input:
            if 'forward' in line.rstrip('\n').split(' ')[0]:
                horisontal += int(line.rstrip('\n').split(' ')[1])
                depth += aim*int(line.rstrip('\n').split(' ')[1])
            elif 'down' in line.rstrip('\n').split(' ')[0]:
                aim += int(line.rstrip('\n').split(' ')[1])
            elif 'up' in line.rstrip('\n').split(' ')[0]:
                aim -= int(line.rstrip('\n').split(' ')[1])

    return horisontal*depth


if __name__ == '__main__':
    DAY = '02'

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('inputs/input02.txt')))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part('inputs/input02.txt')))

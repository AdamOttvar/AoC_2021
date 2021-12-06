import lib.AoC_lib as AoC
from collections import deque

@AoC.timer
def first_part(input):
    result = 0
    fish_list = list(input)

    for day in range(1,81):
        for ind, fish in enumerate(fish_list):
            if fish == 0:
                fish_list[ind] = 6
                fish_list.append(9)
            else:
                fish_list[ind] -= 1

    return len(fish_list)


@AoC.timer
def second_part(input):
    nbr_of_days = 256
    result = 0
    fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for fish in input:
        fish_dict[fish] += 1

    for day in range(1,nbr_of_days+1):
        nbr_of_hatchings = fish_dict[0]
        fish_dict[0] = fish_dict[1]
        fish_dict[1] = fish_dict[2]
        fish_dict[2] = fish_dict[3]
        fish_dict[3] = fish_dict[4]
        fish_dict[4] = fish_dict[5]
        fish_dict[5] = fish_dict[6]
        fish_dict[6] = fish_dict[7] + nbr_of_hatchings
        fish_dict[7] = fish_dict[8]
        fish_dict[8] = nbr_of_hatchings

    for days_left in fish_dict:
        result += fish_dict[days_left]

    return result


if __name__ == '__main__':
    DAY = '06'
    USE_TEST_INPUT = False
    # Read the input file.

    if USE_TEST_INPUT:
        with open('inputs/dummy.txt', 'r') as input_file:
            input = [int(i) for i in input_file.readline().rstrip('\n').split(',')]
    else:
        with open('inputs/input' + DAY + '.txt', 'r') as input_file:
            input = [int(i) for i in input_file.readline().rstrip('\n').split(',')]

    #print(input)

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part(input)))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part(input)))

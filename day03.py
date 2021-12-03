import lib.AoC_lib as AoC
from collections import deque

@AoC.timer
def first_part(input_file):
    input_list = list(input_file)

    occurences = [[0]*2 for _ in range(len(input_list[0]))]
    occurences[0][0] = 1
    occurences[0][1] = 1

    for bin_nbr in input_list:
        for position, value in enumerate(bin_nbr):
            if int(value) == 0:
                occurences[position][0] += 1
            else:
                occurences[position][1] += 1

    gamma_rate = [0]*len(input_list[0])
    epsilon_rate = [0]*len(input_list[0])
    for position, value in enumerate(occurences):
        if value[0] > value[1]:
            gamma_rate[position] = 0
            epsilon_rate[position] = 1
        else:
            gamma_rate[position] = 1
            epsilon_rate[position] = 0

    return AoC.binary_list_to_decimal(gamma_rate)*AoC.binary_list_to_decimal(epsilon_rate)


@AoC.timer
def second_part(input_file):
    input_list = list(input_file)
    zero_list = []
    zero_counter = 0
    one_list = []
    one_counter = 0

    while len(input_list) > 1:
        for bin_pos in range(len(input_list[0])):
            for bin_nbr in input_list:
                if int(bin_nbr[bin_pos]) == 0:
                    zero_list.append(bin_nbr)
                    zero_counter += 1
                else:
                    one_list.append(bin_nbr)
                    one_counter += 1
            if zero_counter > one_counter:
                input_list = list(zero_list)
            else:
                input_list = list(one_list)

            zero_list = []
            zero_counter = 0
            one_list = []
            one_counter = 0
    
    oxygen_bin_list = input_list[0]

    input_list = list(input_file)
    while len(input_list) > 1:
        for bin_pos in range(len(input_list[0])):
            for bin_nbr in input_list:
                if int(bin_nbr[bin_pos]) == 0:
                    zero_list.append(bin_nbr)
                    zero_counter += 1
                else:
                    one_list.append(bin_nbr)
                    one_counter += 1
            
            if zero_counter > one_counter:
                input_list = list(one_list)
            else:
                input_list = list(zero_list)

            if len(input_list) < 2:
                break
            
            zero_list = []
            zero_counter = 0
            one_list = []
            one_counter = 0
    
    co2_bin_list = input_list[0]

    return int(oxygen_bin_list,2)*int(co2_bin_list,2)


if __name__ == '__main__':
    DAY = '03'
    USE_TEST_INPUT = False
    # Read the input file.

    if USE_TEST_INPUT:
        with open('inputs/dummy.txt', 'r') as input_file:
            input = [i.rstrip('\n') for i in input_file.readlines()]
    else:
        with open('inputs/input' + DAY + '.txt', 'r') as input_file:
            input = [i.rstrip('\n') for i in input_file.readlines()]

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part(input)))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part(input)))

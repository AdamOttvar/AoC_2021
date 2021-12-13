import lib.AoC_lib as AoC
from collections import deque

@AoC.timer
def first_part(input_file):
    cheapest_possible_fuel = 999999999999

    for pos in range(len(input_file)):
        fuel_cost_list = [abs(crab_pos-pos) for crab_pos in input_file]
        fuel_cost = sum(fuel_cost_list)
        if fuel_cost < cheapest_possible_fuel:
            cheapest_possible_fuel = fuel_cost

    return cheapest_possible_fuel


@AoC.timer
def second_part(input_file):
    cheapest_possible_fuel = 999999999999

    for pos in range(len(input_file)):
        fuel_cost_list = [sum(range(abs(crab_pos-pos)+1)) for crab_pos in input_file]
        fuel_cost = sum(fuel_cost_list)
        if fuel_cost < cheapest_possible_fuel:
            cheapest_possible_fuel = fuel_cost

    return cheapest_possible_fuel


if __name__ == '__main__':
    DAY = '07'
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

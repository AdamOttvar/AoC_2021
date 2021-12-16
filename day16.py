import lib.AoC_lib as AoC
from collections import deque
import copy
import math

VERSION = 0

def convert_hex_to_bin(hex_message):
    bin_message = ''

    hex_lookup = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', 
                  '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                  'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    for char in hex_message:
        bin_message += hex_lookup[char]

    return bin_message

def get_header(input_string):
    version = int(input_string[:3],2)
    type_ID = int(input_string[3:6],2)
    return version, type_ID

def read_literal_value(input_string):
    # Read literal number, return it together with the increased index
    internal_idx = 0
    last_group = False
    number = ''
    while not last_group:
        prefix = int(input_string[internal_idx], 2)
        internal_idx += 1
        number += input_string[internal_idx:internal_idx+4]
        internal_idx += 4
        if prefix == 0:
            last_group = True
    print('type_ID = 4: ' + number + ' -> ' + str(int(number, 2)))


    return internal_idx, int(number,2)

def decode_length_type_id_0(input_string):
    internal_idx = 0
    total_length_in_bits = int(input_string[internal_idx:internal_idx+15], 2)
    internal_idx += 15
    sub_pack = input_string[internal_idx:internal_idx+total_length_in_bits]
    number_list = []
    j = 0
    while j < total_length_in_bits:
        added_idx, number = encode_BITS(sub_pack[j:])
        j += added_idx
        number_list.append(number)

    internal_idx += total_length_in_bits

    return internal_idx, number_list


def decode_length_type_id_1(input_string):
    internal_idx = 0
    number_of_sub_packets = int(input_string[internal_idx:internal_idx+11], 2)
    internal_idx += 11
    j = 0
    number_list = []
    while j < number_of_sub_packets:
        added_idx, number = encode_BITS(input_string[internal_idx:])
        j += 1
        internal_idx += added_idx
        number_list.append(number)
    
    return internal_idx, number_list

def operand_operation(operand, list_of_numbers):
    result = -1

    if operand == 0:
        result = sum(list_of_numbers)
    elif operand == 1:
        result = math.prod(list_of_numbers)
    elif operand == 2:
        result = min(list_of_numbers)
    elif operand == 3:
        result = max(list_of_numbers)
    elif operand == 5:
        result = int(list_of_numbers[0] > list_of_numbers[1])
    elif operand == 6:
        result = int(list_of_numbers[0] < list_of_numbers[1])
    elif operand == 7:
        result = int(list_of_numbers[0] == list_of_numbers[1])

    print('List: ' + str(list_of_numbers) + 'Operand: ' + str(operand) + ' Result: ' + str(result))
    return result


def encode_BITS(input_string):
    global VERSION
    result = -1
    internal_idx = 0
    version, type_ID = get_header(input_string[internal_idx:internal_idx+6])
    VERSION += version
    #print('Version: ' + str(version))
    internal_idx = 6
    if type_ID == 4:
        added_idx, result = read_literal_value(input_string[internal_idx:])
        internal_idx += added_idx
    else:
        length_type_id = int(input_string[internal_idx], 2)
        #print('Length type ID: ' + str(length_type_id))
        internal_idx += 1
        if length_type_id == 0:
            added_idx, number_list = decode_length_type_id_0(
                input_string[internal_idx:])
            operand_result = operand_operation(type_ID, number_list)
            if operand_operation != -1:
                result = operand_result
            else:
                print('Something wrong with result')
            internal_idx += added_idx
        elif length_type_id == 1:
            added_idx, number_list = decode_length_type_id_1(
                input_string[internal_idx:])
            operand_result = operand_operation(type_ID, number_list)
            if operand_operation != -1:
                result = operand_result
            else:
                print('Something wrong with result')
            internal_idx += added_idx
        else:
            print('Wrong length type id!')
    
    return internal_idx, result


@AoC.timer
def first_part(input_file):
    global VERSION
    result = 0

    i, result = encode_BITS(input_file)

    return VERSION


@AoC.timer
def second_part(input_file):
    result = 0

    i, result = encode_BITS(input_file)

    return result


if __name__ == '__main__':
    DAY = '16'
    USE_TEST_INPUT = False
    # Read the input file.

    if USE_TEST_INPUT:
        filename = 'inputs/dummy.txt'
    else:
        filename = 'inputs/input' + DAY + '.txt'
    
    with open(filename, 'r') as input_file:
            input = [i.rstrip('\n') for i in input_file.readlines()]

    int_input = convert_hex_to_bin(input[0])
    #print(int_input)

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part(int_input)))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part(int_input)))

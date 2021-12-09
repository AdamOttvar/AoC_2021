import lib.AoC_lib as AoC
from collections import deque, defaultdict

def get_output_digits(input):
    output_string = input.split('|')[1]
    return output_string.strip(' ').split(' ')

def get_unique_signal_patterns(input):
    output_string = input.split('|')[0]
    return output_string.strip(' ').split(' ')

def get_dict_of_digit_mapping(line):

    dict_of_length = defaultdict(list)
    map_to_digit = defaultdict(int)
    map_to_sections = defaultdict(str)
    unique_lengths = {2: 1, 3: 7, 4: 4, 7: 8}

    for digit in get_unique_signal_patterns(line):
        dict_of_length[len(digit)].append(digit)
        # Map the unique lengths
        # 1, 7, 4 and 8
        if len(digit) in unique_lengths.keys():
            map_to_digit[''.join(sorted(digit))] = unique_lengths[len(digit)]
            map_to_sections[unique_lengths[len(digit)]] = digit
    # Map 9, 0 and 6
    for digit in dict_of_length[6]:
        four_in_nine = set(sorted(map_to_sections[4])).issubset(set(sorted(digit)))
        one_in_digit = set(sorted(map_to_sections[1])).issubset(set(sorted(digit)))
        if four_in_nine:
            map_to_digit[''.join(sorted(digit))] = 9
            map_to_sections[9] = digit
        elif one_in_digit and not four_in_nine:
            map_to_digit[''.join(sorted(digit))] = 0
            map_to_sections[0] = digit
        else:
            map_to_digit[''.join(sorted(digit))] = 6
            map_to_sections[6] = digit
    
    # Map 3, 5 and 2
    print(dict_of_length)
    for digit in dict_of_length[5]:
        one_in_three = set(sorted(map_to_sections[1])).issubset(set(sorted(digit)))
        five_in_six = set(sorted(digit)).issubset(set(sorted(map_to_sections[6])))
        if one_in_three:
            map_to_digit[''.join(sorted(digit))] = 3
            map_to_sections[3] = digit
        elif five_in_six:
            map_to_digit[''.join(sorted(digit))] = 5
            map_to_sections[5] = digit
        else:
            map_to_digit[''.join(sorted(digit))] = 2
            map_to_sections[2] = digit


    #print(dict_of_length)
    #print(map_to_digit)
    #print(map_to_sections)
    return map_to_digit

@AoC.timer
def first_part(input_file):
    result = 0
    unique_length = [2, 3, 4, 7]

    for line in input_file:
        for digit in get_output_digits(line):
            if len(digit) in unique_length:
                result += 1

    return result


@AoC.timer
def second_part(input_file):
    result = 0

    for line in input_file:
        segment_mapping = get_dict_of_digit_mapping(line)
        output_digits = get_output_digits(line)
        print('main')
        print(segment_mapping)

        output_list = []
        for digit in output_digits:
            output_list.append(str(segment_mapping[''.join(sorted(digit))]))
        
        result += int(''.join(output_list))

        
    return result


if __name__ == '__main__':
    DAY = '08'
    USE_TEST_INPUT = False
    # Read the input file.

    if USE_TEST_INPUT:
        with open('inputs/dummy.txt', 'r') as input_file:
            input = [i.rstrip('\n') for i in input_file.readlines()]
    else:
        with open('inputs/input' + DAY + '.txt', 'r') as input_file:
            input = [i.rstrip('\n') for i in input_file.readlines()]

    #print(input)

    #print('First solution for day' + DAY + ': ')
    #print('Result: ' + str(first_part(input)))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part(input)))

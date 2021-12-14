import lib.AoC_lib as AoC
from collections import deque, defaultdict, Counter
import copy

def read_optimal_polymer_formula(filename):
    template = None
    insert_rules = defaultdict(str)
    with open(filename, 'r') as input_file:
        for line in input_file:
            if not template:
                template = line.rstrip('\n')
            elif line == '\n':
                continue
            else:
                input, output = line.rstrip('\n').split(' -> ')
                insert_rules[input] = output

    return template, insert_rules

@AoC.timer
def first_part(template, insert_rules):
    for _ in range(10):
        polymer_string = ''
        for char_idx in range(len(template)-1):
            output = insert_rules[template[char_idx:char_idx+2]]
            if output:
                polymer_string += template[char_idx] + output
        
        polymer_string += template[-1]
        template = polymer_string

        count = Counter(template)

    return count.most_common(1)[0][1] - count.most_common()[:-2:-1][0][1]


@AoC.timer
def second_part(template, insert_rules):
    polymer_pair_counter = defaultdict(int,{ k:0 for k in insert_rules })
    single_polymer_counter = defaultdict(int)
    for char in template:
        single_polymer_counter[char] += 1

    for char_idx in range(len(template)-1):
        input = template[char_idx:char_idx+2]
        output = insert_rules[input]
        if output:
            polymer_pair_counter[input] += 1

    for _ in range(40):
        poly_count_temp = copy.deepcopy(polymer_pair_counter)
        for polymer_pair in polymer_pair_counter:
            if polymer_pair_counter[polymer_pair] > 0:
                curr_amount = polymer_pair_counter[polymer_pair]
                output = insert_rules[polymer_pair]
                first = polymer_pair[0] + output
                second = output + polymer_pair[1]
                poly_count_temp[first] += curr_amount
                poly_count_temp[second] += curr_amount
                poly_count_temp[polymer_pair] -= curr_amount
                single_polymer_counter[output] += curr_amount
        
        polymer_pair_counter = copy.deepcopy(poly_count_temp)

    count = Counter(single_polymer_counter)

    return count.most_common(1)[0][1] - count.most_common()[:-2:-1][0][1]


if __name__ == '__main__':
    DAY = '14'
    USE_TEST_INPUT = False
    # Read the input file.

    if USE_TEST_INPUT:
        filename = 'inputs/dummy.txt'
    else:
        filename = 'inputs/input' + DAY + '.txt'

    template, insert_rules = read_optimal_polymer_formula(filename)

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part(template, insert_rules)))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part(template, insert_rules)))

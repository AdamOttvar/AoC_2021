import lib.AoC_lib as AoC
from collections import deque

@AoC.timer
def first_part(input_file):
    result = 0
    closings_to_openings = {'(': ')', '[': ']', '{': '}', '<': '>'}
    illegal_characters = []
    point_table = {')': 3, ']': 57, '}': 1197, '>': 25137}

    for row in input_file:
        openings = deque()
        for char in row:
            if char in closings_to_openings:
                openings.append(char)
            elif closings_to_openings[openings[-1]] == char:
                openings.pop()
            else:
                illegal_characters.append(char)
                result += point_table[char]
                break
    return result


@AoC.timer
def second_part(input_file):
    result = 0
    closings_to_openings = {'(': ')', '[': ']', '{': '}', '<': '>'}
    illegal_characters = []
    point_table = {')': 1, ']': 2, '}': 3, '>': 4}
    incomplete_rows = []
    scores = []

    for row in input_file:
        result = 0
        openings = deque()
        incomplete_row = True
        for char in row:
            if char in closings_to_openings:
                openings.append(char)
            elif closings_to_openings[openings[-1]] == char:
                openings.pop()
            else:
                illegal_characters.append(char)
                incomplete_row = False
                break
        
        if incomplete_row:
            incomplete_rows.append(openings)
            while len(openings) > 0:
                result = result*5 + point_table[closings_to_openings[openings.pop()]]
            scores.append(result)

    return sorted(scores)[int(len(scores)/2)]


if __name__ == '__main__':
    DAY = '10'
    USE_TEST_INPUT = False
    # Read the input file.

    if USE_TEST_INPUT:
        with open('inputs/dummy.txt', 'r') as input_file:
            input = [i.rstrip('\n') for i in input_file.readlines()]
    else:
        with open('inputs/input' + DAY + '.txt', 'r') as input_file:
            input = [i.rstrip('\n') for i in input_file.readlines()]

    #print(input)

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part(input)))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part(input)))

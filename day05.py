import lib.AoC_lib as AoC
from collections import Counter
import itertools

def return_lines_from_input(input):
    list_of_line = []

    with open(input, 'r') as input_file:
        for line in input_file:
            list_of_line.append([tuple(map(int,point.split(','))) for point in line.strip('\n').split('->')])
    
    return list_of_line

def check_if_hor_or_vert(line):
    return line[0][0] == line[1][0] or line[0][1] == line[1][1]

def return_all_positions_for_line(points):
    positions = []

    # If only x-position changes
    if abs(points[0][0] - points[1][0]) and not abs(points[0][1] - points[1][1]):
        # If first point larger than second (flip range needed)
        if points[0][0] > points[1][0]:
            positions = [(x,points[0][1]) for x in range(points[1][0], points[0][0]+1)]
        else:
            positions = [(x,points[0][1]) for x in range(points[0][0], points[1][0]+1)]
    # If only y-position changes
    elif abs(points[0][1] - points[1][1]) and not abs(points[0][0] - points[1][0]):
        # If first point larger than second (flip range needed)
        if points[0][1] > points[1][1]:
            positions = [(points[0][0],y) for y in range(points[1][1], points[0][1]+1)]
        else:
            positions = [(points[0][0],y) for y in range(points[0][1], points[1][1]+1)]
    # If both changes
    else:
        if points[1][0] - points[0][0] < 0:
            x_pos = list(range(points[0][0], points[1][0]-1, -1))
        else:
            x_pos = list(range(points[0][0], points[1][0]+1))

        if points[1][1] - points[0][1] < 0:
            y_pos = list(range(points[0][1], points[1][1]-1, -1))
        else:
            y_pos = list(range(points[0][1], points[1][1]+1))

        positions = [(x,y) for x,y in zip(x_pos, y_pos)]

    return positions

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

@AoC.timer
def first_part(list_of_lines):
    all_positions = []
    hor_and_vert_lines = []
    for line in list_of_lines:
        if check_if_hor_or_vert(line):
            hor_and_vert_lines.append(line)
    
    for line in hor_and_vert_lines:
        all_positions.extend(return_all_positions_for_line(line))
    
    intersected_positions = Counter({k: c for k, c in Counter(all_positions).items() if c >= 2})

    return len(intersected_positions)


@AoC.timer
def second_part(list_of_lines):
    all_positions = []
    hor_and_vert_lines = []
    for line in list_of_lines:
        if check_if_hor_or_vert(line):
            hor_and_vert_lines.append(line)
    
    for line in list_of_lines:
        all_positions.extend(return_all_positions_for_line(line))
    
    intersected_positions = Counter({k: c for k, c in Counter(all_positions).items() if c >= 2})

    return len(intersected_positions)


if __name__ == '__main__':
    DAY = '05'
    USE_TEST_INPUT = False
    # Read the input file.

    if USE_TEST_INPUT:
        input = 'inputs/dummy.txt'
    else:
        input = 'inputs/input' + DAY + '.txt'

    lines = return_lines_from_input(input)
    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part(lines)))

    lines = return_lines_from_input(input)
    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part(lines)))

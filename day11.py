import lib.AoC_lib as AoC
from collections import deque
import copy

def flash_octopus(map, x, y, octos_above_nine, already_flashed):
    # Direction vectors
    dCol = [ 0, 1, 0, -1, -1, 1, -1, 1]
    dRow = [ -1, 0, 1, 0, -1, -1, 1, 1]

    if (x, y) in already_flashed:
        return
    else:
        already_flashed.add((x, y))

    # Go to the adjacent cells
    for i in range(len(dRow)):
        adjx = x + dRow[i]
        adjy = y + dCol[i]
        if (AoC.is_inside_map(map, adjx, adjy)):
            map[adjy][adjx] += 1
            if (map[adjy][adjx] > 9) and not ((adjx, adjy) in already_flashed):
                octos_above_nine.append((adjx,adjy))
    

@AoC.timer
def first_part(input_file):
    result = 0
    interations = 100

    for iteration in range(interations):
        octos_to_start = deque()
        flashed_this_iteration = set()
        for y, row in enumerate(input_file):
            for x, col in enumerate(row):
                input_file[y][x] += 1
                if input_file[y][x] > 9:
                    octos_to_start.append((x,y))

        # Go through "starting" octos, found on addition of all octos
        while len(octos_to_start) > 0:
            start_octo = octos_to_start.popleft()
            if (start_octo[0], start_octo[1]) in flashed_this_iteration:
                continue
            octos_to_flash = deque()
            octos_to_flash.append(start_octo)

            while len(octos_to_flash) > 0:
                octo = octos_to_flash.pop()
                flash_octopus(input_file, octo[0], octo[1], octos_to_flash, flashed_this_iteration)
            
        for octo in flashed_this_iteration:
            input_file[octo[1]][octo[0]] = 0


        result += len(flashed_this_iteration)

    return result


@AoC.timer
def second_part(input_file):
    result = 0
    interations = 900

    for iteration in range(interations):
        octos_to_start = deque()
        flashed_this_iteration = set()
        for y, row in enumerate(input_file):
            for x, col in enumerate(row):
                input_file[y][x] += 1
                if input_file[y][x] > 9:
                    octos_to_start.append((x,y))

        # Go through "starting" octos, found on addition of all octos
        while len(octos_to_start) > 0:
            start_octo = octos_to_start.popleft()
            if (start_octo[0], start_octo[1]) in flashed_this_iteration:
                continue
            octos_to_flash = deque()
            octos_to_flash.append(start_octo)

            while len(octos_to_flash) > 0:
                octo = octos_to_flash.pop()
                flash_octopus(input_file, octo[0], octo[1], octos_to_flash, flashed_this_iteration)
            
        for octo in flashed_this_iteration:
            input_file[octo[1]][octo[0]] = 0


        if len(flashed_this_iteration) == len(input_file)*len(input_file[0]):
            #print('==== Step ' + str(iteration+1) + ' ====')
            #print('Flashed: ' + str(len(flashed_this_iteration)))
            #AoC.print_2D_int_map(input_file)
            return iteration+1

    return result



if __name__ == '__main__':
    DAY = '11'
    USE_TEST_INPUT = False
    # Read the input file.

    if USE_TEST_INPUT:
        filename = 'inputs/dummy.txt'
    else:
        filename = 'inputs/input' + DAY + '.txt'
    
    with open(filename, 'r') as input_file:
            input = [AoC.split_string_to_int_list(i.rstrip('\n')) for i in input_file.readlines()]

    #AoC.print_2D_int_map(input)

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part(copy.deepcopy(input))))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part(copy.deepcopy(input))))


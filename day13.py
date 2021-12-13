import lib.AoC_lib as AoC
from collections import deque
import copy

def read_transparent_paper_input(filename):
    dots = set()
    folds = []
    with open(filename, 'r') as input_file:
        for line in input_file:
            if line == '\n':
                continue
            elif 'fold' in line:
                orientation, position = line.rstrip('\n').split()[2].split('=')
                folds.append((orientation, int(position)))
            else:
                x, y = line.rstrip('\n').split(',')
                dots.add((int(x),int(y)))

    return dots, folds

@AoC.timer
def first_part(dots, folds):
    for fold in folds:
        folded_dots = set(dots)
        if fold[0] == 'y':
            for dot in dots:
                if dot[1] > fold[1]:
                    folded_dots.remove(dot)
                    folded_dots.add((dot[0],fold[1]*2 - dot[1]))

        elif fold[0] == 'x':
            for dot in dots:
                if dot[0] > fold[1]:
                    folded_dots.remove(dot)
                    folded_dots.add((fold[1]*2 - dot[0],dot[1]))
        else:
            print('Wrong fold!')
        
        dots = set(folded_dots)
        break

    #AoC.print_2D_dot_map(dots)
    return len(dots)


@AoC.timer
def second_part(dots, folds):
    for fold in folds:
        folded_dots = set(dots)
        if fold[0] == 'y':
            for dot in dots:
                if dot[1] > fold[1]:
                    folded_dots.remove(dot)
                    folded_dots.add((dot[0],fold[1]*2 - dot[1]))

        elif fold[0] == 'x':
            for dot in dots:
                if dot[0] > fold[1]:
                    folded_dots.remove(dot)
                    folded_dots.add((fold[1]*2 - dot[0],dot[1]))
        else:
            print('Wrong fold!')
        
        dots = set(folded_dots)

    AoC.print_2D_dot_map(dots)
    return len(dots)


if __name__ == '__main__':
    DAY = '13'
    USE_TEST_INPUT = False
    # Read the input file.

    if USE_TEST_INPUT:
        filename = 'inputs/dummy.txt'
    else:
        filename = 'inputs/input' + DAY + '.txt'
    
    dots, folds = read_transparent_paper_input(filename)

    #print(input)

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part(copy.deepcopy(dots), copy.deepcopy(folds))))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part(copy.deepcopy(dots), copy.deepcopy(folds))))

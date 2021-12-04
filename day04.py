import lib.AoC_lib as AoC
from collections import deque
from itertools import repeat

def read_bingo_input(input):
    draw_numbers = None
    board_number = -1
    boards = []
    with open(input, 'r') as input_file:
        for line in input_file:
            if not draw_numbers:
                draw_numbers = [int(i) for i in line.rstrip('\n').split(',')]
            else:
                if len(line.rstrip('\n')) > 1:
                    boards[board_number].append([int(i) for i in line.rstrip('\n').split()])
                else:
                    board_number += 1
                    boards.append([])
        boards = boards[:-1]
    
    return draw_numbers, boards


@AoC.timer
def first_part(numbers, boards):
    boards = list(boards)
    result = 0
    # Keep track of number of Xs in rows and cols for all boards
    board_scores = [[[0,0,0,0,0],[0,0,0,0,0]] for x in repeat(None, len(boards))]
    for number in numbers:
        for board_idx,board in enumerate(boards):
            for row_idx, row in enumerate(board):
                for col_idx, col in enumerate(row):
                    if col == number:
                        boards[board_idx][row_idx][col_idx] = 'X'
                        board_scores[board_idx][0][row_idx] += 1
                        board_scores[board_idx][1][col_idx] += 1
                    
                    # Check if 5 Xs in any row or col
                    if (5 in board_scores[board_idx][0]) or 5 in board_scores[board_idx][1]:
                        for row_score in board:
                            for col_score in row_score:
                                if col_score != 'X':
                                    result += col_score
                        return result*number                   

    return result


@AoC.timer
def second_part(numbers, boards):
    boards = list(boards)
    result = 0
    finished_boards = set([])
    # Keep track of number of Xs in rows and cols for all boards
    board_scores = [[[0,0,0,0,0],[0,0,0,0,0]] for x in repeat(None, len(boards))]
    for number in numbers:
        for board_idx,board in enumerate(boards):
            for row_idx, row in enumerate(board):
                for col_idx, col in enumerate(row):
                    if col == number:
                        boards[board_idx][row_idx][col_idx] = 'X'
                        board_scores[board_idx][0][row_idx] += 1
                        board_scores[board_idx][1][col_idx] += 1
                    
                    # Check if 5 Xs in any row or col
                    if (5 in board_scores[board_idx][0]) or 5 in board_scores[board_idx][1]:
                        if len(finished_boards) == len(boards)-1 and board_idx not in finished_boards:
                            for row_score in board:
                                for col_score in row_score:
                                    if col_score != 'X':
                                        result += col_score
                            return result*number
                        else:
                            finished_boards.add(board_idx)              

    return result


if __name__ == '__main__':
    DAY = '04'
    USE_TEST_INPUT = False
    # Read the input file.

    if USE_TEST_INPUT:
        input = 'inputs/dummy.txt'
    else:
        input = 'inputs/input' + DAY + '.txt'

    draw_numbers, boards = read_bingo_input(input)
    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part(draw_numbers, boards)))

    draw_numbers, boards = read_bingo_input(input)
    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part(draw_numbers, boards)))

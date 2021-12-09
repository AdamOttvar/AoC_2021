import lib.AoC_lib as AoC
from collections import deque
from heapq import nlargest

def get_adj_nbrs(map, x, y):
    adj_nbrs = set()
    if 0 <= y-1 <= len(map)-1:
        adj_nbrs.add(int(map[y-1][x]))
    if 0 <= y+1 <= len(map)-1:
        adj_nbrs.add(int(map[y+1][x]))
    if 0 <= x-1 <= len(map[0])-1:
        adj_nbrs.add(int(map[y][x-1]))
    if 0 <= x+1 <= len(map[0])-1:
        adj_nbrs.add(int(map[y][x+1]))

    return adj_nbrs

def get_lowest_points(input_file):
    lowest_points = []
    for y, row in enumerate(input_file):
        for x, col in enumerate(row):
            adjacent_nbrs = get_adj_nbrs(input_file,x,y)
            if int(col) < min(adjacent_nbrs):
                lowest_points.append([x,y])
    
    return lowest_points


def is_valid_position(map, visited, pos):
    x = pos[0]
    y = pos[1]

    valid = True
    if not (0 <= y <= len(map)-1 and 0 <= x <= len(map[0])-1):
        valid = False
    
    if valid and visited[y][x]:
        valid = False

    if valid and int(map[y][x]) >= 9:
        valid = False

    return valid


@AoC.timer
def first_part(input_file):
    result = 0

    for y, row in enumerate(input_file):
        for x, col in enumerate(row):
            adjacent_nbrs = get_adj_nbrs(input_file,x,y)
            if int(col) < min(adjacent_nbrs):
                result += int(col)+1

    return result


@AoC.timer
def second_part(input_file):
    result = 1
    visited_map = [ [0]*len(input_file[0]) for _ in range(len(input_file))]

    # Direction vectors
    dRow = [ -1, 0, 1, 0]
    dCol = [ 0, 1, 0, -1]

    lowest_points = get_lowest_points(input_file)
    basin_sizes = [0]*len(lowest_points)
    
    for point_idx, start in enumerate(lowest_points):
        queue = deque()
        queue.append(start)
        visited_map[start[1]][start[0]] = 1
        basin_sizes[point_idx] += 1

        while len(queue) > 0:
            cell = queue.popleft()
            x = cell[0]
            y = cell[1]
    
            # Go to the adjacent cells
            for i in range(4):
                adjx = x + dRow[i]
                adjy = y + dCol[i]
                if (is_valid_position(input_file, visited_map, [adjx, adjy])):
                    queue.append([adjx, adjy])
                    visited_map[adjy][adjx] = 1
                    basin_sizes[point_idx] +=1
    

    result = 1
    for x in nlargest(3, basin_sizes):
         result = result * x

    return result


if __name__ == '__main__':
    DAY = '09'
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

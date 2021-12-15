import lib.AoC_lib as AoC
from collections import defaultdict, deque
import copy
import itertools
from queue import PriorityQueue


def get_adj_nodes(map: list[list[int]], x: int, y: int, diagonals: bool=False) -> set[tuple]:
    # Direction vectors
    if diagonals:
        dCol = [0, 1, 0, -1, -1, 1, -1, 1]
        dRow = [-1, 0, 1, 0, -1, -1, 1, 1]
    else:
        dRow = [-1, 0, 1, 0]
        dCol = [0, 1, 0, -1]

    neighbours = set()

    for i in range(4):
        adjx = x + dRow[i]
        adjy = y + dCol[i]
        if (AoC.is_inside_map(map, adjx, adjy)):
            neighbours.add((adjx, adjy))
    
    return neighbours

def dijkstra_2D_map(map, start, goal):
    queue = PriorityQueue()
    visited = set()

    all_positions = list(itertools.product(
        *[range(len(map[0])), range(len(map))]))

    node_costs = defaultdict(
        int, {(x, y): 99999999999999 for x, y in all_positions})

    queue.put((0,start))
    node_costs[start] = 0

    while not queue.empty():
        node = queue.get()[1]
        visited.add(node)

        neighbours = get_adj_nodes(map, node[0], node[1])
        for neighbour in neighbours:
            distance = map[neighbour[1]][neighbour[0]]
            if neighbour not in visited:
                current_cost = node_costs[neighbour]
                new_cost = node_costs[node] + distance

                if new_cost < current_cost:
                    queue.put((new_cost,neighbour))
                    node_costs[neighbour] = new_cost

    return node_costs


@AoC.timer
def first_part(map):
    start = (0, 0)
    goal = (len(map[0])-1, len(map)-1)
    node_costs = dijkstra_2D_map(map, start, goal)
    return node_costs[goal]


@AoC.timer
def second_part(map):
    larger_map = [[] for _ in range(len(map)*5)]

    for y,row in enumerate(map):
        for i1 in range(5):
            for i2 in range(i1,i1+5):
                larger_map[y+len(map)*i1].extend([x+i2 if x+i2 <=
                                                  9 else (x+i2) % 9 for x in map[y]])
    
    start = (0, 0)
    goal = (len(larger_map[0])-1, len(larger_map)-1)
    node_costs = dijkstra_2D_map(larger_map, start, goal)
    return node_costs[goal]


if __name__ == '__main__':
    DAY = '15'
    USE_TEST_INPUT = False
    # Read the input file.

    if USE_TEST_INPUT:
        filename = 'inputs/dummy.txt'
    else:
        filename = 'inputs/input' + DAY + '.txt'
    
    with open(filename, 'r') as input_file:
            input = [AoC.split_string_to_int_list(i.rstrip('\n')) for i in input_file.readlines()]

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part(copy.deepcopy(input))))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part(copy.deepcopy(input))))

import lib.AoC_lib as AoC
from collections import deque, defaultdict
import copy

counter = 0

def create_graph(input_list):
    graph = defaultdict(list)
    for line in input_list:
        start, end = line.split('-')
        graph[start].append(end)
        if start != 'start': graph[end].append(start)
    
    return graph

def traverse_graph(graph, start, end, visited, path_list, allow_twice=False):
    global counter

    if start.islower():
        visited[start] += 1
    path_list.append(start)

    if start == end:
        #print(','.join(path_list))
        counter += 1
    else:
        for i in graph[start]:
            if visited[i] < 1:
                traverse_graph(graph,i,end,visited,path_list,allow_twice)
            elif visited[i] == 1 and allow_twice and i != 'start':
                allow_twice = False
                traverse_graph(graph,i,end,visited,path_list,allow_twice)
                allow_twice = True

    path_list.pop()
    visited[start] -= 1


@AoC.timer
def first_part(input_file):
    global counter

    graph = create_graph(input_file)
    visited = defaultdict(int)
    path = []

    traverse_graph(graph, 'start', 'end', visited, path)

    return counter


@AoC.timer
def second_part(input_file):
    global counter

    graph = create_graph(input_file)
    visited = defaultdict(int)
    path = []

    traverse_graph(graph, 'start', 'end', visited, path, allow_twice=True)

    return counter


if __name__ == '__main__':
    DAY = '12'
    USE_TEST_INPUT = False
    # Read the input file.

    if USE_TEST_INPUT:
        filename = 'inputs/dummy.txt'
    else:
        filename = 'inputs/input' + DAY + '.txt'
    
    with open(filename, 'r') as input_file:
            input = [i.rstrip('\n') for i in input_file.readlines()]

    #print(input)

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part(copy.deepcopy(input))))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part(copy.deepcopy(input))))

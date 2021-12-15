import functools
import time
import typing

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return value
    return wrapper_timer

def split_string_to_int_list(string_to_split, delimiter=' '):
    return [int(x) for x in string_to_split]

def binary_list_to_decimal(binary_list):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary_list)))

def is_inside_map(map: list[list[int]], x: int, y: int) -> bool:
    inside = True
    if not (0 <= y <= len(map)-1 and 0 <= x <= len(map[0])-1):
        inside = False

    return inside

def print_2D_int_map(map):
    for row in map:
        print(''.join(str(i) for i in row))

def print_2D_dot_map(dots):
    max_x = max(dots, key=lambda x: x[0])[0]
    max_y = max(dots, key=lambda x: x[1])[1]
    dot_map = [['.']*(max_x+1) for _ in range(max_y+1)]
    for dot in dots:
        dot_map[dot[1]][dot[0]] = '#'
    
    for row in dot_map:
        print(''.join(row))

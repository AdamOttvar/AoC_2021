import lib.AoC_lib as AoC
from itertools import product

def check_velocity_reaches_target(target, velocity):
    x_min, x_max = target[0]
    y_min, y_max = target[1]
    x_pos, y_pos = (0, 0)
    x_vel, y_vel = velocity

    while x_pos <= x_max and y_pos >= y_min:
        x_pos = x_pos + x_vel
        y_pos = y_pos + y_vel

        if x_min <= x_pos <= x_max and y_min <= y_pos <= y_max:
            return True

        x_vel_sign = -1 if x_vel < 0 else 1 if x_vel > 0 else 0
        x_vel = x_vel - x_vel_sign
        y_vel = y_vel - 1

    return False


@AoC.timer
def first_part(target):
    y_vel_max = -99999
    for x_vel, y_vel in product(range(100), range(-300,300)):
        if check_velocity_reaches_target(target, (x_vel, y_vel)):
            y_vel_max = y_vel if y_vel > y_vel_max else y_vel_max

    return (y_vel_max+1) * y_vel_max // 2


@AoC.timer
def second_part(target):
    y_vel_list = list()
    for x_vel, y_vel in product(range(100), range(-300, 300)):
        if check_velocity_reaches_target(target, (x_vel, y_vel)):
            y_vel_list.append(y_vel)

    return len(y_vel_list)


if __name__ == '__main__':
    DAY = '17'
    USE_TEST_INPUT = False
    # Read the input file.

    if USE_TEST_INPUT:
        x_interval = (20, 30)
        y_interval = (-10, -5)
        target = (x_interval, y_interval)
    else:
        # target area: x=25..67, y=-260..-200
        x_interval = (25, 67)
        y_interval = (-260, -200)
        target = (x_interval, y_interval)

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part(target)))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part(target)))

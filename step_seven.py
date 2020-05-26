from solve import find_cubie
from step_six import is_fish, is_H, find_unsolved_edges


def solve_down_edges(cube, result_steps):
    lst = find_unsolved_edges(cube)
    if len(lst) == 0:
        return
    if is_H(cube, lst):
        H_method(cube, lst, result_steps)
    elif is_fish(cube, lst):
        fish_method(cube, lst, result_steps)


def fish_method(cube, lst, result_steps):
    pos1 = find_cubie(cube, lst[0])
    pos2 = find_cubie(cube, lst[1])
    sum_el = cube.ideal_cube[pos1[0]].face[pos1[1]][pos1[2]] + cube.ideal_cube[pos2[0]].face[pos2[1]][pos2[2]]
    fish_method_steps = {92 : ["b", "l", "r", "d", "U", "f", "f", "d", "U", "d", "U", "b", "d", "d", "B", "D", "u", "D", "u", "f", "f", "D", "u", "R", "d", "d", "L", "B"], # 47+45
                        87: ["r", "b", "f", "d", "U", "l", "l", "d", "U", "d", "U", "r", "d", "d", "R", "D", "u", "D", "u", "l", "l", "D", "u", "F", "d", "d", "B", "R"], # 42+45
                        86: ["f", "r", "l", "d", "U", "b", "b", "d", "U", "d", "U", "f", "d", "d", "F", "D", "u", "D", "u", "b", "b", "D", "u", "L", "d", "d", "R", "F"], # 42+44
                        91: ["l", "f", "b", "d", "U", "r", "r", "d", "U", "d", "U", "l", "d", "d", "L", "D", "u", "D", "u", "r", "r", "D", "u", "B", "d", "d", "F", "L"]} # 44+47
    steps = fish_method_steps[sum_el]
    for move in steps:
        cube.rotate(move)
        result_steps.append(move)


def H_method(cube, lst, result_steps):
    pos1 = find_cubie(cube, lst[0])
    pos2 = find_cubie(cube, lst[1])
    maxel = max(cube.ideal_cube[pos1[0]].face[pos1[1]][pos1[2]], cube.ideal_cube[pos2[0]].face[pos2[1]][pos2[2]])
    fish_method_steps = {45 : ["r", "d", "U", "f", "f", "d", "U", "d", "U", "b", "d", "d", "B", "D", "u", "D", "u", "f", "f", "D", "u", "R", "d", "d"], # 44+45
                         47 : ["f", "d", "U", "l", "l", "d", "U", "d", "U", "r", "d", "d", "R", "D", "u", "D", "u", "l", "l", "D", "u", "F", "d", "d"]} # 42+47

    steps = fish_method_steps[maxel]
    for move in steps:
        cube.rotate(move)
        result_steps.append(move)

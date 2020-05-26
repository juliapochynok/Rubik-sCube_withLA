from solve import find_cubie

# "D": [[41, 43, 46, 48], [16, 24, 40, 32], [22, 30, 14, 38],
#                                               [15, 23, 31, 39], [42, 45, 47, 44]]


def solve_bottom_corners(cube,result_steps):
    one_round(cube, result_steps)
    if not check_fourth_step(cube):
        solve_bottom_corners(cube, result_steps)


def one_round(cube, result_steps):
    methods = [[1, 2, 3, 4], [3, 1, 4, 2], [2, 4, 1, 3], [4, 3, 2, 1]]
    relations = cube.relation_representation["D"]
    for corner in range(len(relations[0])):
        c = find_cubie(cube, relations[0][corner])
        done = False
        i = corner - 1
        while not done:
            i = (i + 1) % 4
            if check_corner(cube, c, i):
                done = True
        method = methods[corner][i]
        if method == 1:
            continue
        elif method == 2:
            method_1_to_2(cube, corner, result_steps)
        elif method == 3:
            method_1_to_3(cube, corner, result_steps)
        elif method == 4:
            method_1_to_2(cube, corner, result_steps)
            cube.rotate("d")
            method_1_to_2(cube, corner, result_steps)
            cube.rotate("D")
            method_1_to_2(cube, corner, result_steps)


def check_fourth_step(cube):
    relations = cube.relation_representation["D"]
    for i in range(4):
        c = find_cubie(cube, relations[0][i])
        if not check_corner(cube, c, i):
            return False
    return True


def check_corner(cube, corner, i):
    relations = cube.relation_representation["D"]
    if corner == find_cubie(cube, relations[0][i], True):
        return True
    elif corner == find_cubie(cube, relations[1][i], True):
        return True
    elif corner == find_cubie(cube, relations[2][i], True):
        return True
    return False


def method_1_to_2(cube, place, result_steps):
    method_1_to_2_steps = [["r", "d", "R", "F", "D", "f", "r", "D", "R", "D", "D"],
                           ["b", "d", "B", "R", "D", "r", "b", "D", "B", "D", "D"],
                           ["f", "d", "F", "L", "D", "l", "f", "D", "F", "D", "D"],
                           ["l", "d", "L", "B", "D", "b", "l", "D", "L", "D", "D"]]
    steps = method_1_to_2_steps[place]
    for move in steps:
        cube.rotate(move)
        result_steps.append(move)


def method_1_to_3(cube, place, result_steps):
    cube.rotate("D")
    result_steps.append("D")
    method_1_to_2(cube, place, result_steps)
    cube.rotate("d")
    result_steps.append("d")


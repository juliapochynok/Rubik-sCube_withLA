def solve_second_layer(cube, result_steps):
    check_first_row(cube, result_steps)
    third_step_rec(cube, result_steps)


def third_step_rec(cube, result_steps):
    do_third_step(cube, result_steps)
    checked_res = check_third_step(cube)
    err = False
    if len(checked_res[0]) != 0:
        method_left(cube, checked_res[0][0], result_steps)
        err = True
    if len(checked_res[1]) != 0:
        method_right(cube, checked_res[1][0], result_steps)
        err = True
    if err:
        solve_second_layer(cube,result_steps)


def do_third_step(cube, result_steps):
    for side in cube.sides:
        for i in range(4):
            if cube.cube[side].face[2][1] == cube.ideal_cube[side].face[1][0]:
                method_left(cube, cube.ideal_cube[side].face[1][0], result_steps)
            elif cube.cube[side].face[2][1] == cube.ideal_cube[side].face[1][2]:
                method_right(cube, cube.ideal_cube[side].face[1][2], result_steps)
            else:
                cube.rotate("D")
                result_steps.append("D")


def check_first_row(cube, result_steps):
    j = 4
    while j > 0:
        rotated = False
        for side in cube.sides:
            face = cube.cube[side].face
            for i in range(len(face[0])):
                if face[0][i] != cube.ideal_cube[side].face[0][i]:
                    cube.rotate("U")
                    result_steps.append("U")
                    rotated = True
                    continue
        j -= 1
        if not rotated:
            break


def check_third_step(cube):
    res_left = []
    res_right = []
    for side in cube.sides:
        face = cube.cube[side].face
        if face[1][0] != cube.ideal_cube[side].face[1][0]:
            res_left.append(cube.ideal_cube[side].face[1][0])
        if face[1][2] != cube.ideal_cube[side].face[1][2]:
            res_right.append(cube.ideal_cube[side].face[1][2])
    return res_left, res_right


def method_left(cube, place, result_steps):
    method_left_steps = {
        20: ["D", "L", "d", "l", "d", "f", "D", "F"],
        12: ["D", "B", "d", "b", "d", "l", "D", "L"],
        36: ["D", "R", "d", "r", "d", "b", "D", "B"],
        28: ["D", "F", "d", "f", "d", "r", "D", "R"],
    }
    steps = method_left_steps[place]
    for move in steps:
        cube.rotate(move)
        result_steps.append(move)


def method_right(cube, place, result_steps):
    method_right_steps = {
        21: ["d", "r", "D", "R", "D", "F", "d", "f"],
        13: ["d", "f", "D", "F", "D", "L", "d", "l"],
        37: ["d", "l", "D", "L", "D", "B", "d", "b"],
        29: ["d", "b", "D", "B", "D", "R", "d", "r"],
    }
    steps = method_right_steps[place]
    for move in steps:
        cube.rotate(move)
        result_steps.append(move)

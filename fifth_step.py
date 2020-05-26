from solve import find_cubie


def fifth_step(cube, result_steps):
    rotated = 0
    while not check_bottom_corners(cube):
        if check_config_1(cube, rotated) or check_config_2(cube, rotated) or check_config_3(cube, rotated):
            method(cube, result_steps)
        else:
            cube.rotate("d")
            result_steps.append("d")
            rotated += 1
        if rotated > 3:
            method(cube, result_steps)
            rotated = 0


def check_config_1(cube, rotated):
    situations = [[43, 41], [48, 43], [46, 48], [41, 46]]
    situation = situations[rotated]
    return (find_cubie(cube, 24, True) == find_cubie(cube, situation[0])) and \
           (find_cubie(cube, 41, True) == find_cubie(cube, situation[1]))


def check_config_2(cube, rotated):
    situations = [[41, 46], [43, 41], [48, 43], [46, 48]]
    situation = situations[rotated]
    return (find_cubie(cube, 16, True) == find_cubie(cube, situation[0])) and \
           (find_cubie(cube, 14, True) == find_cubie(cube, situation[1]))


def check_config_3(cube, rotated):
    situations = [[46, 41], [43, 41], [48, 43], [46, 48]]
    situation = situations[rotated]
    return (find_cubie(cube, 14, True) == find_cubie(cube, situation[0])) and \
           (find_cubie(cube, 41, True) == find_cubie(cube, situation[1]))


def method(cube, result_steps):
    steps = ["r", "d", "R", "d", "r", "d", "d", "R", "d", "d"]
    for move in steps:
        cube.rotate(move)
        result_steps.append(move)


def check_bottom_corners(cube):
    return (find_cubie(cube, 46, True) == find_cubie(cube, 46)) and \
           (find_cubie(cube, 41, True) == find_cubie(cube, 41)) and \
           (find_cubie(cube, 43, True) == find_cubie(cube, 43)) and \
           (find_cubie(cube, 48, True) == find_cubie(cube, 48))

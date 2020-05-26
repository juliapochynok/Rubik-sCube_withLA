from solve import find_cubie


def sixth_step(cube, result_steps):
    side = check_config(cube)
    while side is None:
        finish_two_edges_method(cube, "F", result_steps)
        side = check_config(cube)
    lst = find_unsolved_edges(cube)
    fish = is_fish(cube, lst)
    H = is_H(cube, lst)
    if fish == "Done" or H == "Done":
        return
    same_side = 0
    iter = 0
    while not (fish or H):
        iter += 1
        if iter > 20:
            print("Step six is impossible")
            break
        finish_two_edges_method(cube, side, result_steps)
        lst = find_unsolved_edges(cube)
        fish = is_fish(cube, lst)
        H = is_H(cube, lst)
        new_side = check_config(cube)
        if side == new_side:
            same_side += 1
            if same_side >= 4:
                for s in cube.sides:
                    finish_two_edges_method(cube, s, result_steps)
                new_side = check_config(cube, side)
                same_side = 0
        while new_side is None:
            finish_two_edges_method(cube, "B", result_steps)
            new_side = check_config(cube)
        side = new_side

        if fish == "Done" or H == "Done":
            return


def check_config(cube, bad_side=None):
    d_rep = cube.relation_representation["D"]
    side = "A"
    for edge in range(len(d_rep[3])):
        if find_cubie(cube, d_rep[3][edge]) == find_cubie(cube, d_rep[3][edge], True):
            side = find_cubie(cube, d_rep[4][edge], True)[0]
        elif find_cubie(cube, d_rep[4][edge]) == find_cubie(cube, d_rep[3][edge], True):
            side = find_cubie(cube, d_rep[4][edge], True)[0]
        if side == bad_side:
            continue
        elif side != "A":
            return side


def finish_two_edges_method(cube, front,result_steps):
    front = cube.sides.index(front)
    finish_two_edges_method_steps = [["b", "F", "l", "f", "B", "d", "d", "b", "F", "l", "f", "B"],
                                     ["l", "R", "f", "r", "L", "d", "d", "l", "R", "f", "r", "L"],
                                     ["f", "B", "r", "b", "F", "d", "d", "f", "B", "r", "b", "F"],
                                     ["r", "L", "b", "l", "R", "d", "d", "r", "L", "b", "l", "R"]]
    steps = finish_two_edges_method_steps[front]
    for move in steps:
        cube.rotate(move)
        result_steps.append(move)


def find_unsolved_edges(cube):
    res = []
    down_face = cube.cube["D"].face
    for row in range(len(down_face)):
        for col in range(len(down_face[0])):
            if down_face[row][col] != cube.ideal_cube["D"].face[row][col]:
                if isinstance(down_face[row][col], str) or isinstance(cube.ideal_cube["D"].face[row][col], str):
                    continue
                res.append(down_face[row][col])
    return res


def is_H(cube, lst):
    if len(lst) > 2 or len(lst) == 1:
        # print("Error!!!")
        return False
    if len(lst) == 0:
        return "Done"
    first_edge_pos = find_cubie(cube, lst[0])
    second_edge_pos = find_cubie(cube, lst[1])
    return ((first_edge_pos[1] == second_edge_pos[1]) and (abs(first_edge_pos[2] - second_edge_pos[2]) == 2)) or \
           ((first_edge_pos[2] == second_edge_pos[2]) and (abs(first_edge_pos[1] - second_edge_pos[1]) == 2))


def is_fish(cube, lst):
    if len(lst) > 2 or len(lst) == 1:
        # print("Error!!!")
        return False
    if len(lst) == 0:
        return "Done"
    first_edge_pos = find_cubie(cube, lst[0])
    second_edge_pos = find_cubie(cube, lst[1])
    return (abs(first_edge_pos[1] - second_edge_pos[1]) == 1) and (abs(first_edge_pos[2] - second_edge_pos[2]) == 1)

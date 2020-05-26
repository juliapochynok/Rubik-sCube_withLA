from cube import Cube
from solve import find_cubie


def solve_corners(cube, prime_side):
    res_steps = []
    relations = cube.relation_representation[prime_side][0]
    for i in range(len(relations)):
        turn_u = 0
        j = 8
        while j > 0:
            pos_tup = find_cubie(cube, relations[i], True)
            corner = cube.cube[pos_tup[0]].face[pos_tup[1]][pos_tup[2]]
            if corner == cube.ideal_cube[pos_tup[0]].face[pos_tup[1]][pos_tup[2]]:
                j -= 1
                continue
            else:
                method = corner_method(cube, pos_tup, i, prime_side, turn_u)
            if method[0] == 1:
                corner_method1(cube, i,res_steps)
                break
            elif method[0] == 2:
                corner_method2(cube, i,res_steps)
                break
            elif method[0] == 3:
                corner_method3(cube, i,res_steps)
                break
            elif method[0] == 4:
                corner_method4(cube, i, res_steps)
                break
            elif method[0] == 5:
                corner_method5(cube, i, res_steps)
                break
            elif isinstance(method[0], int):
                corner_method6(cube, i, method[0], res_steps)
                break
            else:
                if j < 5:
                    turn_u += 1
                cube.rotate("D")
                res_steps.append("D")
                j -= 1

    return res_steps


def corner_method1(cube, i, res_lst):
    method1_steps = [["l", "d", "L"], ["b", "d", "B"], ["f", "d", "F"], ["r", "d", "R"]]
    steps = method1_steps[i]
    for move in steps:
        cube.rotate(move)
        res_lst.append(move)


def corner_method2(cube, i,res_lst):
    method2_steps = [["d", "l", "D", "L"], ["d", "b", "D", "B"],
                     ["d", "f", "D", "F"], ["d", "r", "D", "R"]]
    steps = method2_steps[i]
    for move in steps:
        cube.rotate(move)
        res_lst.append(move)


def corner_method3(cube, i, res_lst):
    method3_steps = [["l", "D", "L", "D", "D"], ["b", "D", "B", "D", "D"],
                     ["f", "D", "F", "D", "D"], ["r", "D", "R", "D", "D"]]
    steps = method3_steps[i]
    for move in steps:
        cube.rotate(move)
        res_lst.append(move)
    corner_method1(cube, i, res_lst)


def corner_method4(cube, i, res_lst):
    method4_steps = [["B", "D", "b", "D", "D", "l", "D", "L"],
                     ["R", "D", "r", "D", "D", "b", "D", "B"],
                     ["L", "D", "l", "D", "D", "f", "D", "F"],
                     ["F", "D", "f", "D", "D", "r", "D", "R"]]
    steps = method4_steps[i]
    for move in steps:
        cube.rotate(move)
        res_lst.append(move)


def corner_method5(cube, i, res_lst):
    corner_method1(cube, i, res_lst)
    cube.rotate("D")
    res_lst.append("D")
    corner_method1(cube, i, res_lst)


def corner_method6(cube, i, place, res_lst):
    place = place/10
    method6_steps = {35: [[corner_method4], # 1
                          ["B", "D", "b", "D", "D", corner_method2], # 3
                          ["B", "D", "b", corner_method2], # 6
                          ["B", "D", "b", "D", corner_method2]], # 8

                     9: [[corner_method5], # 1
                          ["B", "D", "b", "D", "D", corner_method3], # 3
                          ["B", "D", "b", corner_method3], # 6
                          ["B", "D", "b", "D", corner_method3]], # 8

                     27: [["b", "D", "B", "D", corner_method2],
                          [corner_method4],
                          ["b", "D", "B", "D", "D", corner_method2],
                          ["b", "D", "B", "d", corner_method2]],

                     33: [["R", "d", "r", "D", corner_method1],
                          [corner_method5],
                          ["R", "d", "r", "D", "D", corner_method1],
                          ["R", "d", "r", "d", corner_method1]],

                     11: [["f", "d", "F", corner_method3], # 1
                          ["f", "d", "F", "d", corner_method3], # 3
                          [corner_method4], # 6
                          ["f", "d", "F", "d", "d", corner_method3]], # 8

                     17: [["L", "d", "l", "d", corner_method1],
                          ["L", "d", "l", "d", "d", corner_method1],
                          [corner_method4],
                          ["L", "d", "l", "D", corner_method1]],

                     19: [["r", "d", "R", "d", corner_method3],
                          ["r", "d", "R", "D", "D", corner_method3],
                          ["r", "d", "R", corner_method3],
                          [corner_method4]],

                     25: [["F", "d", "f", "D", "D", corner_method1],
                          ["F", "d", "f", "D", corner_method1],
                          ["F", "d", "f", "d", corner_method1],
                          [corner_method5]],

                     1: [[None],
                         ["B", "d", "b", "d", corner_method2],
                         ["B", "d", "b", "D", corner_method2],
                         ["B", "d", "b", "d", "d", corner_method2]],

                     3: [["b", "d", "B", "d", "d", corner_method2],
                         [None],
                         ["b", "d", "B", "d", corner_method2],
                         ["b", "d", "B", corner_method2]],

                     6: [["L", "D", "l", "d", "d", corner_method1],
                         ["L", "D", "l", "D", corner_method1],
                         [None],
                         ["L", "D", "l", corner_method1]],

                     8: [["r", "d", "R", "d", corner_method2],
                         ["r", "d", "R", "d", "d", corner_method2],
                         ["r", "d", "R", corner_method2],
                         [None]],
                     }
    method = method6_steps[place]
    steps = method[i]
    for move in steps:
        if callable(move):
            move(cube, i, res_lst)
        elif move is None:
            continue
        else:
            cube.rotate(move)
            res_lst.append(move)


def corner_method(cube, pos_tup, i, prime_side, turn_u):
    places_4_5 = [35, 9, 27, 33, 11, 17, 19, 25, 1, 3, 6, 8]
    if turn_u > 0:
        for place in places_4_5:
            possible_pos = find_cubie(cube, place, True)
            el_in_possible_pos = cube.cube[possible_pos[0]].face[possible_pos[1]][possible_pos[2]]
            if el_in_possible_pos == cube.ideal_cube[pos_tup[0]].face[pos_tup[1]][pos_tup[2]]:
                return place*10, turn_u
    j = 1
    while True:
        if j > 5:
            # print("Error!!!")
            return None, None
            break
        possible_pos = find_cubie(cube, cube.relation_representation[prime_side][j][i], True)
        el_in_possible_pos = cube.cube[possible_pos[0]].face[possible_pos[1]][possible_pos[2]]
        if el_in_possible_pos == cube.ideal_cube[pos_tup[0]].face[pos_tup[1]][pos_tup[2]]:
            return j, turn_u
        j += 1


if __name__ == "__main__":
    c = Cube(3)

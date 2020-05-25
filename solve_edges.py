from cube import Cube
from solve import find_cubie


def solve_edges(cube, prime_side):
    relations = cube.relation_representation[prime_side][6]
    for i in range(len(relations)):
        j = 8
        middle_edge = 0
        while j > 0:
            pos_tup = find_cubie(cube, relations[i], True)
            edge = cube.cube[pos_tup[0]].face[pos_tup[1]][pos_tup[2]]
            if edge == cube.ideal_cube[pos_tup[0]].face[pos_tup[1]][pos_tup[2]]:
                j -= 1
                continue
            else:
                method = edge_method(cube, pos_tup, i, middle_edge, prime_side)
            if method[0] == 1:
                edge_method1(cube, i)
                break
            elif method[0] == 2:
                edge_method2(cube, i)
                break
            elif method[0] == 3:
                edge_method3(cube, i, method[1])
                break
            elif method[0] == 4:
                edge_method4(cube, i, method[1])
                break
            elif method[0] == 5:
                edge_method5(cube, i)
                break
            elif isinstance(method[0], int):
                edge_method6(cube, i, method[0])
            else:
                if j < 5:
                    middle_edge += 1
                cube.rotate("d")
                j -= 1


def edge_method(cube, pos_tup, i, middle_edge, prime_side):
    possible_places = [34, 26, 18, 10, 2, 5, 7, 4]
    j = 7
    i = (i + middle_edge) % 4
    while True:
        if middle_edge > 0 and not (j == 9 or j == 10):
            j += 1
            if j > 11:
                # print("Error!!!")
                return None, None
            continue
        if j > 11:
            for place in possible_places:
                possible_pos = find_cubie(cube, place, True)
                el_in_possible_pos = cube.cube[possible_pos[0]].face[possible_pos[1]][possible_pos[2]]
                if el_in_possible_pos == cube.ideal_cube[pos_tup[0]].face[pos_tup[1]][pos_tup[2]]:
                    return place * 10, middle_edge

            return None, None
        possible_pos = find_cubie(cube, cube.relation_representation[prime_side][j][i], True)
        el_in_possible_pos = cube.cube[possible_pos[0]].face[possible_pos[1]][possible_pos[2]]
        if el_in_possible_pos == cube.ideal_cube[pos_tup[0]].face[pos_tup[1]][pos_tup[2]]:
            return (j - 6), middle_edge
        j += 1


def edge_method1(cube, i):
    # method1_steps = [["L", "r", "b", "b", "l", "R"],
    #                  ["F", "b", "l", "l", "f", "B"],
    #                  ["B", "f", "r", "r", "F", "b"],
    #                  ["R", "l", "f", "f", "L", "r"]]
    method1_steps = [["L", "r", "b", "b", "l", "R"],
                     ["B", "f", "r", "r", "F", "b"],
                     ["R", "l", "f", "f", "L", "r"],
                     ["F", "b", "l", "l", "f", "B"]]
    steps = method1_steps[i]
    for move in steps:
        cube.rotate(move)


def edge_method2(cube, i):
    # method2_steps = [["b", "L", "r", "B", "l", "R"],
    #                  ["l", "F", "b", "L", "f", "B"],
    #                  ["r", "B", "f", "R", "F", "b"],
    #                  ["f", "R", "l", "F", "L", "r"]]
    method2_steps = [["d", "L", "r", "B", "l", "R"],
                     ["d", "f", "B", "R", "F", "b"],
                     ["d", "R", "l", "F", "L", "r"],
                     ["d", "F", "b", "L", "f", "B"]]
    steps = method2_steps[i]
    for move in steps:
        cube.rotate(move)


def edge_method3(cube, i, middle_edge):
    method3_steps = [["U", "d", "R", "u", "D", "b"],
                     ["U", "d", "F", "u", "D", "r"],
                     ["U", "d", "L", "u", "D", "f"],
                     ["U", "d", "B", "u", "D", "l"]]

    for j in range(middle_edge):
        cube.rotate("U")

    steps = method3_steps[(i + middle_edge) % 4]
    for move in steps:
        cube.rotate(move)

    for j in range(middle_edge):
        cube.rotate("u")


def edge_method4(cube, i, middle_edge):
    # method4_steps = [["U", "d", "b", "u", "D", "u", "D", "R"],
    #                  ["U", "d", "l", "u", "D", "u", "D", "B"],
    #                  ["U", "d", "r", "u", "D", "u", "D", "F"],
    #                  ["U", "d", "f", "u", "D", "u", "D", "L"]]
    method4_steps = [["U", "d", "r", "u", "D", "u", "D", "L", "U", "d"],
                     ["U", "d", "f", "u", "D", "u", "D", "B", "U", "d"],
                     ["U", "d", "l", "u", "D", "u", "D", "R", "U", "d"],
                     ["U", "d", "b", "u", "D", "u", "D", "F", "U", "d"]]
    for j in range(middle_edge):
        cube.rotate("U")

    steps = method4_steps[(i + middle_edge) % 4]
    for move in steps:
        cube.rotate(move)

    for j in range(middle_edge):
        cube.rotate("u")


def edge_method5(cube, i):
    edge_method1(cube, i)
    edge_method2(cube, i)


def edge_method6(cube, i, place):
    place = place / 10
    method6_steps = {34: [[edge_method5],
                          ["L", "r", "b", "l", "R", edge_method1],
                          ["L", "r", "b", "b", "l", "R", "D", "D", edge_method2],
                          ["L", "r", "B", "l", "R", edge_method1]],

                     26: [["B", "f", "R", "b", "F", edge_method1],
                          [edge_method5],
                          ["B", "f", "r", "b", "F", edge_method1],
                          ["B", "f", "R", "R", "b", "F", "D", "D", edge_method2]],

                     18: [["l", "R", "F", "F", "L", "r", "D", "D", edge_method2],
                          ["l", "R", "F", "L", "r", edge_method1],
                          [edge_method5],
                          ["l", "R", "f", "L", "r", edge_method1]],

                     10: [["b", "F", "l", "f", "B", edge_method1],
                          ["b", "F", "L", "L", "f", "B", "D", "D", edge_method2],
                          ["b", "F", "L", "f", "B", edge_method1],
                          [edge_method5]],
                     2: [[None],
                         ["L", "r", "b", "l", "R", edge_method2],
                         ["L", "r", "b", "l", "R", "d", edge_method2],
                         ["L", "r", "b", "l", "R", "d", "d", edge_method2]],
                     5: [["B", "f", "r", "b", "F", "d", "d", edge_method2],
                         [None],
                         ["B", "f", "r", "b", "F", edge_method2],
                         ["B", "f", "r", "b", "F", "d", edge_method2]],
                     7: [["l", "R", "f", "r", "L", "d", edge_method2],
                         ["l", "R", "f", "r", "L", "d", "d", edge_method2],
                         [None],
                         ["l", "R", "f", "r", "L", edge_method2]],
                     4: [["b", "F", "l", "B", "f", edge_method2],
                         ["b", "F", "l", "B", "f", "d", edge_method2],
                         ["b", "F", "l", "B", "f", "d", "d", edge_method2],
                         [None]]}
    method = method6_steps[place]
    steps = method[i]
    for move in steps:
        if callable(move):
            move(cube, i)
        elif move is None:
            continue
        else:
            cube.rotate(move)

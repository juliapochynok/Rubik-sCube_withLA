def find_cubie(cube, number, ideal=False):
    if ideal:
        c = cube.ideal_cube
    else:
        c = cube.cube
    for key in c:
        for row_index in range(len(c[key].face)):
            for col_index in range(len(c[key].face[row_index])):
                if c[key].face[row_index][col_index] == number:
                    return key, row_index, col_index

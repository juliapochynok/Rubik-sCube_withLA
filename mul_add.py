import copy


def matrix_multiplication(matrix1, matrix2):
    result = []
    if len(matrix1[0]) != len(matrix2):
        return None
    for i in range(len(matrix1)):
        row = matrix1[i]
        new_row = []
        for j in range(len(matrix2[0])):
            numb = 0
            for k in range(len(matrix2)):
                try:
                    numb += row[j]*matrix2[k][j]
                except:
                    # numb = row[j]
                    continue
            new_row.append(numb)
        result.append(new_row)
    return result


def matrix_add(matrix1, matrix2):
    result = []
    if len(matrix1) != len(matrix2):
        return None
    if len(matrix1[0]) != len(matrix2[0]):
        return None

    for i in range(len(matrix1)):
        new_row = []
        for j in range(len(matrix1[0])):
            if isinstance(matrix1[i][j], str):
                new_row.append(matrix1[i][j])
            if isinstance(matrix2[i][j], str):
                new_row.append(matrix2[i][j])
            else:
                new_row.append(matrix1[i][j]+matrix2[i][j])
        result.append(new_row)
    return result


def transpose(matrix):
    result = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[j][i]
    return result


def set_val(matrix, val, coordinates):
    matrix2 = copy.deepcopy(matrix)
    for i in coordinates:
        matrix2[i[0]][i[1]] = val
    return matrix2


def make_matrix_with_one(matrix, line):
    if line % 2 == 0:
        col = 0
    else:
        col = 2
    res = set_val(matrix, 1, [[0, col]])
    return res


def make_matrix_with_two_ones(matrix, line):
    res = matrix
    if line % 2 == 0:
        col = 0
    else:
        col = 2
    for i in range(3):
        if i == col:
            continue
        res = set_val(res, 1, [[0, i]])
    return res


if __name__ == "__main__":
    matrix1 = [[2, 3, 5],
               [2, 6, 7],
               [1, 2, 9]]

    matrix2 = [[0, 0, 0],
               [0, 0, 0],
               [0, 0,0]]
    # mat = matrix_multiplication(matrix1, matrix2)
    mat1 = make_matrix_with_one(matrix2, 2)
    mat2 = make_matrix_with_two_ones(matrix2, 2)

    # matrix3 = [[1, 2, 3],
    #            [1, 2, 3],
    #            [1, 2, 3]]
    #
    # for i in range(len(matrix3)):
    #     for j in range(len(matrix3)):
    #         print(" ", matrix3[i][j], end=" ")
    #     print()
    #
    #
    #
    # matrix3 = transpose(matrix3)
    # print()
    # print()
    #
    # for i in range(len(matrix3)):
    #     for j in range(len(matrix3)):
    #         print(" ", matrix3[i][j], end=" ")
    #     print()
    #
    # matrix3 = transpose(matrix3)
    # print()
    # print()

    for i in range(len(mat1)):
        for j in range(len(mat1)):
            print(" ", mat1[i][j], end=" ")
        print()
    for i in range(len(mat2)):
        for j in range(len(mat2)):
            print(" ", mat2[i][j], end=" ")
        print()

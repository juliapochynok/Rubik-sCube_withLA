from Face import Face
from mul_add import *

MATRIX_0 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


class Cube:

    def __init__(self, n):
        self.ideal_cube = {'U': Face(n, "U",  1), 'L': Face(n, "L", 9), 'F': Face(n, "F", 17),
        'R': Face(n, "R", 25), 'B': Face(n,  "B", 33), 'D': Face(n, "D", 41)}

        self.cube = {'U': Face(n, "U",  1), 'L': Face(n, "L", 9), 'F': Face(n, "F", 17),
        'R': Face(n, "R", 25), 'B': Face(n,  "B", 33), 'D': Face(n, "D", 41)}

        self.right_left_rotation = ["F", "R", "B", "L"]
        self.up_down_rotation = ["F", "U", "B", "D"]

        self.neighbour = {"U": ["B", "F", "L", "R"], "L": ["U", "D", "B", "F"], "F": ["U", "D", "L", "R"],
        "R": ["U", "D", "F", "B"], "B": ["D", "U", "L", "R"], "D": ["F", "B", "L", "R"],}

        self.n = n
        self.mix()

    def rotate(self, face_name, row, direction):
        if row == 0:
            self.change_row(0, direction)
            self.cube[self.neighbour[face_name][row]].rotate(direction*(-1))
        elif row == 1:
            self.change_row(2, direction)
            self.cube[self.neighbour[face_name][row]].rotate(direction)
        elif row == 2:
            self.change_column(0, direction)
            self.cube[self.neighbour[face_name][row]].rotate(direction*(-1))
        elif row == 3:
            self.change_column(2, direction)
            self.cube[self.neighbour[face_name][row]].rotate(direction)

    def change_column(self, col, direction):

        matrix_for_add1 = set_val(MATRIX_0, 1, [[0, col]])
        matrix_for_add2 = set_val(MATRIX_0, 1, [[0, abs(2-col)], [0, abs(1-col)]])
        vec_to_add = matrix_multiplication(self.cube[self.up_down_rotation[0]].face, matrix_for_add1)
        range_lst = []
        if direction == 1:
            range_lst = [1, 2, 3, 4]
        elif direction == -1:
            range_lst = [3, 2, 1, 0]
        for i in range_lst:
            matrix_to_add = matrix_multiplication(self.cube[self.up_down_rotation[i % 4]].face, matrix_for_add2)
            next_vec = matrix_multiplication(self.cube[self.up_down_rotation[i % 4]].face, matrix_for_add1)
            self.cube[self.up_down_rotation[i % 4]].face = matrix_add(matrix_to_add, vec_to_add)
            vec_to_add = next_vec

    def change_row(self, row, direction):
        matrix_for_add1 = set_val(MATRIX_0, 1, [[0, row]])
        matrix_for_add2 = set_val(MATRIX_0, 1, [[0, abs(2-row)], [0, abs(1-row)]])

        vec_to_add = matrix_multiplication(transpose(self.cube[self.right_left_rotation[0]].face), matrix_for_add1)
        range_lst = []
        if direction == 1:
            range_lst = [1, 2, 3, 4]
        elif direction == -1:
            range_lst = [3, 2, 1, 0]

        for i in range_lst:
            matrix_to_add = matrix_multiplication(transpose(self.cube[self.right_left_rotation[i % 4]].face), matrix_for_add2)
            next_vec = matrix_multiplication(transpose(self.cube[self.right_left_rotation[i % 4]].face), matrix_for_add1)
            self.cube[self.right_left_rotation[i % 4]].face = transpose(matrix_add(matrix_to_add, vec_to_add))
            vec_to_add = next_vec
    
    def show(self):
        for key in self.cube:
            print("\n{}:", key)
            print(self.cube[key].show_face())

    def mix(self):
        self.cube["U"].face = [[48, 21, 17], [13, "U", 18], [43, 37, 41]]
        self.cube["F"].face = [[24, 12, 22], [47, "F", 26], [35, 42, 25]]
        self.cube["L"].face = [[32, 20, 30], [44, "L", 39], [46, 45, 9]]
        self.cube["R"].face = [[16, 7, 6], [5, "R", 4], [19, 29, 27]]
        self.cube["B"].face = [[11, 28, 38], [10, "B", 15], [3, 2, 14]]
        self.cube["D"].face = [[1, 23, 8], [31, "D", 36], [40, 34, 33]]


    def mix2(self):
        self.cube["U"].face = [[48, 21, 17], [13, "U", 18], [43, 37, 41]]
        self.cube["F"].face = [[24, 12, 22], [4, "F", 26], [35, 42, 25]]
        self.cube["L"].face = [[32, 20, 30], [44, "L", 39], [46, 45, 9]]
        self.cube["R"].face = [[16, 7, 6], [5, "R", 47], [19, 29, 27]]
        self.cube["B"].face = [[11, 28, 38], [10, "B", 15], [3, 2, 14]]
        self.cube["D"].face = [[1, 23, 8], [31, "D", 36], [40, 34, 33]]

    def from_concole(self):
        pass


if __name__ == "__main__":
    cube1 = Cube(3)
    # cube1.show()
    cube1.rotate("F", 3, -1)
    cube1.show()

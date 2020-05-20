from Face import Face
from mul_add import *

MATRIX_0 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


class Cube:

    def __init__(self, n):

        self.relation_representation = {"F": [[17, 19, 22, 24], [9, 3, 46, 32], [1, 27, 14, 48],
                                              [35, 33, 40, 38],
                                              [6, 25, 16, 43], [11, 8, 41, 30], [18, 21, 23, 20], [7, 28, 42, 13]],

                                        "B": [[33, 35, 40, 38], [34, 37, 39, 36], [3, 9, 46, 32],
                                              [2, 12, 47, 29], [1, 14, 48, 27]],
                                        "L": [[9, 11, 16, 14], [10, 13, 15, 12], [1, 17, 41, 40],
                                              [4, 20, 44, 37], [6, 22, 46, 35]],

                                        "U": [[1, 3, 6, 8], [14, 38, 22, 30], [40, 32, 16, 24],
                                              [46, 48, 41, 43], [35, 27, 11, 19], [9, 33, 17, 25],
                                              [2, 5, 7, 4], [10, 34, 26, 18]],

                                        "D": [[41, 43, 48, 46], [42, 45, 47, 44], [14, 22, 30, 38],
                                              [15, 23, 31, 39], [16, 24, 32, 40]],
                                        "R": [[25, 27, 32, 30], [26, 29, 31, 28], [3, 38, 43, 19],
                                              [5, 36, 45, 21], [8, 33, 48, 24]]}

        self.ideal_cube = {'U': Face(n, "U", 1), 'L': Face(n, "L", 9), 'F': Face(n, "F", 17),
                           'R': Face(n, "R", 25), 'B': Face(n, "B", 33), 'D': Face(n, "D", 41)}

        self.cube = {'U': Face(n, "U", 1), 'L': Face(n, "L", 9), 'F': Face(n, "F", 17),
                     'R': Face(n, "R", 25), 'B': Face(n, "B", 33), 'D': Face(n, "D", 41)}

        self.right_left_rotation = ["F", "R", "B", "L"]
        self.up_down_rotation = ["F", "U", "B", "D"]

        self.neighbour = {"U": ["B", "F", "L", "R"], "L": ["U", "D", "B", "F"], "F": ["U", "D", "L", "R"],
                          "R": ["U", "D", "F", "B"], "B": ["D", "U", "L", "R"], "D": ["F", "B", "L", "R"]}

        self.neighbour2 = {"U": ["B", "F", "L", "R"], "L": ["U", "D", "B", "F"], "F": ["U", "D", "L", "R"],
                           "R": ["U", "D", "F", "B"], "B": ["D", "U", "L", "R"], "D": ["F", "B", "L", "R"]}

        self.n = n
        self.sides_relations = {"U": [["B", 0, -1], ["R", 0, -1], ["F", 0, -1],  ["L", 0, -1]],
                                "L": [["F", 2, -1], ["D", 2, -1], ["B", 3, 1], ["U", 2, -1]],
                                "F": [["U", 1, 1], ["R", 2, -1], ["D", 0, -1],  ["L", 3, 1]],
                                "R": [["U", 3, 1], ["B", 2, -1], ["D", 3, 1],  ["F", 3, 1]],
                                "B": [["U", 0, -1], ["L", 2, -1], ["D", 1, 1],  ["R", 3, 1]],
                                "D": [["F", 1, 1], ["R", 1, 1], ["B", 1, 1],  ["L", 1, 1]]}

    def rotate(self, letter):
        if ord(letter) < 97:
            direction = 1
        else:
            direction = -1
            letter = letter.upper()
        self.cube[letter].rotate(direction)
        self.change_sides(letter, direction)

    def change_sides(self, let, direction):
        order = self.sides_relations[let]

        j = len(order)
        index = len(order)-1

        vec_to_add = self.find_vector_to_add(order[index])

        while j > 0:
            if direction > 0:
                index = (index + 1) % 4
            else:
                index -= 1

            transp = False
            letter = order[index][0]
            line = order[index][1]

            matrix_with_two_ones = make_matrix_with_two_ones(MATRIX_0, line)

            if line <= 1:
                transp = True
                matrix_to_add = matrix_multiplication(transpose(self.cube[letter].face),
                                                      matrix_with_two_ones)
            else:
                matrix_to_add = matrix_multiplication(self.cube[letter].face, matrix_with_two_ones)

            if transp:
                matrix_to_add = transpose(matrix_to_add)

            if (direction > 0 and let == "F") or (direction < 0 and let == "B"):
                vec_to_add.reverse()
                vec_to_add = transpose(vec_to_add)
            if (direction < 0 and let == "F") or (direction > 0 and let == "B"):
                for r in vec_to_add:
                    r.reverse()
                vec_to_add = transpose(vec_to_add)

            if letter == "B" and not transp:
                vec_to_add.reverse()
                for r in vec_to_add:
                    r.reverse()

            res = matrix_add(matrix_to_add, vec_to_add)

            vec_to_add = self.find_vector_to_add(order[index])

            self.cube[letter].face = res

            j -= 1

    def find_vector_to_add(self, side):
        transp = False
        letter = side[0]
        line = side[1]
        matrix_with_one = make_matrix_with_one(MATRIX_0, line)

        if line <= 1:
            transp = True
            vec_to_add = matrix_multiplication(transpose(self.cube[letter].face),
                                               matrix_with_one)
        else:
            vec_to_add = matrix_multiplication(self.cube[letter].face, matrix_with_one)
        if letter == "B" and not transp:
            vec_to_add.reverse()
            for row in vec_to_add:
                row.reverse()

        if transp:
            vec_to_add = transpose(vec_to_add)
        return vec_to_add

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
        self.cube["F"].face = [[24, 12, 22], [47, "F", 26], [35, 42, 25]]
        self.cube["L"].face = [[32, 20, 30], [44, "L", 39], [1, 45, 9]]
        self.cube["R"].face = [[16, 7, 6], [5, "R", 4], [19, 29, 27]]
        self.cube["B"].face = [[11, 28, 38], [10, "B", 15], [3, 2, 14]]
        self.cube["D"].face = [[46, 23, 8], [31, "D", 36], [40, 34, 33]]

    def from_concole(self):
        pass


if __name__ == "__main__":
    cube1 = Cube(3)
    # cube1.mix2()
    # cube1.show()
    # cube1.rotate("B", 2, 1)
    cube1.rotate("d")
    cube1.show()

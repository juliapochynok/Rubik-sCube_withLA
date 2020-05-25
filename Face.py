class Face:
    def __init__(self, n, letter, first_el):
        self.n = n
        self.letter = letter
        self.first_el = first_el
        if isinstance(self.first_el, list):
            self.face = self.set_face()
        else:
            self.face = self.create_face()

    def create_face(self):
        lst = []
        curr_el = self.first_el
        for i in range(self.n):
            row = []
            for j in range(self.n):
                if i == self.n//2 and j == self.n//2:
                    row.append(self.letter)
                    curr_el -= 1
                else:
                    row.append(curr_el)
                curr_el += 1
            lst.append(row)
        return lst

    def set_face(self):
        lst = []
        curr_el = 0
        for i in range(self.n):
            row = []
            for j in range(self.n):
                if i == self.n // 2 and j == self.n // 2:
                    row.append(self.letter)
                else:
                    row.append(self.first_el[curr_el])
                    curr_el += 1
            lst.append(row)
        return lst

    def show_face(self):
        for i in range(self.n):
            for j in range(self.n):
                print(" ", self.face[i][j], end=" ")
            print()

    def rotate(self, prop):
        if prop > 0:
            direction = 1
        else:
            direction = -1
        amount = abs(prop) % 4
        for i in range(amount):
            new_matr = []
            for i in range(self.n):
                new_row = []
                for j in range(self.n):
                    coords = self.change_coords([i, j], direction)
                    new_row.append(self.face[coords[0]][coords[1]])
                new_matr.append(new_row)
            self.face = new_matr

    def change_coords(self, coords, direction):
        new_c = [0, 0]
        x = 0
        y = 1
        if direction > 0:
            x = 1
            y = 0

        new_c[x] = coords[y]
        if coords[x] == 1:
            new_c[y] = 1
        else:
            new_c[y] = abs(coords[x] - (self.n - 1)) % self.n
        return new_c

    def __ne__(self, other):
        for row in range(len(self.face)):
            for col in range(len(self.face[row])):
                if self.face[row][col] != other.face[row][col]:
                    if isinstance(other.face[row][col], str) or isinstance(self.face[row][col], str):
                        continue
                    return True
        return False

    def __eq__(self, other):
        for row in range(len(self.face)):
            for col in range(len(self.face[row])):
                if self.face[row][col] != other.face[row][col]:
                    return False
        return True


if __name__ == "__main__":
    f = Face(3, "R", [33, 21, 11, 32, 16, 13, 5, 3])
    f.show_face()
    f.rotate(1)
    print()
    print()
    print()
    f.show_face()

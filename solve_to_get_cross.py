from cube import Cube


def flipping(make_flip):
    for coord in range(4):
        if c.ideal_cube["U"].face[coords[coord][0]][coords[coord][1]] == \
                c.cube["U"].face[coords[coord][0]][coords[coord][1]]:
            continue
        else:
            move = make_flip(coord)
            if move:
                moves.append(move)


def make_cross():
    flipping(first_flip)
    flipping(second_flip)


def first_flip(cell):
    for flip in range(3):
        c.rotate("U", cell, 1)
        if c.ideal_cube["U"].face[coords[cell][0]][coords[cell][1]] == \
                c.cube["U"].face[coords[cell][0]][coords[cell][1]]:
            return flip + 1
    c.rotate("U", cell, 1)
    return False


def second_flip(cell):
    for flip in range(3):
        c.rotate("U", order[cell], 1)
        move = first_flip(cell)
        if move:
            return [flip, move]
    c.rotate("U", order[cell], 1)
    return False


if __name__ == "__main__":
    c = Cube(3)
    coords = [(0, 1), (2, 1), (1, 0), (1, 2)]
    order = [2, 3, 0, 1]
    moves = []
    make_cross()
    c.show()

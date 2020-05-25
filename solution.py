from cube import Cube
from solve_corners import solve_corners
from solve_edges import solve_edges


class Solution:
    def __init__(self, cube):
        self.prime_side = "U"
        self.cube = cube

    def solve_corners(self):
        solve_corners(self.cube, self.prime_side)

    def solve_edges(self):
        solve_edges(self.cube, self.prime_side)



if __name__ == "__main__":
    c = Cube(3)
    f = open("seed_bad2.txt", "w")
    # c.shuffle(4)
    # s = Solution(c)
    # s.solve_corners()
    # s.solve_edges()
    for i in range(1000):
        c.shuffle(i)

        # c.show()
        s = Solution(c)
        s.solve_corners()
        s.solve_edges()
        if s.cube.cube["U"] != s.cube.ideal_cube["U"]:
            f.write(str(i))
            f.write("\n")
    # c.show()
    f.close()
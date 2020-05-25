from cube import Cube
from solve_corners import solve_corners
from solve_edges import solve_edges
from third_step import solve_second_layer, check_third_step
from forth_step import solve_bottom_corners

class Solution:
    def __init__(self, cube):
        self.prime_side = "U"
        self.cube = cube

    def solve_corners(self):
        solve_corners(self.cube, self.prime_side)

    def solve_edges(self):
        solve_edges(self.cube, self.prime_side)

    def solve_second_layer(self):
        solve_second_layer(self.cube)

    def solve_bottom_corners(self):
        solve_bottom_corners(self.cube)


if __name__ == "__main__":
    c = Cube(3)
    # f = open("seed_bad.txt", "w")
    c.shuffle(13)
    s = Solution(c)
    s.solve_corners()
    s.solve_edges()
    s.solve_second_layer()
    s.solve_bottom_corners()
    # for i in range(1000):
    #     c.shuffle(i)
    #     s = Solution(c)
    #     s.solve_corners()
    #     s.solve_edges()
    #     s.solve_second_layer()
    #     s.solve_bottom_corners()
    #     lst = check_third_step(s.cube)
    #     if s.cube.cube["U"] != s.cube.ideal_cube["U"]:
    #         f.write(str(i))
    #         f.write("\n")
    #
    #     elif (len(lst[0]) != 0) or (len(lst[1]) != 0):
    #         f.write(str(i))
    #         f.write("\n")
    c.show()
    # f.close()
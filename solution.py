from cube import Cube
from solve_corners import solve_corners
from solve_edges import solve_edges
from third_step import solve_second_layer, check_third_step
from forth_step import solve_bottom_corners
from fifth_step import fifth_step, check_bottom_corners
from step_six import sixth_step
from step_seven import solve_down_edges


class Solution:
    def __init__(self, cube):
        self.prime_side = "U"
        self.cube = cube
        self.shuffle_steps = []
        self.result_steps = []

    def shuffle(self, seed):
        self.shuffle_steps = self.cube.shuffle(seed)

    def solve_cube(self):
        self.result_steps = solve_corners(self.cube, self.prime_side)
        solve_edges(self.cube, self.prime_side, self.result_steps)
        solve_second_layer(self.cube, self.result_steps)
        solve_bottom_corners(self.cube, self.result_steps)
        fifth_step(self.cube, self.result_steps)
        sixth_step(self.cube, self.result_steps)
        solve_down_edges(self.cube, self.result_steps)

    def shuffle_user(self, steps):
        self.shuffle_steps = steps
        for el in steps:
            self.cube.rotate(el)


if __name__ == "__main__":
    c = Cube(3)
    f = open("seed_bad.txt", "w")
    # c.shuffle(19)
    # c.shuffle(74)
    # s = Solution(c)
    # s.solve_corners()
    # s.solve_edges()
    # s.solve_second_layer()
    # s.solve_bottom_corners()
    # s.fifth_step()
    # s.sixth_step()
    # s.solve_down_edges()
    for i in range(10):

        s = Solution(c)
        s.shuffle(i)
        s.solve_cube()
        for key in s.cube.cube:
            if s.cube.cube[key] != s.cube.ideal_cube[key]:
                f.write(str(i))
                f.write("\n")
                f.flush()
                break
        f.write("shuffle_steps: " + str(s.shuffle_steps))
        f.write("\n")
        f.write("result_steps: " + str(s.result_steps))
        f.write("\n")
        f.flush()
    # c.show()
    f.close()

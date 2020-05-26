from cube import Cube
from solution import Solution
from simplify import simplify, simplify_user



def start_cube():
    c = Cube(3)
    s = Solution(c)
    possible_steps = ['D', 'd', 'U', 'u', 'L', 'l', 'R', 'r', 'B', 'b', 'F', 'f']

    print("Hello! Here is the program to help you with solving Rubik's Cube.")
    print("Do you want to shuffle cube yourself, or perform autoshuffle? (enter 'my' for your shuffle or enter 'auto' for shuffle)")
    shuffle_type = str(input())
    shuffle_type = shuffle_type.strip().lower()

    if shuffle_type == "my":
        print("Enter steps you want to make seperated by spaces (possible steps: D, d, U, u, L, l, R, r, B, b, F, f)")
        shuffle_steps_str = str(input())
        shuffle_steps = shuffle_steps_str.split()
        for i in shuffle_steps:
            if i not in possible_steps:
                print("Invalid input! No such steps allowed")
                return 1
        s.shuffle_user(shuffle_steps)
    elif shuffle_type == "auto":
        print("Enter numeric value of seed which is used to generate random steps")
        try:
            shuffle_seed = int(input())
        except:
            print("Invalid input! Try again")
            return 1
        s.shuffle(shuffle_seed)
        print("Used steps to shuffle the cube:")
        print(s.shuffle_steps)
    else:
        print("Invalid input! Try again")
        return 1
    
    s.solve_cube()
    # vidualizatsia
    result_steps = s.result_steps
    for i in range(3):
        result_steps = simplify(result_steps)



    print("Steps to solve a cube:")
    print(simplify_user(result_steps))

    return s.shuffle_steps, result_steps


if __name__ == "__main__":
    steps = start_cube()

    # c = Cube_vis(3)
    # shuffle_moves = steps[0]
    # result_moves = steps[1]
    # shuffle_vis(c, shuffle_moves)
    # c.move_list = result_moves
    # c.draw_interactive()
    # plt.show()

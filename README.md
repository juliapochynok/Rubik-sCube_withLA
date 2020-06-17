# Solution of the Rubik’s Cube with Linear Algebra



## Description
The cube has 43,252,003,274,489,856,000 (43 quintillions) possible positions, and only one is the correct one. 
As in any period of time cube can be in any of these positions, moreover, there is only a certain amount of positions one can move to in one step, the main problem, and the main difficulty of this puzzle is to transfer from a given position to the correct one. 

![](https://github.com/sophiakravchuk/Rubik-sCube_withLA/blob/master/images/LA1.png?raw=true)


The main goal of our project was to make a program that finds moves to solve a  Rubik’s Cube from certain state.

## Notation
![](https://github.com/sophiakravchuk/Rubik-sCube_withLA/blob/master/images/LA2.png?raw=true)

This form of notation is used to represent the cube in our project.

Cube 3x3x3 has 6 faces, each of which in real life is marked by colour. As our project is a python script and not AI for us it is more convenient to use numbers as unique indicators of the cell of the face, than colours. 

Every block on the Rubik's Cube is unique. One can divide them into three categories. Corners, sides, and middles. Middles never move, so one does not need to worry about them. Side blocks have eight positions and two rotations for each position. Corner blocks have eight positions and three rotations for each position. That means that one could write each move as a linear transformation that affects only the eight blocks involved. 

Each face is represented as a 3x3 matrix. Inside the matrix in the middle cell the letter is placed to indicate the position of the face relative to the static position of the cube. There are 6 letters with such meanings:

"U" - upper

"F" - front

"R" - right

"L" - left

"D" - down

"B" - bottom

In the picture above one can see the appearance of the cube in this representation in solved form. When the cube is shuffled, certain numbers will not be placed in their original positions, but the middle of the matrix always remains unchanged and indicates the face of the cube.

![](https://github.com/sophiakravchuk/Rubik-sCube_withLA/blob/master/images/LA3.png?raw=true)
![](https://github.com/sophiakravchuk/Rubik-sCube_withLA/blob/master/images/la4.png?raw=true)

In order for a person to be able to use the result of our program, we use the following notation:


Instead of  X or Y one needs to substitute one of the six letters that represent the face of the cube.
 - X - turn a face X 90° clockwise. ( Ex: one can see “R” turn on the right illustration in the upper row of pictures or “D” rotation on the right one in lower row)

 - x - turn a face X 90° counterclockwise (Ex: One can see “f” rotation illustrated in lower row on the left picture)
 - X*Y - sequence X, Y  must be rotated in such order.


## Incoming and outgoing data
We have two shuffle options for our cube:
- user can enter sequence of moves to perform for shuffling
- program can perform auto shuffle
	
We perform our algorithm for getting a step by step solution of the shuffled cube and then display steps on the screen.	
We can evaluate correctness of found solution by performing it in visualization or by checking if all numbers are in their correct positions.

## Approach and LA methods
### Approach for solving the cube
In this project we used Denny Dedmore approach for solving Rubik's Cube.
The algorithm consists of seven main parts:
 - Top Row Corners
 - Top Edges 
 - Center and Middle Layer Edges
 - Turn the Cube Over and Arrange the Last Layer Corners
 - Completely Finish the Last Layer Corners
 - Completely Finish Two Edges and Prepare the Remaining Two
 - Solve
 
Each part consists of 2 to 5 move-sequences (“moves” can be raising the first column up, turning the last row left or rotating a certain face of the cube) that need to be performed in a certain order.

### LA methods
Matrix multiplication - we use this method to separate the certain row or column that is needed to make a move. 


Matrix addition - we use this method to combine two matrices earlier made by matrix multiplication. 


Matrix transposition - we use the transposition method for matrices to reorganize the position of the cells of the side when rotating one of the sides because during one rotation they change their position.

![](https://github.com/sophiakravchuk/Rubik-sCube_withLA/blob/master/images/LA10.png?raw=true)

## Usage Example

![](https://github.com/sophiakravchuk/Rubik-sCube_withLA/blob/master/images/ezgif.com-video-to-gif%20(2).gif?raw=true)
![](https://github.com/sophiakravchuk/Rubik-sCube_withLA/blob/master/images/ezgif.com-video-to-gif.gif?raw=true)

Our progam solves 88% entirely and 12% - almost entirely.

## Run Dependencies
To run the project you will need to download this repository and run command in command line. 

Example:

![](https://github.com/sophiakravchuk/Rubik-sCube_withLA/blob/master/images/ezgif.com-video-to-gif%20(1).gif?raw=true)

## Visualization
For better understanding of our project we took visualization of the Rubik's Cube written by David W. Hogg (NYU) and Jacob Vanderplas (UW). So we do not own any of the code for vizualization and all credits for it are to its authors.
You can find his whole version here https://github.com/davidwhogg/MagicCube


## Team
Sophia Kravchuk, Julia Pochynok, Sophia Haletska

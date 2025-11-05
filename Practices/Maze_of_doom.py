#PS 1st Maze generator

import turtle
import random

#types of walls the code can make
size_of_squares = 25
F = False
T = True
Bools = [T,F]
ex_col = [F,F,F,F,F,F,F,F]
ex_row = [F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F]
#all the rows in the grid
grid_rows =  []
#columns
grid_columns = []

#updating a column
for x in range(0,19):
    for y in range(0,8):
        #change each part of a column
        ex_col[y] = random.choice(Bools)
    #add that column to the maze
    grid_columns.append(ex_col)
    ex_col = [F,F,F,F,F,F,F,F]

print(grid_columns)

for x in range(0,10):
    for y in range(0,19):
        #change each part of a row
        ex_row[y] = random.choice(Bools)
    #add that new randomized row to the grid
    grid_rows.append(ex_row)
    ex_row = [F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F]
print(grid_rows)



#Maze solvable function
def solvability(grid_row,grid_col):
    #coords are realtive to the walls not the turtle
    #starting position is going to be
    to_be_checked_coords = [(11,0)]
    #vars for coords
    visited = []
    maze_size = len(grid_row) - 1
    while to_be_checked_coords:
        #get coordinates for checking
        x , y = to_be_checked_coords.pop()

        if x == maze_size-1 and y == maze_size -1:
            return True
        
        if (x , y) in visited: 
            continue

        #adds the new coordinates to the checked portion

        visited.append((x,y))


    #checks if there is a wall north of it
        if y > 0 and grid_row[y][x] == False:
            to_be_checked_coords.append((x,y-1))
    #checks if there is a wall west of it
        if x > 0 and grid_col[y][x] == False:
            to_be_checked_coords.append((x-1,y))

    #checks if there is a wall east of it
        if x < maze_size - 1 and grid_col[y][x+1] == False:
            to_be_checked_coords.append((x+1,y))

    #checks if there is a wall south of it
        if y < maze_size -1 and grid_row[y+1][x] == False:
            to_be_checked_coords.append((x,y+1))

solvability(grid_rows,grid_columns)

#create turtle
Bob_the_builder = turtle.Turtle()

#draw outside boundary

Bob_the_builder.penup()
Bob_the_builder.goto(-250,250)
Bob_the_builder.pendown()
Bob_the_builder.forward(250)
Bob_the_builder.penup()
Bob_the_builder.forward(25)
Bob_the_builder.pendown()
Bob_the_builder.forward(250)
Bob_the_builder.right(90)
Bob_the_builder.forward(250)
Bob_the_builder.right(90)
Bob_the_builder.forward(250)
Bob_the_builder.penup()
Bob_the_builder.forward(25)
Bob_the_builder.pendown()
Bob_the_builder.forward(250)
Bob_the_builder.right(90)
Bob_the_builder.forward(250)
Bob_the_builder.right(90)
#draw the walls inside
for w in grid_rows:
    Bob_the_builder.goto(-250,225)
    for a in w:
        if w == F:
            Bob_the_builder.penup()
        elif w == T:
            Bob_the_builder.pendown()
        Bob_the_builder.forward(1.25)


turtle.done()
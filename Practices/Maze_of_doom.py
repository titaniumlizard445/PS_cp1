#PS 1st Maze generator

import turtle
import random

#types of walls the code can make
size_of_squares = 25
F = False
T = True
#updating a column
def randomize_columns():
    F = False
    T = True
    Bools = [T,F]
    ex_col = [F,F,F,F,F,F,F,F,F,F]
    #columns
    grid_columns = []
    for x in range(0,21):
        for y in range(0,10):
            #change each part of a column
            ex_col[y] = random.choice(Bools)
        #add that column to the maze
        grid_columns.append(ex_col)
        ex_col = [F,F,F,F,F,F,F,F,F,F]
    print(grid_columns)
    return grid_columns

def Randomize_rows():
    F = False
    T = True
    Bools = [T,F]
    ex_row = [F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F]
    #all the rows in the grid
    grid_rows =  []
    for x in range(0,9):
        for y in range(0,20):
            #change each part of a row
            ex_row[y] = random.choice(Bools)
        #add that new randomized row to the grid
        grid_rows.append(ex_row)
        ex_row = [F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F,F]
    print(grid_rows)
    return grid_rows
    



#Maze solvable function
def solvability(grid_row,grid_col):
    #coords are realtive to the walls not the turtle
    #starting position is going to be
    to_be_checked_coords = [(11,0)]
    #vars for coords
    visited = []
    maze_size = len(grid_row)
    while to_be_checked_coords:
        #get coordinates for checking
        x , y = to_be_checked_coords.pop()

        #if it is outside the maze on the other side
        if x == 11 and y == 9:
            return True
        
        #if the space has already been checked
        if (x , y) in visited: 
            continue

        #adds the new coordinates to the checked portion

        visited.append((x,y))


    #checks if there is a wall north of it
        if y > 0 and grid_row[y][x] == False:
            to_be_checked_coords.append((x,y+1))
    #checks if there is a wall west of it
        if x > 0 and grid_col[x-1][y] == False:
            to_be_checked_coords.append((x+1,y))
    #checks if there is a wall east of it
        if x < maze_size - 1 and grid_col[y][x-1] == False:
            to_be_checked_coords.append((x-1,y))
    #checks if there is a wall south of it
        if y < maze_size-1 and grid_row[y-1][x] == False:
            to_be_checked_coords.append((x,y-1))

    return False


#runs till the maze is solvable
solved = False
while not solved:
    randomize_columns()
    Randomize_rows()
    solved = solvability(Randomize_rows(),randomize_columns())




#create turtle
Bob_the_builder = turtle.Turtle()

#draw outside boundary
def Outside_boundary():
    Bob_the_builder.speed(0)
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

Outside_boundary()
#draw the walls inside

#horizontal walls
Bob_the_builder.goto(-250,225)
iterator = 0
for w in Randomize_rows():
    iterator += 1
    Bob_the_builder.goto(-250,iterator*25)
    #draws a wall when there is true else it has the pen up and moves forward
    for a in w:
        if a == False:
            Bob_the_builder.penup()
        elif a == True:
            Bob_the_builder.pendown()
        Bob_the_builder.forward(25)
        Bob_the_builder.penup()


Bob_the_builder.goto(250,250)
iterator = 0
Bob_the_builder.right(90)
for w in randomize_columns:
    iterator += 1
    Bob_the_builder.goto(275-(25*iterator),250)
    #draws a wall when there is true else it has the pen up and moves forward
    for a in w:
        if a == False:
            Bob_the_builder.penup()
        elif a == True:
            Bob_the_builder.pendown()
        Bob_the_builder.forward(25)
        Bob_the_builder.penup()


turtle.done()
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




#functions for drawing each wall


def vertical_wall():
    print("bob")

def horizontal_wall():
    print("the ram")

#Maze solvable function
def solvability():
    print("bob")



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



turtle.done()
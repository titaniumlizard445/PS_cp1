#PS 1st Maze generator

import turtle
import random

#types of walls the code can make
size_of_squares = 25
walls = ["_","| "," |","-"," "]
#all the rows in the grid
grid_rows =  [[],[],[],[],[],[],[],[]]
#columns
grid_columns = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

for row in grid_rows:
    for space in row:
        grid_rows[row[space]] = random.choice(walls)

print(grid_rows)
#functions for drawing each type of wall


def left_side_wall():
    print("bob")

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



turtle.done()
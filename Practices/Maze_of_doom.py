#PS 1st Maze generator

import turtle
import random

#types of walls the code can make
size_of_squares = 25
walls = ["_","| "," |","-"]
bottom_and_top_row_ = ["_","_","_","_","_","_","_","_","_","_","_","_"," ","_","_","_","_","_","_","_","_","_","_","_","_","_"]
row = []
maze = [row,row,row,row,row,row,row,row,row,row,row,row,row,row,row,row,row,row,row,row,row,row,row,row,row,row]
#functions for drawing each type of wall

def left_side_wall():
    print("bob")
    

#create turtle
Bob_the_builder = turtle.Turtle()

#loop to make the whole maze
for x in maze:
    if x == 0:
        print("bob")

#draw predetermined top row
#draw the row
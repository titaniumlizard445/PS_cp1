#PS 1st turtle race

import random
import turtle as Bob

Finish = False
winner = ""
screen = Bob.Screen()
screen.setup(1000,1000)
screen.title("The Amazing Turtle Race!")

writingturtle = Bob.Turtle()
turtle1 = Bob.Turtle()
turtle2 = Bob.Turtle()
turtle3 = Bob.Turtle()
turtle4 = Bob.Turtle()
turtle5 = Bob.Turtle()

writingturtle.color("black")
turtle1.shape("turtle")
turtle1.color("blue")
turtle2.shape("turtle")
turtle2.color("red")
turtle3.shape("turtle")
turtle3.color("green")
turtle4.shape("turtle")
turtle4.color("yellow")
turtle5.shape("turtle")
turtle5.color("magenta")

writingturtle.penup()
turtle1.penup()
turtle2.penup()
turtle3.penup()
turtle4.penup()
turtle5.penup()

#setup
writingturtle.goto(-450,450)
writingturtle.pendown()
writingturtle.forward(800)
writingturtle.right(90)
writingturtle.forward(500)
writingturtle.right(90)
writingturtle.forward(800)
writingturtle.penup()
writingturtle.goto(-450,50)
writingturtle.pendown()
writingturtle.right(180)
writingturtle.forward(800)
writingturtle.penup()
writingturtle.goto(-450,150)
writingturtle.pendown()
writingturtle.forward(800)
writingturtle.penup()
writingturtle.goto(-450,250)
writingturtle.pendown()
writingturtle.forward(800)
writingturtle.penup()
writingturtle.goto(-450,350)
writingturtle.pendown()
writingturtle.forward(800)

writingturtle.penup()
writingturtle.goto(300,450)
writingturtle.right(90)
writingturtle.pendown()
writingturtle.forward(500)
writingturtle.penup()
writingturtle.goto(1000,1000)

#position
turtle1.goto(-400,400)
turtle2.goto(-400,300)
turtle3.goto(-400,200)
turtle4.goto(-400,100)
turtle5.goto(-400,0)

#put pendown for racing turtles
turtle1.pendown()
turtle2.pendown()
turtle3.pendown()
turtle4.pendown()
turtle5.pendown()


#race

while Finish == False:
    turtle1.forward(random.randint(1,25))
    t1pos = turtle1.position()
    if t1pos[1] >= 300.0:
        Finish == True
        winner = "Turtle 1"
    turtle2.forward(random.randint(1,25))
    t2pos = turtle2.position()
    if t2pos[1] >= 300.0:
        Finish == True
        winner = "Turtle 2"
    turtle3.forward(random.randint(1,25))
    t3pos = turtle3.position()
    if t3pos[1] >= 300.0:
        Finish == True
        winner = "Turtle 3"
    turtle4.forward(random.randint(1,25))
    t4pos = turtle4.position()
    if t4pos[1] >= 300.0:
        Finish == True
        winner = "Turtle 4"
    turtle5.forward(random.randint(1,25))
    t5pos = turtle5.position()
    if t5pos[1] >= 300.0:
        Finish == True
        winner = "Turtle 5"


Bob.done()
print(F"{winner} wins!")
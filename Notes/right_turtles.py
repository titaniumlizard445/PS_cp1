#PS 1st extra thing
import turtle
import random as r
turtle1 = turtle.Turtle()
choices = [1,2,3,4]

turtle1.color("black")
turtle1.speed(0)
for x in range(0,5000):
    for y in range(0,5):
        turtle1.forward(10)
        turtle1.right(r.choice(choices)*90)
    turtle1.forward(20)
turtle.done()
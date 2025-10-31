#PS 1st random thing

import turtle

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
width = 1
angle = 149
turtle1.speed(0)
turtle.bgcolor("black")
turtle.width(width)
turtle.shape("turtle")
turtle1.color("blue")
turtle2.color("white")
turtle2.speed(0)
for x in range(1,4000):
    turtle1.forward(x)
    turtle1.right(angle)
    turtle2.forward(x)
    turtle2.left(angle)
    turtle1.width(width)
    turtle2.width(width)
turtle.done()
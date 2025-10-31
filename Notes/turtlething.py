#PS 1st random thing

import turtle

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
width = 1
turtle1.speed(0)
turtle.bgcolor("black")
turtle.width(width)
turtle.shape("turtle")
turtle1.color("blue")
turtle2.color("white")
turtle2.speed(0)
for x in range(1,3000):
    turtle1.forward(x)
    turtle1.right(119)
    turtle2.forward(x)
    turtle2.left(119)
turtle.done()
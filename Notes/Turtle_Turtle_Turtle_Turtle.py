#PS 1st TURTLE

import turtle

colors = ["darkblue","lightblue","blue","navyblue","cyan","darkcyan"]
width = 10
turtle.color(colors[1])
turtle.speed(0)
turtle.bgcolor("black")
turtle.width(width)
turtle.shape("turtle")

for x in range(1,5000):
    turtle.backward(x/4)
    turtle.forward(x)
    turtle.right(89)
    turtle.pencolor(colors[x%6])
    width+=x
    width /= 10
    turtle.width(width)
turtle.done()

#PS 1st TURTLE

import turtle

blues = ["darkblue","lightblue","blue","navyblue","cyan","darkcyan"]
GreyScale = ["grey","black","white","darkgrey","lightgrey"]
width = 10
turtle.color(GreyScale[1])
turtle.speed(0)
turtle.bgcolor("red")
turtle.width(width)
turtle.shape("turtle")

for x in range(1,5000):
    #turtle.backward(x/4)
    turtle.forward(x)
    turtle.right(79)
    turtle.pencolor(GreyScale[x%5])
    width+=x
    width /= 10
    turtle.width(width)
turtle.done()

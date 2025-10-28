#PS 1st TURTLE

import turtle

colors = ["darkblue","red","lightblue","orange","blue","yellow"]
width = 10
turtle.color(colors[1])
turtle.speed(0)
turtle.bgcolor("black")
turtle.width(width)
turtle.shape("turtle")

for x in range(1,5000):
    turtle.forward(100)
    turtle.right(59)
    turtle.color(colors[x%6])
    width+=x
    width /= 10
    turtle.width(width)
turtle.done()

#PS 1st turtle starter

import turtle

def draw_branch(length):
    if length > 5:
        for i in range(3):
            turtle1.forward(length)
            draw_branch(length / 3)
            turtle1.backward(length)
            turtle1.right(60)

turtle1 = turtle.Turtle()
turtle1.speed(0)
turtle1.color("light blue")
turtle1.penup()
turtle1.goto(0,0)
turtle1.pendown()

for i in range(6):
    draw_branch(100)
    turtle1.right(60)

turtle1.hideturtle()
turtle.done()
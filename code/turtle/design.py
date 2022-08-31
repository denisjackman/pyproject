'''
    turtle design piece
'''
import turtle
# Creating turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("red")

ALPHA = 0
BETA = 0
t.speed(0)
t.penup()
t.goto(0, 200)
t.pendown()
while True:
    t.forward(ALPHA)
    t.right(BETA)
    ALPHA += 3
    BETA += 1
    if BETA == 210:
        break
    t.hideturtle()

turtle.done()

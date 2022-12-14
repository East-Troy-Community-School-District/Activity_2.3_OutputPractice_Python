'''
Frown
12/14/2022
Python I
'''

import turtle

t = turtle.Turtle()

# face outline
t.circle(100)

# left eye
t.penup()
t.goto(-40, 100)
t.pendown()
t.circle(20)

# right eye
t.penup()
t.goto(40, 100)
t.pendown()
t.circle(20)

# mouth
t.penup()
t.goto(50, 50)
t.pendown()
t.left(90)
t.circle(50, 180)
# this hides the turtle
t.hideturtle()
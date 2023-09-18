'''
Frown
Pawelski
9/17/2023
Introduction to Computer Science
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

turtle.mainloop()
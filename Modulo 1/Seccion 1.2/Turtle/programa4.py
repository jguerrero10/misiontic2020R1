import turtle
import math

t = turtle.Turtle()

def triangulo(Ca1, Ca2, col=None):
    hip = math.sqrt(Ca1 **2 + Ca2 **2)
    if col != None:
        t.color(col)
        t.begin_fill()
        t.forward(Ca1)
        t.left(315)
        t.forward(hip)
        t.right(315)
        t.forward(Ca2)
        t.end_fill()
    else:
        t.forward(Ca1)
        t.left(315)
        t.forward(hip)
        t.right(315)
        t.forward(Ca2)

t.penup()
t.forward(50)
t.pendown()
triangulo(10, 10)
t.penup()
t.back(50)
t.pendown()
triangulo(10, 10)
 

turtle.done()
turtle.getscreen()._root.mainloop()
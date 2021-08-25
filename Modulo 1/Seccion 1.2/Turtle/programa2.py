# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 17:14:27 2021

@author: Liceth Usma

"""
import turtle

t = turtle.Turtle()

def triangulo(La, c=None):
    if c != None:
        t.color(c)
        t.begin_fill()
        t.forward(La)
        t.left(120)
        t.forward(La)
        t.right(240)
        t.forward(La)
        t.end_fill()
    else:
        t.forward(La)
        t.left(120)
        t.forward(La)
        t.right(240)
        t.forward(La)



La = int(input("Digite el lado del triangulo: "))

opcion = input("Digite (C) si quiere color y (N) si no: ")

if opcion == "C":
    color1 = input( "Digite el numero de color en hexagesimal con # : " )
    triangulo(La, color1)
elif opcion == "N":
    t.penup()
    t.forward(20)
    t.pendown()     
    triangulo(La)
    t.penup()
    t.right(90)
    t.back(40)
    t.pendown()
    triangulo(La)
else:
    print("¡error! la opcion es incorrecta")

turtle.done()
turtle.getscreen()._root.mainloop()
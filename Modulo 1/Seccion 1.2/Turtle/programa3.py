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

Ca1 = int(input("Digite el cateto 1 del triangulo: "))
Ca2 = int(input("Digite el cateto 2 del triangulo: "))

opcion = input("Digite (C) si quiere color y (N) si no: ")

if opcion == "C":
    color1 = input( "Digite el numero de color en hexagesimal con # : " )
    triangulo(Ca1, Ca2, color1)
elif opcion == "N":
     triangulo(Ca1, Ca2,)

else:
    print("¡error! la opcion es incorrecta")

 

turtle.done()
turtle.getscreen()._root.mainloop()
import turtle

t = turtle.Turtle()

def cuadrado(l, color_relleno=None):
    if color_relleno != None:
        t.color(color_relleno)
        t.begin_fill()
        t.forward(l)
        t.left(90)
        t.forward(l)
        t.left(90)
        t.forward(l)
        t.left(90)
        t.forward(l)
        t.end_fill()
    else:
        t.forward(l)
        t.left(90)
        t.forward(l)
        t.left(90)
        t.forward(l)
        t.left(90)
        t.forward(l)
        
def trianguloEqui(lado, color_relleno=None):
    if color_relleno != None:
        t.color(color_relleno)
        t.begin_fill()
        t.forward(lado)
        t.left(90)
        t.forward(l)
        t.left(90)
        t.forward(l)
        t.left(90)
        t.forward(l)
        t.end_fill()
    else:
        t.forward(l)
        t.left(90)
        t.forward(l)
        t.left(90)
        t.forward(l)
        t.left(90)
        t.forward(l)

l = int(input("Digite el lado del cuadrado"))

relleno = input("Digite (S) quiere relleno y (N) si no quiere ")

if relleno == "S":
    color_hex = input("Digite el color en hexadecimal con su # ")
    cuadrado(l, color_hex)
elif relleno == "N":
    cuadrado(l)
else:
    print("La opcion no es valida")
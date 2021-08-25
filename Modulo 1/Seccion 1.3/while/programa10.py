def sumar(x, y):
   print(x + y)

def restar(x, y):
    print(x - y)

def multiplicar(x, y):
    print(x * y)

def solicitar():
    num1 = float(input("Digite el primer numero "))
    num2 = float(input("Digite el segundo numero "))
    return num1, num2

while True:
    opcion = input("Digite una opcion (s) Suma (r) Resta (m) Multiplicacion (q) Salir ")
    if opcion == "q":
        break
    elif opcion == "s":
        num1, num2 = solicitar()
        sumar(num1, num2)
    elif opcion == "r":
        num1, num2 = solicitar()
        restar(num1, num2)
    elif opcion == "m":
        num1, num2 = solicitar()
        multiplicar(num1, num2)
    else:
        print("Opcion no valida")

    

    


def sumar(x ,y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

while True:
    opcion = input("Digite una opcion (s) Sumar (r) Restar (m) Multiplicar (d) Dividir (q) Salir ")
    if opcion == "s":
        try:
            num1 = float(input("Digite el primer numero "))
            num2 = float(input("Digite el segundo numero "))
            resultado = sumar(num1, num2)
            print(f"La suma de {num1} + {num2} es {resultado}")
        except:
            print("Debe ingresar un valor numerico")
            continue        
    elif opcion == "r":
        try:
            num1 = float(input("Digite el primer numero "))
            num2 = float(input("Digite el segundo numero "))
            resultado = restar(num1, num2)
            print(f"La resta de {num1} - {num2} es {resultado}")
        except:
            print("Debe ingresar un valor numerico")
            continue 
    elif opcion == "m":
        try:
            num1 = float(input("Digite el primer numero "))
            num2 = float(input("Digite el segundo numero "))
            resultado = multiplicar(num1, num2)
            print(f"La resta de {num1} * {num2} es {resultado}")
        except:
            print("Debe ingresar un valor numerico")
            continue
    elif opcion == "d":
        try:
            num1 = float(input("Digite el primer numero "))
            num2 = float(input("Digite el segundo numero "))
            resultado = dividir(num1, num2)
            print(f"La resta de {num1} / {num2} es {resultado}")
        except:
            print("Debe ingresar un valor numerico")
            continue
    elif opcion == "q":
        break
    else:
        print("Digito una opcion no valida")
n = 1
suma = 0
while n <= 10:
    try:
        numero = int(input("Digite el numero "))
        suma += numero
        n += 1
    except:
        print("Debe ingresar un valor numerico")

promedio = suma/10

print(f"La suma de los numeros es {suma}")
print(f"El promedio de los numeros es {promedio}")
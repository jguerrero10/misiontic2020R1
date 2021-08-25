control = 1
suma = 0
while control <= 10:
    try:
        numero = int(input(f"Digite el numero {control} "))
        suma += numero
        print(suma)
        control += 1
    except:
        print("Ingreso un valor erroneo")

promedio = suma / 10

print(f"La suma de los numeros es {suma}")
print(f"El promedio es {promedio}")

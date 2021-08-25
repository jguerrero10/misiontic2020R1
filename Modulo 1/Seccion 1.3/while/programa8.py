pedirValor = 1
suma = 0
while pedirValor <= 10:
    try:
        numeros = int(input(f"Digite el numero {pedirValor}: "))
        suma += numeros
        pedirValor += 1
        print(suma)
    except:
        print("Ingrese algo bien bobo")

promedio = suma/10
print(promedio)
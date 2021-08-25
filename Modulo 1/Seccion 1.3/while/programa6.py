n = 1

try:
    numero = int(input("Digite un valor numerico positivo "))
    if numero > 0:
        while n <= numero:
            print(n)
            n += 1
    else:
        print("Este programa solo acepta valores numericos positivos")
except:
    print("Este programa solo permite valores numericos")
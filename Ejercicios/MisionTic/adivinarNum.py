import random

num_secreto = random.randint(1, 10)
intentos = 1

while intentos <= 4:
    try:
        numero = int(input("Digite el numero Entero "))
        if numero == num_secreto:
            print("Es Ganador")
            break
        else:
            if num_secreto < numero:
                print("El numero a adivinar es menor")
            else:
                print("El numero a adivinar es mayor")
    except:
        print("Debe Digitar un valor numerico")
    intentos += 1
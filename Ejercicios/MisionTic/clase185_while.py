import random

num_secreto = random.randint(1, 10)

intentos = 1
print("Programa juego de adivinar numero")
while intentos < 5:
    try:    
        numero = int(input("Diga un numero entre 1 y 10 "))
        if numero == num_secreto:
            print("Ganador....")
            break
        else:
            print("No es, intenete nuevamente")
            if num_secreto > numero:
                print("El numero advinar es mayor")
            else:
                print("El numero secreto es Menor")
                
    except:
        print("Debe digitar solo numeros enteros")
    intentos += 1
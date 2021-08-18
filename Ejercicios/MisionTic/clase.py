import random

num_secreto = random.randint(1, 50)
control = 1
while control < 5:
    try:
        numero = int(input())
    except:
        print("Error")
    
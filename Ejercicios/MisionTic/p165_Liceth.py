n= 0
try:
    numero = int(input("ingresar un numero"))
except:
    print("error!!! ")

while n < numero:
    n += 1
    print(n)
    if n == numero:        
        break
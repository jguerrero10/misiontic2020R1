""" 
Construye un programa que pregunte 
al usuario las longitudes de los tres 
lados de un triángulo y arroje un 
mensaje informando el área del triángulo

"""

base = float(input("Digite la base del triangulo "))
altura = float(input("Digite la altura del triangulo "))

area = (base * altura) / 2

print(f"El area del triangulo es {area}")
print("El area del triangulo es "+ str(area))
print("El area del triangulo es %s" %(area))
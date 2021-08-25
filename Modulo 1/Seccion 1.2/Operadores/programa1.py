""" 
Construye un programa que pregunte al usuario 
el radio de una circunferencia (r) y le 
muestre en pantalla un mensaje así: 
“Para una circunferencia con radio r, 
el perímetro es p y el área es a”. 

Las fórmulas para el cálculo del perímetro 
y el área de una circunferencia se presentan 
a continuación:

Perímetro = 2πr Área = π*r2

"""

r = float(input("Digite el radio de la circunferencia "))
pi = 3.1416

p = 2 * pi * r
a = pi * r ** 2

print(f"Para una circunferencia con radio {r}, el perímetro es {p} y el área es {a}")
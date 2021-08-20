"""

Escriba un programa en Python para crear un diccionario a partir de una cadena.

Nota: Realice un seguimiento del recuento de letras de la cadena.

Cadena de muestra: 'w3resource'

Salida esperada: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1} 

autor: Liceth Usma
"""

diccionario = {
}

cadena = input("Escriba un texto: ")

for i in cadena:
   t = cadena.count(i)
   diccionario[i]= t

print(diccionario)
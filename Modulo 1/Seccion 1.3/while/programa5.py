""" 
Un profresor necesita agregar las notas de un grupo de estudiantes

sacar el promedio y la suma de las notas

"""

""" 
Tengo 10 notas de las cuales necesito sacar el promedio, la suma y la nota mayor
"""
suma = 0
contar = 0
while True:
    nota = input("Digite la nota ")
    if nota == "q":
        break
    else:
       
        nota = float(nota)
        suma += nota
        contar += 1
       

promedio = suma / contar   

print(f"Promedio: {promedio}")
print(f"Suma: {suma}")




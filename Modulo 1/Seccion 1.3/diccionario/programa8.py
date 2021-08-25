""" 
Diseñar una funcion que tenga como argumento un diccionario
que su claves serian los numeros de identificacion de unos estudiantes,
y los valores serian la informacion personal de dichos estudiantes.

La funcion retornara otro diccionario que contenga, el nombre del estudiante con su apellido
y en mayusculas, el promedio de nota, si el estudiante esta matriculado, si aprueba o no, si el promedio
de notas es mayor o igual a 7 entonces aprobo.

{
    1102876223: {
        "nombre": "LUISA FERNANDA GUTIERREZ LOPEZ",
        "promedio": 7.36,
        "matriculado": "SI",
        "aprobado": "SI" 
    }
}
"""

estudiantes = {
   1102876223 : {
    "nombres": "Luisa Fernanda",
    "apellidos": "Gutierrez Lopez",
    "edad": 17,
    "notas": [6.7, 8.0, 9.0, 5.0, 8.1],
    "matricula": True,
    "curso": 11
    },
    1105678234 : {
    "nombres": "Jose Miguel",
    "apellidos": "Diaz Miranda",
    "edad": 16,
    "notas": [7.0, 8.0, 10.0, 8.0, 9.1],
    "matricula": True,
    "curso": 11
    },
    114567789 : {
    "nombres": "Marcela",
    "apellidos": "Garcia Sanchez",
    "edad": 15,
    "notas": [9.0, 8.0, 10.0, 9.0, 8.1],
    "matricula": True,
    "curso": 11
    }  
}


for estudiante in estudiantes:
    notas = estudiantes[estudiante]["notas"]
    print(notas)

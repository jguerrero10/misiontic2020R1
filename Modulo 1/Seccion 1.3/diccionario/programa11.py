""" 
Se necesita crear una función que permita
con la estructura dada, generar un diccionario clave el numero identidad del estudiante
nombres con apellido, promedio y especificar si el estudiante esta matriculado o no

"""

estudiantes = {
    104678234: {
        "nombres": "Julio Cesar",
        "apellidos": "mora diaz",
        "notas": [3.6, 4.1, 5.0, 4.7, 3.8],
        "edad": 16,
        "matriculado": True
    },
    1102834677: {
        "nombres": "jose",
        "apellidos": "mendez sanchez",
        "notas": [3.1, 3.9, 2.6, 3.7, 4.0],
        "edad": 17,
        "matriculado": True
    },
    1014355678: {
        "nombres": "Luisa",
        "apellidos": "diaz garcia",
        "notas": [4.5, 4.9, 3.1, 3.7, 4.3],
        "edad": 16,
        "matriculado": False
    }

}


""" 
Salida:

<3.0 Reprobado
{
    identidad: {
        nombres: "JULIO CESAR MORA DIAZ"
        promedio: 4.24,
        matriculado: "Si",
        aprobado: "Si"
    }
}
"""


def promedio_nota(est):
    prom = dict()
    for estudiante in est:
        notas = est[estudiante]["notas"]
        nombre = est[estudiante]["nombres"].upper() +" " + est[estudiante]["apellidos"].upper()                    
        promedio = sum(notas) / len(notas)

        if est[estudiante]["matriculado"]:
            matricula = "Si"
        else:
            matricula = "No"

        if promedio >= 3.0:
            aprobado = "Si"
        else:
            aprobado = "No"

        prom[estudiante]={
            'nombres': nombre,
            'promedio': promedio,
            'matriculado': matricula,
            'aprobado': aprobado
        }
    
    return prom
         
print(promedio_nota(estudiantes))

""" 
Se necesita crear una función que permita
con la estructura dada, generar un diccionario clave el numero identidad del estudiante
nombres con apellido, promedio y especificar si el estudiante esta matriculado o no

Curso 96 - Fernando Reyes

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
        aprobado. "Si"
    }
}
"""
# diccionario[key]
"""for estudiante in estudiantes:
    notas = estudiantes[estudiante]["notas"]
    suma = 0
    for nota in notas:
        suma += nota
    promedio = suma/len(notas)
    suma = 0
    print(promedio)
"""
def promedios(dic):
    est_salida = dict()
    for estudiante in dic:
        upperNombres = dic[estudiante]["nombres"].upper()
        upperApellidos = dic[estudiante]["apellidos"].upper()
        suma = sum(dic[estudiante]["notas"]) 
        promedio = suma/len("notas")
        nombresConcatenados = f"{upperNombres} {upperApellidos}"
        estadoMatricula = dic[estudiante]["matriculado"]        
        if estadoMatricula == False:
            matr = "NO"
        else:
            matr = "SI"
        if promedio >= 3.0:
            apr = "SI"
        else:
            apr = "NO"
        est_salida[estudiante] = {
            "nombres": nombresConcatenados,
            "promedio": promedio,
            "matriculado": matr,
            "aprobado": apr
            } 
    return est_salida

resultados = promedios(estudiantes)

print(resultados)
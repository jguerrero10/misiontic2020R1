"""
Haga una funcion que teniendo estructura tal, obtenga el promedio de notas del estudiante
el retorno seria una lista, donde muestre el nombre y apellidos en mayuscula, nota promedio
matriculado o no matriculado 

"""

estudiantes = {}

estudiantes[101442356] = {
    "nombres": "luis carlos",
    "apellidos": "suares montoya",
    "notas": [4.5, 3.6, 5.0, 3.2],
    "matriculado": True
}
estudiantes[103456782] = {
    "nombres": "jose",
    "apellidos": "perez diaz",
    "notas": [4.7, 3.0, 4.0, 3.2],
    "matriculado": True
}

def estado_est(dic):    
    suma = 0    
    for estudiante in estudiantes:
        nombre = estudiantes[estudiante]["nombres" ]
        apellido = estudiantes[estudiante]["apellidos"]
        nombre = nombre.upper()
        apellido = apellido.upper()

        notas = estudiantes[estudiante]['notas']
        for nota in notas:
            suma += nota
        promedio = suma / len(notas)
        suma = 0
        if estudiantes[estudiante]['matriculado']:
            matricula = "Matriculado"
        else:
            matricula = "No matriculado"
        datos = f"{nombre} {apellido}, {promedio}, {matricula}"
        datos = list(datos.split(","))
        print(datos)        
        


estado_est(estudiantes)
    
 


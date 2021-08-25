estudiantes = {

}

def create(key, valor):
    estudiantes[key] = valor
    return f"el valor {valor} se agrego correctamente"

def read(key):    
    return f"{key} --> {estudiantes[key]}"

def update(key, valor):
    estudiantes[key] = valor
    return f"el valor {valor} se actualizo correctamente"

def delete(key):
   estudiantes.pop(key)

create("Joel Guerrero", 1203466522) 

print(estudiantes)

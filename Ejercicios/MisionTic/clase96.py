claves = {
    'm': 0,
    'u': 1,
    'r': 2,
    'c': 3,
    'i': 4,
    'e': 5,
    'l': 6,
    'a': 7,
    'g': 8,
    'o': 9
}

def encriptar(cadena):
    sub = cadena.lower()    
    for key in claves:
        mensaje = sub.replace(key,str(claves[key]))
        sub = mensaje        
    return sub

def desencriptar(cadena):
    for key in claves:
        mensaje = cadena.replace(str(claves[key]), key)
        cadena = mensaje
    return cadena

entrada = input("Digite el mensaje a encriptar ")
mensaje_encriptado = encriptar(entrada)
mensaje = desencriptar(mensaje_encriptado)

print(mensaje_encriptado)
print(mensaje)
informacion = {
    'Cierra Vega': [6.2, 70], 
    'Alden Cantrell':  [5.9, 65], 
    'Kierra Gentry': [6.0, 68], 
    'Pierre Cox': [5.8, 66 ]
}

def mostar_altura_peso(datos):
    necesidad = input("Si desea ver todos los valores presione s; si es uno en especifico presione n: ")
    print(necesidad)

    if necesidad == "s" or necesidad == "S": 
        print(datos)
        print("Fin del programa")
        print(necesidad)
        
    else:
        print(necesidad)
        print("El programa continua") 
        nombre = input("ingrese el nombre para mostrar sus datos: ")

        if nombre in datos:   
            altura = datos[nombre][0]*0.3048
            peso = datos[nombre][1]/2.205
            print(datos)
    
        return f"Su altura es: {altura} metros, y su peso es de {peso} kilos"

print(mostar_altura_peso(informacion))   
""" 
Se desea calcular la distancia 
recorrida (m) por un móvil 
que tiene velocidad constante (m/s) 
durante un tiempo t (s), considerar 
que es un MRU (Movimiento Rectilíneo Uniforme).

"""

v = float(input("Digite la velocidad m/s "))
t = float(input("Digite el tiempo (s) de duracion del recorrido "))

distancia = v * t

print(f"La distancia recorrida es {distancia}")
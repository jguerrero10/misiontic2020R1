from django.db import models
from django.contrib.auth.models import User


opciones_prestamo = [
    ('P', 'Prestado'),
    ('E', 'Entregado'),
    ('Pe', 'Perdido')
] 

opcion = [
    ('F', 'Femenino'),
    ('M', 'Masculino')
]

class Libro(models.Model):
    serial = models.CharField(max_length=10, default="N/A")
    titulo = models.CharField(max_length=80)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=40)
    editorial = models.CharField(max_length=60, default="N/A")
    pag = models.PositiveIntegerField()
    precio = models.FloatField()    
    notas = models.TextField(max_length=500, default='N/A', blank=True)


class Persona(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)             
    nombre = models.CharField(max_length=80)    
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=12)
    correo = models.EmailField(max_length=25)
    sexo = models.CharField(max_length=2, choices=opcion, default='M')

class Prestamo(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fprestamo = models.DateTimeField()
    fentrega = models.DateTimeField(null=True)
    estado = models.CharField(max_length=2, choices=opciones_prestamo)












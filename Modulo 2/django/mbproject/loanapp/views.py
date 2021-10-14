from django.shortcuts import render
from django.http import HttpResponse
from loanapp.models import *

def home(request):
    contexto = dict()
    libros = Libro.objects.all()
    for libro in libros:
       libro.precio = round(libro.precio)
    contexto['libros'] = libros 
    print(contexto)   
    return render(request, 'index.html', contexto)

def agregar_libro(request):
    return render(request, 'agregar_libro.html')



    

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from loanapp.models import *

def home(request):
    contexto = dict()
    libros = Libro.objects.all()
    for libro in libros:
        libro.precio = round(libro.precio)
    contexto['libros'] = libros      
    return render(request, 'index.html', contexto)

def agregar_libro(request):
    if request.method == 'POST':
        serial = request.POST['serial']
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        genero = request.POST['genero']
        editorial = request.POST['editorial']
        pag = request.POST['pag']
        precio = request.POST['precio']
        notas = request.POST['notas']
        try:
            libro = Libro.objects.create(serial=serial, titulo=titulo, autor=autor, genero=genero, editorial=editorial, pag=pag, precio=precio, notas=notas)
            estado = True
            contexto = {
                'estado': estado,
                'libro': libro
                }
        except:
            estado = False
            contexto = {
                'estado': estado,
                'titulo': titulo
                }
        return render(request, 'respuesta.html', contexto)        
    else:    
        return render(request, 'agregar_libro.html')

def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == 'POST':
        serial = request.POST['serial']
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        genero = request.POST['genero']
        editorial = request.POST['editorial']
        pag = request.POST['pag']
        precio = request.POST['precio']
        notas = request.POST['notas']
        libro.serial = serial
        libro.titulo = titulo
        libro.autor = autor
        libro.genero = genero
        libro.editorial = editorial
        libro.pag = pag
        libro.precio = precio
        libro.notas = notas
        try:
            libro.save()
            estado = True
            contexto = {
                'estado': estado,
                'libro': libro
                }
        except:
            estado = False
            contexto = {
                'estado': estado,
                'titulo': titulo
                }
        return render(request, 'respuesta.html', contexto) 
    else:                        
        return render(request, 'editar_libro.html', {'libro': libro})
    


    

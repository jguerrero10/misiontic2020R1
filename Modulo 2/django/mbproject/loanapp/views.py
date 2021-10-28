from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from django.urls import reverse
from loanapp.models import *
from loanapp.forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    contexto = dict()
    libros = Libro.objects.all()
    for libro in libros:
        libro.precio = round(libro.precio)
    contexto['libros'] = libros      
    return render(request, 'index.html', contexto)

@login_required(login_url='/usuario/login/')
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
        except ValueError as e:
            estado = False
            contexto = {
                'estado': estado,
                'titulo': titulo,
                'error': e
                }
        return render(request, 'respuesta.html', contexto)        
    else:    
        return render(request, 'agregar_libro.html')

@login_required(login_url='/usuario/login/')
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

@login_required(login_url='/usuario/login/')
def eliminar_libro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect(reverse('inicio'))

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            correo = form.cleaned_data['correo']
            password = form.cleaned_data['password']
            password_verificar = form.cleaned_data['password_verificar']
            if password == password_verificar:
                User.objects.create_user(usuario, correo, password)
                messages.success(request, 'Usuario creado correctamente.')
                return redirect(reverse('registrar_usuario'))
            else:
                messages.warning(request, 'Contraseña no coincide')
                return redirect(reverse('registrar_usuario'))            
        else:
            messages.warning(request, 'Datos no validos')
            return redirect(reverse('registrar_usuario')) 
    else:      
        contexto = dict()
        contexto['UsuarioForm'] = UsuarioForm()
        return render(request, 'registrar_usuario.html', contexto)

def login_(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('inicio'))
            else:
                messages.warning(request, 'El usuario y/o contraseña es incorrecto')
                return redirect(reverse('login_user'))
        else:
            messages.warning(request, 'Error al leer los datos enviados')
            return redirect(reverse('login_user'))            
    else:
        contexto = dict()
        contexto['formLogin'] = LoginForm()
        return render(request, 'login_usuario.html', contexto)
        
@login_required(login_url='/usuario/login/')
def logout_(request):
    logout(request)
    return redirect(reverse('inicio'))




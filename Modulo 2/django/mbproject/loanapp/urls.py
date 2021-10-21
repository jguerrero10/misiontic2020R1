from django.urls import path
from loanapp.views import *

urlpatterns  = [
    path('agregar/', agregar_libro, name='agregar_libro'),
    path('editar/<int:id>', editar_libro, name='editar_libro'),    
]
from django.urls import path
from loanapp.views import *

urlpatterns  = [
    path('libro/agregar/', agregar_libro, name='agregar_libro'),
    path('libro/editar/<int:id>', editar_libro, name='editar_libro'),
    path('libro/eliminar/<int:id>', eliminar_libro, name='eliminar_libro'),     
]
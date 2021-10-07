from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def fecha(request):
    ahora = datetime.now()
    return HttpResponse(f"La hora es {ahora}")

def calculos(request, year, year2):
    cant = year2 - year
    return HttpResponse(f"La cantidad de años de {year2} a {year} es {cant}")

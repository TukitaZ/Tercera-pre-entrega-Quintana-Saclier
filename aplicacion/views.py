from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'aplicacion/home.html')

def materias(request):
    contexto = {'materias': Materia.objects.all()}
    return render(request, 'aplicacion/materias.html', contexto)

def maestros(request):
    contexto = {'maestros': Maestro.objects.all()}
    return render(request, 'aplicacion/maestros.html', contexto)

def alumnos(request):
    contexto = {'alumnos': Alumno.objects.all()}
    return render(request, 'aplicacion/alumnos.html', contexto)
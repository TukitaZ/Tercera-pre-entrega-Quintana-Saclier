from django.shortcuts import render
from .models import Materia

# Create your views here.
def home(request):
    return render(request, 'aplicacion/home.html')

def materias(request):
    contexto = {'materias': Materia.objects.all()}
    return render(request, 'aplicacion/materias.html', contexto)

def maestros(request):
    return render(request, 'aplicacion/maestros.html')

def alumnos(request):
    return render(request, 'aplicacion/alumnos.html')
from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import *

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

def FormMateria(request):
    if request.method == "POST":
        miForm = FormM(request.POST)
        if miForm.is_valid():
            materia_nombre = miForm.cleaned_data.get('nombre')
            materia_comision = miForm.cleaned_data.get('comision')
            materia = Materia(nombre=materia_nombre,
                          comision=materia_comision)
            materia.save()
            return render(request, 'aplicacion/home.html')
    else:
        miForm = FormM()

    return render(request, 'aplicacion/FormMateria.html', {"form": miForm})

def FormMaestro(request):
    if request.method == "POST":
        miForm = FormT(request.POST)
        if miForm.is_valid():
            maestro_nombre = miForm.cleaned_data.get('nombre')
            maestro_apellido = miForm.cleaned_data.get('apellido')
            maestro_documento = miForm.cleaned_data.get('documento')
            maestro_email= miForm.cleaned_data.get('email')
            maestro_profesion = miForm.cleaned_data.get('profesion')
            maestro = Maestro(nombre=maestro_nombre, apellido=maestro_apellido, documento=maestro_documento, email=maestro_email,)
            maestro.save()
            maestro.profesion.set(maestro_profesion)
            return render(request, 'aplicacion/home.html')
    else:
        miForm = FormT()

    return render(request, 'aplicacion/FormMaestro.html', {"form": miForm})

def FormAlumno(request):
    if request.method == "POST":
        miForm = FormA(request.POST)
        if miForm.is_valid():
            alumno_nombre = miForm.cleaned_data.get('nombre')
            alumno_apellido = miForm.cleaned_data.get('apellido')
            alumno_documento = miForm.cleaned_data.get('documento')
            alumno_email = miForm.cleaned_data.get('email')
            alumno_comision = miForm.cleaned_data.get('comision')
            alumno = Alumno(nombre=alumno_nombre, apellido=alumno_apellido, documento=alumno_documento, email=alumno_email,)
            alumno.save()
            alumno.comision.set(alumno_comision)
            return render(request, 'aplicacion/home.html')
    else:
        miForm = FormA()

    return render(request, 'aplicacion/FormAlumno.html', {"form": miForm})

def BuscarMaestro(request):
    return render(request, 'aplicacion/BuscarMaestro.html')

def buscar3(request):
    if request.GET.get('buscar'):
        patron = request.GET.get('buscar')
        alumnos = Alumno.objects.filter(nombre__icontains=patron)
        contexto = {'alumnos': alumnos, 'titulo': f'Alumnos que tienen como patron, "{patron}"'}
        return render(request, 'aplicacion/alumnos.html', contexto)
    return HttpResponse('No se ingreso nada a buscar')

def BuscarMateria(request):
    return render(request, 'aplicacion/BuscarMateria.html')

def buscar2(request):
    if request.GET.get('buscar'):
        patron = request.GET.get('buscar')
        materias = Materia.objects.filter(nombre__icontains=patron)
        contexto = {'materias': materias, 'titulo': f'Materias que tienen como patron, "{patron}"'}
        return render(request, 'aplicacion/materias.html', contexto)
    return HttpResponse('No se ingreso nada a buscar')

def BuscarAlumno(request):
    return render(request, 'aplicacion/BuscarAlumno.html')

def buscar1(request):
    if request.GET.get('buscar'):
        patron = request.GET.get('buscar')
        maestros = Maestro.objects.filter(nombre__icontains=patron)
        contexto = {'maestros': maestros, 'titulo': f'Alumnos que tienen como patron, "{patron}"'}
        return render(request, 'aplicacion/maestros.html', contexto)
    return HttpResponse('No se ingreso nada a buscar')
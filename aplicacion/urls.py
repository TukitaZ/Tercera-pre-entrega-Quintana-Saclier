from django.urls import path, include
from .views import *
from . import views
urlpatterns = [
    path('', home, name='home'),
    path('materias/', materias, name='materias'),
    path('maestros/', maestros, name='maestros'),
    path('alumnos/', alumnos, name='alumnos'),

    path('FormMateria/', FormMateria, name='FormMateria'),
    path('FormMaestro/', FormMaestro, name='FormMaestro'),
    path('FormAlumno/', FormAlumno, name='FormAlumno'),

    path('buscar_maestro/', BuscarMaestro, name="buscar_maestro"),
    path('buscar1/', views.buscar1, name="buscar1"),

    path('buscar_materia/', views.BuscarMateria, name="buscar_materia"),
    path('buscar2/', views.buscar2, name="buscar2"),

    path('buscar_alumno/', BuscarAlumno, name="buscar_alumno"),
    path('buscar3/', views.buscar3, name="buscar3"),
]
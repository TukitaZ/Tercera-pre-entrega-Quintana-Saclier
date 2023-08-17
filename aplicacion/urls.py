from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('materias/', materias, name='materias'),
    path('maestros/', maestros, name='maestros'),
    path('alumnos/', alumnos, name='alumnos'),
]
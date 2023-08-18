from django.db import models

# Create your models here.
class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

    def __str__(self):
        return f'{self.nombre}'
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.IntegerField()
    email = models.EmailField()
    comision = models.ManyToManyField(Materia)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Maestro(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.IntegerField()
    email = models.EmailField()
    profesion = models.ManyToManyField(Materia)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
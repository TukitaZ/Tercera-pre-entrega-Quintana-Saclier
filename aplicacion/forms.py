from django import forms
from .models import *
from .forms import *

class FormM(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    comision = forms.IntegerField(required=True)

class FormT(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    documento = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    profesion = forms.ModelMultipleChoiceField(queryset=Materia.objects.all(), required=True)  

class FormA(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(required=True)
    documento = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    comision = forms.ModelMultipleChoiceField(queryset=Materia.objects.all(), required=True)   
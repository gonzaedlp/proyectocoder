from socket import fromshare
from django import forms

class Formulario_personal(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    puesto = forms.CharField(max_length=40)


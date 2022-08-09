from socket import fromshare
from django import forms

class Formulario_articles(forms.Form):
    titulo=forms.CharField(max_length=40)
    descripcion=forms.CharField(max_length=500)
    autor=forms.CharField(max_length=50)


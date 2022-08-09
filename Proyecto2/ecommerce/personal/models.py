from django.db import models

class Personal(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    puesto = models.CharField(max_length=40)

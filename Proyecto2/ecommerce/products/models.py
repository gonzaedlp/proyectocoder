from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    creation_date = models.DateField(auto_now_add=True, blank=True, null=True)

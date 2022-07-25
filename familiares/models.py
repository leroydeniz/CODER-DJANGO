from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length=100)
    tel = models.IntegerField(default="", null=True, blank=True)
    peso = models.FloatField(default=60)
    registro = models.DateField(auto_now_add=True, null=True, blank=True)
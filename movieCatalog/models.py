from email.charset import Charset
from inspect import modulesbyfile
from django.db import models

# Create your models here.
class Directores(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre + " " + self.apellido

class Generos(models.Model):
    genero = models.CharField(max_length=30)

    def __str__(self):
        return self.genero

class Peliculas(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.ManyToManyField(Generos, null=True)
    director = models.ForeignKey(Directores, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField(default=2000)

    def __str__(self):
        return self.titulo + ' - ' + self.director.__str__()

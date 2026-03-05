from django.db import models

from django.db import models

class Heroe(models.Model):
    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Villano(models.Model):
    nombre = models.CharField(max_length=100)
    enemigo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Comic(models.Model):
    titulo = models.CharField(max_length=100)
    heroe = models.CharField(max_length=100)
    anio = models.IntegerField()

    def __str__(self):
        return self.titulo

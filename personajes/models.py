from django.db import models
from vehiculos.models import Vehiculo
from naves.models import Nave

class Personaje(models.Model):
    nombre = models.CharField(max_length=50)
    anio_nacimiento = models.CharField(max_length=15, verbose_name="año de nacimiento")
    genero = models.CharField(max_length=10, verbose_name="género")
    planeta_nacimiento = models.CharField(max_length=50, verbose_name="planeta de nacimiento")
    naves = models.ManyToManyField(Nave, db_table="Personaje_nave")
    vehiculos = models.ManyToManyField(Vehiculo, db_table="Personaje_vehiculo")

    class Meta:
        db_table = 'Personaje'
        verbose_name = "personaje"
        verbose_name_plural = "personajes"

    def __str__(self):
        return self.nombre
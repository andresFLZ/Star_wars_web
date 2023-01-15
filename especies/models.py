from django.db import models

from personajes.models import Personaje

class Especie(models.Model):
    nombre = models.CharField(max_length=30)
    clasificacion = models.CharField(max_length=50, verbose_name="clasificación")
    designacion = models.CharField(max_length=50, verbose_name="designación")
    lenguaje = models.CharField(max_length=50)
    planeta_origen = models.CharField(max_length=50, verbose_name="Planeta de origen")
    personajes = models.ManyToManyField(Personaje, db_table="Personaje_especie")

    class Meta:
        db_table = 'Especie'
        verbose_name = "especie"
        verbose_name_plural = "especies"

    def __str__(self):
        return self.nombre
from django.db import models
from personajes.models import Personaje
from vehiculos.models import Vehiculo
from naves.models import Nave
from especies.models import Especie
from planetas.models import Planeta

class Pelicula(models.Model):
    titulo = models.CharField(max_length=30)
    episodio = models.CharField(max_length=2)
    director = models.CharField(max_length=50)
    fecha_lanzamiento = models.DateField(verbose_name = "fecha de lanzamiento")
    planetas = models.ManyToManyField(Planeta, db_table="Pelicula_planeta")
    especies = models.ManyToManyField(Especie, db_table="Pelicula_especie")
    naves = models.ManyToManyField(Nave, db_table="Pelicula_nave")
    vehiculos = models.ManyToManyField(Vehiculo, db_table="Pelicula_vehiculo")
    personajes = models.ManyToManyField(Personaje, db_table="Pelicula_personaje")

    class Meta:
        db_table = 'Pelicula'
        verbose_name = "pelicula"
        verbose_name_plural = "peliculas"

    def __str__(self):
        return self.titulo

    def devolverPersonajes(self):
        pelicula = Pelicula.objects.get(titulo=self.titulo)
        personajes = pelicula.personajes.all()
        return personajes
from django.db import models

class Vehiculo(models.Model):
    nombre = models.CharField(max_length=30)
    modelo = models.CharField(max_length=50)
    clase = models.CharField(max_length=50)
    costo = models.IntegerField()
    velocidad_max = models.IntegerField(verbose_name="velocidad maxima")

    class Meta:
        db_table = 'Vehiculo'
        verbose_name = "vehiculo"
        verbose_name_plural = "vehiculos"

    def __str__(self):
        return self.nombre
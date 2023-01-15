from django.db import models

class Nave(models.Model):
    nombre = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30, verbose_name="clasificación")
    clase = models.CharField(max_length=30, verbose_name="designación")
    costo = models.IntegerField()
    velocidad_max = models.IntegerField(verbose_name="velocidad maxima")

    class Meta:
        db_table = 'Nave'
        verbose_name = "nave"
        verbose_name_plural = "naves"

    def __str__(self):
        return self.nombre
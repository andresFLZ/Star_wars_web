from django.db import models

class Planeta(models.Model):
    nombre = models.CharField(max_length=30)
    diametro = models.IntegerField()
    periodo_rotacion = models.IntegerField(verbose_name="periodo de rotación")
    periodo_orbitacion = models.IntegerField(verbose_name="periodo de orbitación")
    gravedad = models.CharField(max_length=50)
    poblacion = models.IntegerField(verbose_name="población")

    class Meta:
        db_table = 'Planeta'
        verbose_name = "planeta"
        verbose_name_plural = "planetas"

    def __str__(self):
        return self.nombre
from django.db import models

# Create your models here.
class Ubicacion(models.Model):
    idubicacion = models.AutoField(primary_key=True)
    direccion = models.CharField(blank=True, null=True)
    distrito = models.CharField(blank=True, null=True)
    region = models.CharField(blank=True, null=True)
    longitud = models.IntegerField(blank=True, null=True)
    latitud = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ubicacion'
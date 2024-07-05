from django.db import models
from Almacenes.models import Almacen

# Create your models here.
class Ruta(models.Model):
    idruta = models.AutoField(primary_key=True)
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen', blank=True, null=True)
    transporte = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ruta'
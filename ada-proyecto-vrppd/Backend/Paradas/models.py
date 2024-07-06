from django.db import models
from Rutas.models import Ruta
from Ubicaciones.models import Ubicacion

# Create your models here.
class Parada(models.Model):
    idparada = models.AutoField(primary_key=True)
    idruta = models.ForeignKey(Ruta, models.DO_NOTHING, db_column='idruta', blank=True, null=True)
    idubicacion = models.ForeignKey(Ubicacion, models.DO_NOTHING, db_column='idubicacion', blank=True, null=True)
    tipo = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parada'
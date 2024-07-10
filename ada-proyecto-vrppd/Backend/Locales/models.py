from django.db import models
from Empresarios.models import Empresario
from Productos.models import Producto
from Ubicaciones.models import Ubicacion

# Create your models here.
class Local(models.Model):
    idlocal = models.AutoField(primary_key=True)
    idempresario = models.ForeignKey(Empresario, models.DO_NOTHING, db_column='idempresario')
    idubicacion = models.ForeignKey(Ubicacion, models.DO_NOTHING, db_column='idubicacion')
    tipo = models.CharField(blank=True, null=True)
    nombre = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local'


class Localproducto(models.Model):
    idlocalproducto = models.AutoField(primary_key=True)
    idlocal = models.ForeignKey(Local, models.DO_NOTHING, db_column='idlocal', blank=True, null=True)
    idproducto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localproducto'
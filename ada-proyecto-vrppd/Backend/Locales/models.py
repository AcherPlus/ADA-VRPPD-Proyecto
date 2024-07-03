from django.db import models
from Empresarios.models import Empresario
from Productos.models import Producto

# Create your models here.
class Local(models.Model):
    idlocal = models.AutoField(primary_key=True)
    ubicacion = models.CharField()
    nombre = models.CharField()
    idempresaio = models.ForeignKey(Empresario, models.DO_NOTHING, db_column='idempresaio')

    class Meta:
        managed = False
        db_table = 'local'


class Localproducto(models.Model):
    idlocalprod = models.AutoField(primary_key=True)
    idlocal = models.ForeignKey(Local, models.DO_NOTHING, db_column='idlocal')
    idproducto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='idproducto')

    class Meta:
        managed = False
        db_table = 'localproducto'
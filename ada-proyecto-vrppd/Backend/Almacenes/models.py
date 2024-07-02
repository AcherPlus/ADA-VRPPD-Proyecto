from django.db import models
from Productos.models import Producto
from Proveedores.models import Proveedor
from Transportes.models import Transporte

# Create your models here.
class Almacen(models.Model):
    ubicacion = models.CharField()
    idproveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='idproveedor', blank=True, null=True)
    idalmacen = models.IntegerField(primary_key=True)
    idtransporte = models.ForeignKey(Transporte, models.DO_NOTHING, db_column='idtransporte', blank=True, null=True)
    idproducto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    cantidadprod = models.IntegerField()
    cantidadtransp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'almacen'
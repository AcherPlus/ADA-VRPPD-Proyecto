from django.db import models
from Productos.models import Producto
from Proveedores.models import Proveedor
from Transportes.models import Transporte

# Create your models here.
class Almacen(models.Model):
    idalmacen = models.AutoField(primary_key=True)
    idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='idproveedor', blank=True, null=True)
    idubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='idubicacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'almacen'
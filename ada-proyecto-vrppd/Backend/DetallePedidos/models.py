from django.db import models
from Pedidos.models import Pedido
from Locales.models import Local
from Productos.models import Producto

# Create your models here.
class Detallepedido(models.Model):
    iddetallepedido = models.AutoField(primary_key=True)
    idpedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='idpedido', blank=True, null=True)
    idlocalrecojo = models.ForeignKey(Local, models.DO_NOTHING, db_column='idlocalrecojo', blank=True, null=True)
    idlocalentrega = models.ForeignKey(Local, models.DO_NOTHING, db_column='idlocalentrega', related_name='detallepedido_idlocalentrega_set', blank=True, null=True)
    idproducto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detallepedido'
from django.db import models
from Empresarios.models import Empresario

# Create your models here.
class Pedido(models.Model):
    idpedido = models.AutoField(primary_key=True)
    idempresario = models.ForeignKey(Empresario, models.DO_NOTHING, db_column='idempresario', blank=True, null=True)
    estado = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido'
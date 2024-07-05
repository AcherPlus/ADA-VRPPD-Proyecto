from django.db import models
from Usuarios.models import Usuario

# Create your models here.
class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'
from django.db import models
from Usuarios.models import Usuario

# Create your models here.
class Empresario(models.Model):
    idempresario = models.AutoField(primary_key=True)
    nombres = models.CharField(blank=True, null=True)
    apellidos = models.CharField(blank=True, null=True)
    correo = models.CharField(blank=True, null=True)
    idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='idusuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresario'
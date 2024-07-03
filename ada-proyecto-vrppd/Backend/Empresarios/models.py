from django.db import models
from Usuarios.models import Usuario

# Create your models here.
class Empresario(models.Model):
    idempresario = models.AutoField(primary_key=True)
    nombres = models.CharField()
    apellidos = models.CharField()
    correo = models.CharField()
    ruc = models.IntegerField()
    idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='idusuario')

    class Meta:
        managed = False
        db_table = 'empresario'
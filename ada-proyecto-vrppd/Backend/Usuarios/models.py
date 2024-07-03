from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre_usuario = models.CharField()
    contrasenia = models.CharField()
    idusuario = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'usuario'
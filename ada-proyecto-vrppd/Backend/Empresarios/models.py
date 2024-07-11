from django.db import models

# Create your models here.
class Empresario(models.Model):
    idempresario = models.AutoField(primary_key=True)
    nombres = models.CharField(blank=True, null=True)
    apellidos = models.CharField(blank=True, null=True)
    correo = models.CharField(blank=True, null=True)
    nombre_usuario_emp = models.CharField(blank=True, null=True)
    password_emp = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresario'
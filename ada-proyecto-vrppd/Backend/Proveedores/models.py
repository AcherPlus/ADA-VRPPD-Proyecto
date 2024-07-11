from django.db import models

# Create your models here.
class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    nombre_usuario_prov = models.CharField(blank=True, null=True)
    password_prov = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'
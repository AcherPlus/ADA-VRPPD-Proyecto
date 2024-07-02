from django.db import models

# Create your models here.
class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField()

    class Meta:
        managed = False
        db_table = 'producto'
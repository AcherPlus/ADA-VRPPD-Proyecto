from django.db import models

# Create your models here.
class Transporte(models.Model):
    idtransporte = models.AutoField(primary_key=True)
    disponibilidad = models.CharField()

    class Meta:
        managed = False
        db_table = 'transporte'
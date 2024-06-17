# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Almacen(models.Model):
    ubicacion = models.CharField()
    idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='idproveedor', blank=True, null=True)
    idalmacen = models.IntegerField(primary_key=True)
    idtransporte = models.ForeignKey('Transporte', models.DO_NOTHING, db_column='idtransporte', blank=True, null=True)
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    cantidadprod = models.IntegerField()
    cantidadtransp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'almacen'


class Empresario(models.Model):
    idempresario = models.AutoField(primary_key=True)
    nombres = models.CharField()
    apellidos = models.CharField()
    correo = models.CharField()
    ruc = models.IntegerField()
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario')

    class Meta:
        managed = False
        db_table = 'empresario'


class Local(models.Model):
    idlocal = models.AutoField(primary_key=True)
    ubicacion = models.CharField()
    nombre = models.CharField()
    idempresaio = models.ForeignKey(Empresario, models.DO_NOTHING, db_column='idempresaio')

    class Meta:
        managed = False
        db_table = 'local'


class Localproducto(models.Model):
    idlocalprod = models.AutoField(primary_key=True)
    idlocal = models.ForeignKey(Local, models.DO_NOTHING, db_column='idlocal')
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idproducto')

    class Meta:
        managed = False
        db_table = 'localproducto'


class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField()

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario')

    class Meta:
        managed = False
        db_table = 'proveedor'


class Transporte(models.Model):
    idtransporte = models.AutoField(primary_key=True)
    disponibilidad = models.CharField()

    class Meta:
        managed = False
        db_table = 'transporte'


class Usuario(models.Model):
    nombre_usuario = models.CharField()
    contrasenia = models.CharField()
    idusuario = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'usuario'

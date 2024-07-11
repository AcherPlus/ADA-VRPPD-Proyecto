# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Almacen(models.Model):
    idalmacen = models.AutoField(primary_key=True)
    idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='idproveedor', blank=True, null=True)
    idubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='idubicacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'almacen'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Detallepedido(models.Model):
    iddetallepedido = models.AutoField(primary_key=True)
    idpedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='idpedido', blank=True, null=True)
    idlocalrecojo = models.ForeignKey('Local', models.DO_NOTHING, db_column='idlocalrecojo', blank=True, null=True)
    idlocalentrega = models.ForeignKey('Local', models.DO_NOTHING, db_column='idlocalentrega', related_name='detallepedido_idlocalentrega_set', blank=True, null=True)
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detallepedido'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class Local(models.Model):
    idlocal = models.AutoField(primary_key=True)
    idempresario = models.ForeignKey(Empresario, models.DO_NOTHING, db_column='idempresario')
    idubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='idubicacion')
    tipo = models.CharField(blank=True, null=True)
    nombre = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local'


class Localproducto(models.Model):
    idlocalproducto = models.AutoField(primary_key=True)
    idlocal = models.ForeignKey(Local, models.DO_NOTHING, db_column='idlocal', blank=True, null=True)
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localproducto'


class Parada(models.Model):
    idparada = models.AutoField(primary_key=True)
    idruta = models.ForeignKey('Ruta', models.DO_NOTHING, db_column='idruta', blank=True, null=True)
    idubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='idubicacion', blank=True, null=True)
    tipo = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parada'


class Pedido(models.Model):
    idpedido = models.AutoField(primary_key=True)
    idempresario = models.ForeignKey(Empresario, models.DO_NOTHING, db_column='idempresario', blank=True, null=True)
    estado = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido'


class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    nombre_usuario_prov = models.CharField(blank=True, null=True)
    password_prov = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Ruta(models.Model):
    idruta = models.AutoField(primary_key=True)
    idalmacen = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='idalmacen', blank=True, null=True)
    transporte = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ruta'


class Ubicacion(models.Model):
    idubicacion = models.AutoField(primary_key=True)
    direccion = models.CharField(blank=True, null=True)
    distrito = models.CharField(blank=True, null=True)
    region = models.CharField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ubicacion'

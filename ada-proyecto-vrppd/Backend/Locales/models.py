from django.db import models
from Empresarios.models import Empresario
from Productos.models import Producto
from geopy.geocoders import Nominatim

# Create your models here.
class Local(models.Model):
    idlocal = models.AutoField(primary_key=True)
    direccion = models.CharField(blank=True, null=True)
    nombrelocal = models.CharField()
    idempresario = models.ForeignKey(Empresario, models.DO_NOTHING, db_column='idempresario')
    distrito = models.CharField(blank=True, null=True)
    region = models.CharField(blank=True, null=True)
    longitud = models.FloatField()
    latitud = models.FloatField()

    def save(self, *args, **kwargs):
        if not self.direccion or not self.distrito or not self.region:
            geolocator = Nominatim(user_agent="myGeocoder")
            location = geolocator.reverse((self.latitud, self.longitud), exactly_one=True)
            if location:
                address = location.raw.get('address', {})
                self.direccion = f"{address.get('road', '')} {address.get('house_number', '')}"
                self.distrito = address.get('suburb', '') or address.get('city_district', '') or address.get('neighbourhood', '')
                self.region = address.get('state', '') or address.get('region', '') or address.get('county', '')
        super().save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'local'

class Localproducto(models.Model):
    idlocalprod = models.AutoField(primary_key=True)
    idlocal = models.ForeignKey(Local, models.DO_NOTHING, db_column='idlocal')
    idproducto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='idproducto')

    class Meta:
        managed = False
        db_table = 'localproducto'
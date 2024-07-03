# Generated by Django 5.0.6 on 2024-07-02 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('ubicacion', models.CharField()),
                ('idalmacen', models.IntegerField(primary_key=True, serialize=False)),
                ('cantidadprod', models.IntegerField()),
                ('cantidadtransp', models.IntegerField()),
            ],
            options={
                'db_table': 'almacen',
                'managed': False,
            },
        ),
    ]
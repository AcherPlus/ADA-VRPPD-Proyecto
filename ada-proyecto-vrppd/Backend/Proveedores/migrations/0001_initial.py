# Generated by Django 5.0.6 on 2024-07-02 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idproveedor', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
    ]

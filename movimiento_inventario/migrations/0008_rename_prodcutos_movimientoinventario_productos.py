# Generated by Django 4.2.3 on 2023-07-04 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimiento_inventario', '0007_movimientoinventario_almacen_destino'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movimientoinventario',
            old_name='prodcutos',
            new_name='productos',
        ),
    ]

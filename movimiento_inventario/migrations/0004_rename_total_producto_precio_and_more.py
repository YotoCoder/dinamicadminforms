# Generated by Django 4.2.3 on 2023-07-04 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimiento_inventario', '0003_producto_movimientoinventario_almacen_afectado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='total',
            new_name='precio',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='costo_unit',
        ),
    ]

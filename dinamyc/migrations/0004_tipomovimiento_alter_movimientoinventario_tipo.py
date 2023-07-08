# Generated by Django 4.2.3 on 2023-07-08 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dinamyc', '0003_almacen_movimientoinventario_delete_dinamicform_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMovimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='movimientoinventario',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinamyc.tipomovimiento'),
        ),
    ]

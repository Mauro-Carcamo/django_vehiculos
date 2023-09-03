# Generated by Django 4.2.4 on 2023-09-03 00:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='fecha_creacion',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='fecha_modificacion',
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='fecha_de_creacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='fecha_de_modificacion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='marca',
            field=models.CharField(choices=[('Ford', 'Ford'), ('Toyota', 'Toyota'), ('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet')], default='ford', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='precio',
            field=models.FloatField(),
        ),
    ]

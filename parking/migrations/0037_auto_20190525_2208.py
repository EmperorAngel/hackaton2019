# Generated by Django 2.1.7 on 2019-05-26 02:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0036_auto_20190525_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriendo',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

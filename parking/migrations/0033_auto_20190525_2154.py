# Generated by Django 2.1.7 on 2019-05-26 01:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0032_calificacion_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriendo',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 25, 21, 54, 52, 905215)),
        ),
    ]
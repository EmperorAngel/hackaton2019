# Generated by Django 2.1.2 on 2019-04-04 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0004_auto_20190403_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_comp_data',
            name='activated',
            field=models.BooleanField(default=False),
        ),
    ]

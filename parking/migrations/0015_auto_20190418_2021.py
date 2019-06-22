# Generated by Django 2.1.7 on 2019-04-19 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0014_auto_20190418_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=15)),
                ('rgb', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='user_comp_data',
            name='ui_color_1',
            field=models.CharField(default='default', max_length=23),
        ),
        migrations.AlterField(
            model_name='user_comp_data',
            name='ui_color_2',
            field=models.CharField(default='default', max_length=23),
        ),
    ]
# Generated by Django 3.1.2 on 2021-01-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20210130_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='place',
            name='source',
            field=models.ManyToManyField(blank=True, to='database.Source'),
        ),
    ]

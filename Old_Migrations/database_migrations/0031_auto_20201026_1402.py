# Generated by Django 3.1.2 on 2020-10-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0030_auto_20201026_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristics',
            name='height',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristics',
            name='length',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristics',
            name='surface',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristics',
            name='weight',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='caracteristics',
            name='width',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]

# Generated by Django 3.1.2 on 2021-01-31 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20210131_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profession',
            name='definition',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='profession',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profession',
            name='source',
            field=models.ManyToManyField(blank=True, to='database.Source'),
        ),
    ]

# Generated by Django 3.1.2 on 2021-06-27 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0065_auto_20210627_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typologie',
            name='surface',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

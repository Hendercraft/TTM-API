# Generated by Django 3.1.2 on 2020-10-23 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20201023_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placetype',
            old_name='place_type',
            new_name='placeType',
        ),
    ]

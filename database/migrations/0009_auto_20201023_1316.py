# Generated by Django 3.1.2 on 2020-10-23 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_auto_20201023_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='place',
        ),
        migrations.RemoveField(
            model_name='social',
            name='place',
        ),
    ]
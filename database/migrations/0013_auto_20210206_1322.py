# Generated by Django 3.1.2 on 2021-02-06 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_auto_20210206_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='date',
            old_name='source_data',
            new_name='source_date',
        ),
    ]
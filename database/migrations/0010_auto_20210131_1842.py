# Generated by Django 3.1.2 on 2021-01-31 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_auto_20210131_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modify',
            old_name='x_value',
            new_name='field_value',
        ),
        migrations.RenameField(
            model_name='modify',
            old_name='y_value',
            new_name='instance_value',
        ),
    ]
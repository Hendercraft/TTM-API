# Generated by Django 3.1.2 on 2021-04-22 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0033_auto_20210422_0814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectiveactor',
            old_name='collective_abstractObject',
            new_name='abstract_object',
        ),
        migrations.RenameField(
            model_name='profession',
            old_name='abstractObject',
            new_name='abstract_object',
        ),
    ]

# Generated by Django 3.1.2 on 2021-03-25 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0019_auto_20210325_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload',
            old_name='photo',
            new_name='url',
        ),
    ]

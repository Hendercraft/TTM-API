# Generated by Django 3.1.2 on 2020-10-27 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0045_auto_20201027_1250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='last_name',
            new_name='lastName',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='source_content',
            new_name='sourceContent',
        ),
    ]

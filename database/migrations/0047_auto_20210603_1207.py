# Generated by Django 3.1.2 on 2021-06-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0046_auto_20210603_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='user',
        ),
        migrations.AddField(
            model_name='files',
            name='file_extension',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

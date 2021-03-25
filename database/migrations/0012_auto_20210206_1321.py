# Generated by Django 3.1.2 on 2021-02-06 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_auto_20210131_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='source',
            old_name='date',
            new_name='date_source',
        ),
        migrations.AddField(
            model_name='date',
            name='source_data',
            field=models.ManyToManyField(blank=True, to='database.Source'),
        ),
        migrations.AddField(
            model_name='quality',
            name='source_quality',
            field=models.ManyToManyField(blank=True, to='database.Source'),
        ),
    ]
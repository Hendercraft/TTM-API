# Generated by Django 3.1.2 on 2021-01-31 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_nameactor_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallink',
            name='source',
            field=models.ManyToManyField(blank=True, to='database.Source'),
        ),
    ]

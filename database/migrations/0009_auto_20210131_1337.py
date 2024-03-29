# Generated by Django 3.1.2 on 2021-01-31 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_sociallink_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailcaracteristic',
            name='source',
            field=models.ManyToManyField(blank=True, to='database.Source'),
        ),
        migrations.AddField(
            model_name='energy',
            name='source',
            field=models.ManyToManyField(blank=True, to='database.Source'),
        ),
        migrations.AddField(
            model_name='typeobject',
            name='source',
            field=models.ManyToManyField(blank=True, to='database.Source'),
        ),
    ]

# Generated by Django 3.1.2 on 2021-06-03 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0039_auto_20210603_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='addition_inf_date',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='actor',
            name='nationality',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

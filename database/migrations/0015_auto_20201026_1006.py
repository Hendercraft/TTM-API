# Generated by Django 3.1.2 on 2020-10-26 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0014_auto_20201026_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='duration_date',
        ),
        migrations.AlterField(
            model_name='date',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]

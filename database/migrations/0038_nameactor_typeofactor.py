# Generated by Django 3.1.2 on 2020-10-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0037_auto_20201026_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='nameactor',
            name='typeOfActor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-26 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0024_auto_20201026_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='sexe',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50),
        ),
    ]
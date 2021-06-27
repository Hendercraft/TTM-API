# Generated by Django 3.1.2 on 2021-06-27 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0063_auto_20210627_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='object',
            name='lower_categorie',
        ),
        migrations.AddField(
            model_name='object',
            name='building',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='object',
            name='categorie',
            field=models.CharField(blank=True, choices=[('Architecture', 'Architecture'), ('Production', 'Production')], max_length=50),
        ),
    ]

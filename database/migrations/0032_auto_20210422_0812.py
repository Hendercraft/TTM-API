# Generated by Django 3.1.2 on 2021-04-22 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0031_auto_20210421_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='object',
            name='lower_categorie',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profession',
            name='place',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.place'),
        ),
    ]
# Generated by Django 3.1.2 on 2020-10-26 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0027_auto_20201026_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_location',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.placelocation'),
        ),
    ]

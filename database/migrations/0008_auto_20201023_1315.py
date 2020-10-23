# Generated by Django 3.1.2 on 2020-10-23 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_auto_20201023_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractobject',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.place'),
        ),
        migrations.AlterField(
            model_name='collectiveactor',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.place'),
        ),
        migrations.AlterField(
            model_name='object',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.place'),
        ),
        migrations.AlterField(
            model_name='profession',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.place'),
        ),
    ]

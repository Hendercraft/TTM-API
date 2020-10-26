# Generated by Django 3.1.2 on 2020-10-26 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0028_auto_20201026_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractobject',
            name='knowledge',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.knowledge'),
        ),
        migrations.AlterField(
            model_name='abstractobject',
            name='place',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.place'),
        ),
        migrations.AlterField(
            model_name='abstractobject',
            name='quality',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.quality'),
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-26 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0021_auto_20201026_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractobject',
            name='collectiveActor',
            field=models.ManyToManyField(blank=True, to='database.CollectiveActor'),
        ),
        migrations.AlterField(
            model_name='abstractobject',
            name='knowledge',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='database.knowledge'),
        ),
        migrations.AlterField(
            model_name='abstractobject',
            name='place',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='database.place'),
        ),
    ]

# Generated by Django 3.1.2 on 2021-06-27 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0066_auto_20210627_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='type_object',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.typeobject'),
        ),
    ]

# Generated by Django 3.1.2 on 2021-06-17 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0054_auto_20210610_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500)),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='object',
            name='building',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.building_type'),
        ),
    ]

# Generated by Django 3.1.2 on 2021-04-25 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0036_auto_20210424_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='commentary',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='date',
            name='day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='date',
            name='month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='date',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='editor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='editor', to='database.author'),
        ),
        migrations.AddField(
            model_name='source',
            name='original_registration',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='source',
            name='registration',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='source',
            name='rights',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='source',
            name='study',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]

# Generated by Django 3.1.2 on 2021-04-21 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0030_auto_20210409_0650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='object',
            old_name='definition',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='object',
            name='brand',
        ),
        migrations.AddField(
            model_name='object',
            name='categorie',
            field=models.CharField(blank=True, choices=[('architecture', 'Architecture'), ('production', 'Production'), ('hommes', 'Hommes'), ('urbanisme', 'Urbanisme')], max_length=50),
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(blank=True, max_length=500)),
                ('wall', models.CharField(blank=True, max_length=500)),
                ('roof', models.CharField(blank=True, max_length=500)),
                ('floor', models.IntegerField(blank=True)),
                ('surface', models.IntegerField(blank=True)),
                ('light', models.CharField(blank=True, max_length=500)),
                ('materials', models.CharField(blank=True, max_length=500)),
                ('fk_object', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.object')),
            ],
        ),
    ]

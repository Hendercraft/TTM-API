# Generated by Django 3.1.2 on 2021-02-06 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0014_auto_20210206_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelationLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, choices=[('OLD', 'Old'), ('MADEBY', 'Madeby'), ('USE', 'Use'), ('CREATE', 'Create')], max_length=50)),
                ('validated', models.BooleanField(default=False)),
                ('object_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.object')),
                ('source', models.ManyToManyField(blank=True, to='database.Source')),
            ],
        ),
    ]

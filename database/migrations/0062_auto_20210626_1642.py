# Generated by Django 3.1.2 on 2021-06-26 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0061_auto_20210626_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='url',
        ),
        migrations.AddField(
            model_name='source',
            name='url',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='database.files'),
        ),
    ]

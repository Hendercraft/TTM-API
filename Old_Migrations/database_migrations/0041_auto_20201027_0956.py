# Generated by Django 3.1.2 on 2020-10-27 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0040_auto_20201027_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='socialLink',
        ),
        migrations.AddField(
            model_name='actor',
            name='socialLink',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.sociallink'),
        ),
    ]
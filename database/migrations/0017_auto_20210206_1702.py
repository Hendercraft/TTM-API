# Generated by Django 3.1.2 on 2021-02-06 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0016_author_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='source',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='database.author'),
        ),
        migrations.AlterField(
            model_name='source',
            name='types',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='database.sourcetype'),
        ),
    ]
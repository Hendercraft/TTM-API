# Generated by Django 3.1.2 on 2021-04-08 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0026_auto_20210325_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='fileType',
            field=models.CharField(blank=True, choices=[('Audio', 'Audio'), ('Video', 'Video'), ('Cao', 'Cao'), ('Image', 'Image'), ('Document', 'Document')], max_length=50, null=True),
        ),
    ]

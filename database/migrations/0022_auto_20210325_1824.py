# Generated by Django 3.1.2 on 2021-03-25 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0021_auto_20210325_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('definition', models.CharField(blank=True, max_length=1000, null=True)),
                ('url', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='url',
        ),
        migrations.AddField(
            model_name='source',
            name='url',
            field=models.ManyToManyField(blank=True, to='database.Files'),
        ),
    ]
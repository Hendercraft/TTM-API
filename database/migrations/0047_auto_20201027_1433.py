# Generated by Django 3.1.2 on 2020-10-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0046_auto_20201027_1315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='sexe',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='sociallink',
            old_name='actorlinked',
            new_name='actorlink',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='namesOfActor',
        ),
        migrations.AddField(
            model_name='object',
            name='brand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

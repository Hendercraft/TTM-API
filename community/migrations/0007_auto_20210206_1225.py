# Generated by Django 3.1.2 on 2021-02-06 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_remove_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='commentsDiscipline',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='researchestablishment',
            name='commentsEstablishment',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='researchfield',
            name='commentsResearch',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='workedInCompany',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]

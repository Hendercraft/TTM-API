# Generated by Django 3.1.2 on 2021-01-08 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='disciplineFK',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.discipline'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phoneNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='postalAdress',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profileImage',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='researchEstablishmentFK',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.researchestablishment'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='researchFieldFK',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.researchfield'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='workTimeDuration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='workedInCompany',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='workedOnTheSite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='groups',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]

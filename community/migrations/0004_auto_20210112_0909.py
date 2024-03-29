# Generated by Django 3.1.2 on 2021-01-12 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20210108_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='disciplineFK',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.discipline'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='researchEstablishmentFK',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.researchestablishment'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='researchFieldFK',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.researchfield'),
        ),
    ]

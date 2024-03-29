# Generated by Django 3.1.2 on 2020-11-30 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0004_auto_20201125_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postalAdress', models.IntegerField(blank=True, null=True)),
                ('phoneNumber', models.IntegerField(blank=True, null=True)),
                ('profileImage', models.URLField(blank=True, null=True)),
                ('workedOnTheSite', models.BooleanField(default=False)),
                ('workedInCompany', models.CharField(blank=True, max_length=255, null=True)),
                ('workTimeDuration', models.IntegerField(blank=True, null=True)),
                ('discipline', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='community.discipline')),
                ('researchEstablishment', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='community.researchestablishment')),
                ('researchField', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='community.researchfield')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserInformation',
        ),
    ]

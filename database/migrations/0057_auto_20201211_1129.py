# Generated by Django 3.1.2 on 2020-12-11 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0056_auto_20201117_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstractobject',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='actor',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='caracteristic',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='collectiveactor',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='date',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='detailcaracteristic',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='energy',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='knowledge',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='nameactor',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='object',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='place',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='placelocation',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='placetype',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profession',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quality',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='socialactivity',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sociallink',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='source',
            name='validated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='typeobject',
            name='validated',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 3.1.2 on 2021-01-06 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0057_auto_20201211_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.CharField(choices=[('Date', 'Date'), ('Quality', 'Quality'), ('SourceType', 'Sourcetype'), ('Author', 'Author'), ('Content', 'Content'), ('Url', 'Url'), ('Source', 'Source'), ('PlaceLocation', 'Placelocation'), ('PlaceType', 'Placetype'), ('Place', 'Place'), ('Knowledge', 'Knowledge'), ('CollectiveActor', 'Collectiveactor'), ('AbstractObject', 'Abstractobject'), ('Profession', 'Profession'), ('SocialActivity', 'Socialactivity'), ('SocialLink', 'Sociallink'), ('Actor', 'Actor'), ('NameActor', 'Nameactor'), ('DetailCaracteristic', 'Detailcaracteristic'), ('TypeObject', 'Typeobject'), ('Energy', 'Energy'), ('Object', 'Object'), ('Caracteristic', 'Caracteristic')], max_length=250)),
                ('x_value', models.IntegerField()),
                ('y_value', models.IntegerField()),
                ('content', models.CharField(max_length=10000)),
            ],
        ),
        migrations.AlterField(
            model_name='actor',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='content',
            name='sourceContent',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='detailcaracteristic',
            name='detailCaracteristicsObject',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='energy',
            name='energy',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='object',
            name='brand',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='content',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='definition',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='placelocation',
            name='city',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='placelocation',
            name='country',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='placelocation',
            name='place_said',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='placelocation',
            name='street_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='placetype',
            name='placeType',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='profession',
            name='definition',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='quality',
            name='definition',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='socialactivity',
            name='definition',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='source',
            name='conservationPlace',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='sourcetype',
            name='typesSource',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='typeobject',
            name='typeObject',
            field=models.CharField(max_length=500),
        ),
    ]
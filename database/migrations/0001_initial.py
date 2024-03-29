# Generated by Django 3.1.2 on 2021-01-08 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('definition', models.CharField(max_length=1000)),
                ('validated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100)),
                ('validated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lastName', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('organisation', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CollectiveActor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('definition', models.CharField(max_length=1000)),
                ('validated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourceContent', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField(blank=True, null=True)),
                ('duration_date', models.DurationField(blank=True, null=True)),
                ('validated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DetailCaracteristic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detailCaracteristicsObject', models.CharField(max_length=1000)),
                ('validated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Energy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy', models.CharField(max_length=200)),
                ('validated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('definition', models.CharField(max_length=1000)),
                ('validated', models.BooleanField(default=False)),
            ],
        ),
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
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('validated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_number', models.IntegerField()),
                ('street_type', models.CharField(blank=True, max_length=3, null=True)),
                ('street_name', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('post_code', models.IntegerField(blank=True, default=None, null=True)),
                ('country', models.CharField(max_length=500)),
                ('place_said', models.CharField(blank=True, max_length=1000, null=True)),
                ('validated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeType', models.CharField(max_length=500)),
                ('validated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('definition', models.CharField(max_length=1000)),
                ('validated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SourceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeSource', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TypeObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeObject', models.CharField(max_length=500)),
                ('validated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('viability', models.IntegerField(choices=[(0, 'Notreliable'), (1, 'Reliable')], default=0)),
                ('conservationPlace', models.CharField(blank=True, max_length=1000, null=True)),
                ('cote', models.CharField(blank=True, max_length=200)),
                ('validated', models.BooleanField(default=False)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='database.author')),
                ('content', models.ManyToManyField(blank=True, to='database.Content')),
                ('date', models.ManyToManyField(blank=True, to='database.Date')),
                ('types', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='database.sourcetype')),
                ('url', models.ManyToManyField(blank=True, to='database.Url')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(choices=[('FATHER', 'Father'), ('MOTHER', 'Mother'), ('SISTER', 'Sister'), ('BROTHER', 'Brother'), ('FRIEND', 'Friend'), ('CO-WORKERS', 'Coworker')], max_length=50)),
                ('validated', models.BooleanField(default=False)),
                ('actorlink', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.actor')),
            ],
        ),
        migrations.CreateModel(
            name='SocialActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('definition', models.CharField(max_length=1000)),
                ('validated', models.BooleanField(default=False)),
                ('place', models.ManyToManyField(blank=True, to='database.Place')),
                ('source', models.ManyToManyField(to='database.Source')),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('definition', models.CharField(max_length=1000)),
                ('autonomous', models.BooleanField(default=False)),
                ('validated', models.BooleanField(default=False)),
                ('abstractObject', models.ManyToManyField(blank=True, to='database.AbstractObject')),
                ('place', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='database.place')),
                ('source', models.ManyToManyField(to='database.Source')),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='place_location',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.placelocation'),
        ),
        migrations.AddField(
            model_name='place',
            name='place_type',
            field=models.ManyToManyField(blank=True, to='database.PlaceType'),
        ),
        migrations.AddField(
            model_name='place',
            name='source',
            field=models.ManyToManyField(to='database.Source'),
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('definition', models.CharField(max_length=1000)),
                ('brand', models.CharField(blank=True, max_length=500, null=True)),
                ('content', models.CharField(blank=True, max_length=1000, null=True)),
                ('validated', models.BooleanField(default=False)),
                ('abstract_object', models.ManyToManyField(blank=True, to='database.AbstractObject')),
                ('actor', models.ManyToManyField(blank=True, to='database.Actor')),
                ('collectiveActors', models.ManyToManyField(blank=True, to='database.CollectiveActor')),
                ('date', models.ManyToManyField(blank=True, to='database.Date')),
                ('energy', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.energy')),
                ('place', models.ManyToManyField(blank=True, to='database.Place')),
                ('source', models.ManyToManyField(to='database.Source')),
                ('type_object', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='database.typeobject')),
            ],
        ),
        migrations.CreateModel(
            name='NameActor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('typeOfActor', models.CharField(blank=True, max_length=200, null=True)),
                ('validated', models.BooleanField(default=False)),
                ('actors', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='database.actor')),
            ],
        ),
        migrations.AddField(
            model_name='collectiveactor',
            name='date',
            field=models.ManyToManyField(blank=True, to='database.Date'),
        ),
        migrations.AddField(
            model_name='collectiveactor',
            name='knowledge',
            field=models.ManyToManyField(blank=True, to='database.Knowledge'),
        ),
        migrations.AddField(
            model_name='collectiveactor',
            name='place',
            field=models.ManyToManyField(blank=True, to='database.Place'),
        ),
        migrations.AddField(
            model_name='collectiveactor',
            name='quality',
            field=models.ManyToManyField(blank=True, to='database.Quality'),
        ),
        migrations.AddField(
            model_name='collectiveactor',
            name='source',
            field=models.ManyToManyField(to='database.Source'),
        ),
        migrations.CreateModel(
            name='Caracteristic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.FloatField(blank=True, default=None, null=True)),
                ('width', models.FloatField(blank=True, default=None, null=True)),
                ('height', models.FloatField(blank=True, default=None, null=True)),
                ('weight', models.FloatField(blank=True, default=None, null=True)),
                ('surface', models.FloatField(blank=True, default=None, null=True)),
                ('validated', models.BooleanField(default=False)),
                ('detail_caracteristics', models.ManyToManyField(blank=True, to='database.DetailCaracteristic')),
                ('objectCaracteristic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.object')),
                ('source', models.ManyToManyField(to='database.Source')),
            ],
        ),
        migrations.AddField(
            model_name='actor',
            name='collectiveActors',
            field=models.ManyToManyField(blank=True, to='database.CollectiveActor'),
        ),
        migrations.AddField(
            model_name='actor',
            name='place',
            field=models.ManyToManyField(blank=True, to='database.Place'),
        ),
        migrations.AddField(
            model_name='actor',
            name='profession',
            field=models.ManyToManyField(blank=True, to='database.Profession'),
        ),
        migrations.AddField(
            model_name='actor',
            name='quality',
            field=models.ManyToManyField(blank=True, to='database.Quality'),
        ),
        migrations.AddField(
            model_name='actor',
            name='socialActivities',
            field=models.ManyToManyField(blank=True, to='database.SocialActivity'),
        ),
        migrations.AddField(
            model_name='actor',
            name='socialLink',
            field=models.ManyToManyField(blank=True, to='database.SocialLink'),
        ),
        migrations.AddField(
            model_name='actor',
            name='source',
            field=models.ManyToManyField(to='database.Source'),
        ),
        migrations.AddField(
            model_name='abstractobject',
            name='collectiveActor',
            field=models.ManyToManyField(blank=True, to='database.CollectiveActor'),
        ),
        migrations.AddField(
            model_name='abstractobject',
            name='date',
            field=models.ManyToManyField(blank=True, to='database.Date'),
        ),
        migrations.AddField(
            model_name='abstractobject',
            name='knowledge',
            field=models.ManyToManyField(blank=True, to='database.Knowledge'),
        ),
        migrations.AddField(
            model_name='abstractobject',
            name='place',
            field=models.ManyToManyField(blank=True, to='database.Place'),
        ),
        migrations.AddField(
            model_name='abstractobject',
            name='quality',
            field=models.ManyToManyField(blank=True, to='database.Quality'),
        ),
        migrations.AddField(
            model_name='abstractobject',
            name='source',
            field=models.ManyToManyField(to='database.Source'),
        ),
    ]

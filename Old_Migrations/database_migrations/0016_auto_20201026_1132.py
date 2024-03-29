# Generated by Django 3.1.2 on 2020-10-26 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0015_auto_20201026_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typesSource', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='source',
            old_name='conservation_place',
            new_name='conservationPlace',
        ),
        migrations.RemoveField(
            model_name='typeobject',
            name='type_object',
        ),
        migrations.AddField(
            model_name='typeobject',
            name='typeObject',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='detailcaracteristics',
            name='detailCaracteristicsObject',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='energy',
            name='energy',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='placetype',
            name='placeType',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='source',
            name='types',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='database.sourcetypes'),
        ),
        migrations.DeleteModel(
            name='Types',
        ),
    ]

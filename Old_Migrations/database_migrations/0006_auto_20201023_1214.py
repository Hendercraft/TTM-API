# Generated by Django 3.1.2 on 2020-10-23 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20201023_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractobject',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.date'),
        ),
        migrations.AlterField(
            model_name='abstractobject',
            name='knowledge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.knowledge'),
        ),
        migrations.AlterField(
            model_name='abstractobject',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.place'),
        ),
        migrations.AlterField(
            model_name='abstractobject',
            name='quality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.quality'),
        ),
        migrations.AlterField(
            model_name='abstractobject',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.source'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='collectiveActors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.collectiveactor'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='quality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.quality'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='social',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.social'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='socialLink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.sociallink'),
        ),
        migrations.AlterField(
            model_name='caracteristics',
            name='detail_caracteristics',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.detailcaracteristics'),
        ),
        migrations.AlterField(
            model_name='collectiveactor',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.date'),
        ),
        migrations.AlterField(
            model_name='collectiveactor',
            name='knowledge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.knowledge'),
        ),
        migrations.AlterField(
            model_name='collectiveactor',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.place'),
        ),
        migrations.AlterField(
            model_name='collectiveactor',
            name='quality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.quality'),
        ),
        migrations.AlterField(
            model_name='collectiveactor',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.source'),
        ),
        migrations.AlterField(
            model_name='nameactor',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.actor'),
        ),
        migrations.AlterField(
            model_name='object',
            name='caracteristics',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.caracteristics'),
        ),
        migrations.AlterField(
            model_name='object',
            name='energy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.energy'),
        ),
        migrations.AlterField(
            model_name='object',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.source'),
        ),
        migrations.AlterField(
            model_name='object',
            name='type_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.typeobject'),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.placelocation'),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.placetype'),
        ),
        migrations.AlterField(
            model_name='place',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.source'),
        ),
        migrations.AlterField(
            model_name='profession',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.place'),
        ),
        migrations.AlterField(
            model_name='social',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.source'),
        ),
        migrations.AlterField(
            model_name='source',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.author'),
        ),
        migrations.AlterField(
            model_name='source',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.date'),
        ),
        migrations.AlterField(
            model_name='source',
            name='types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.types'),
        ),
    ]

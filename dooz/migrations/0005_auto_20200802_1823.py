# Generated by Django 3.0.5 on 2020-08-02 13:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dooz', '0004_auto_20200802_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamehistory',
            name='computer',
            field=models.CharField(blank=True, default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='row',
            field=models.BooleanField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn1',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None), size=None), size=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn2',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None), size=None), size=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn3',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None), size=None), size=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn4',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None), size=None), size=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn5',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None), size=None), size=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn6',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None), size=None), size=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn7',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None), size=None), size=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn8',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None), size=None), size=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn9',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None), size=None), size=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='user',
            field=models.CharField(blank=True, default=None, max_length=10),
        ),
    ]

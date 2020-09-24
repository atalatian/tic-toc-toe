# Generated by Django 3.0.5 on 2020-08-03 09:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dooz', '0009_auto_20200803_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamehistory',
            name='row',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn2',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn3',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn4',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn5',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn6',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn7',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn8',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='turn9',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, default=None, null=True), blank=True, null=True, size=None),
        ),
    ]

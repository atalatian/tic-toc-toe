# Generated by Django 3.0.9 on 2020-08-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dooz', '0011_auto_20200804_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamehistory',
            name='counter',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

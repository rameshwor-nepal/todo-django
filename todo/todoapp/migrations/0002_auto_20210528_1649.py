# Generated by Django 3.2 on 2021-05-28 11:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='due',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 11, 4, 14, 821089, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='work',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]

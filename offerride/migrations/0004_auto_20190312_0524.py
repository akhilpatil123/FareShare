# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-12 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerride', '0003_ride_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ride',
            name='seat',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='ride',
            name='time',
            field=models.CharField(default=b'10:10', max_length=250),
        ),
    ]

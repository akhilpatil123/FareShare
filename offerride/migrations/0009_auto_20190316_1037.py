# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-03-16 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerride', '0008_auto_20190316_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='carmodel',
            field=models.CharField(default='x', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='carno',
            field=models.CharField(default='x', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='cartype',
            field=models.CharField(default='s', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(default='red', max_length=240, null=True),
        ),
    ]
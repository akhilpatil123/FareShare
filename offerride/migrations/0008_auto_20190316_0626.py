# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-16 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerride', '0007_auto_20190316_0432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='charno',
        ),
        migrations.AddField(
            model_name='car',
            name='carmodel',
            field=models.CharField(default=b'x', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='carno',
            field=models.CharField(default=b'x', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='carseats',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='cartype',
            field=models.CharField(default=b's', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(default=b'red', max_length=240, null=True),
        ),
    ]
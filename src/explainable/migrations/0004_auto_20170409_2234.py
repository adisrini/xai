# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explainable', '0003_dataset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='docfile',
        ),
        migrations.AddField(
            model_name='dataset',
            name='dataset_url',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]

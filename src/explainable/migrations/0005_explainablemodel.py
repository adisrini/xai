# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explainable', '0004_auto_20170409_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExplainableModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=200)),
            ],
        ),
    ]
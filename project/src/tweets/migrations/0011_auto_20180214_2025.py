# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-14 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import tweets.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0010_auto_20180214_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweet',
            field=models.CharField(max_length=400, validators=[tweets.validators.validate_content]),
        ),
    ]

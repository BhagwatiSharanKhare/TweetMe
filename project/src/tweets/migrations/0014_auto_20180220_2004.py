# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-20 14:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0013_auto_20180220_2003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-updated']},
        ),
    ]
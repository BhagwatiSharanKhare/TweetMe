# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-22 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0014_auto_20180220_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='tweet',
            new_name='content',
        ),
    ]
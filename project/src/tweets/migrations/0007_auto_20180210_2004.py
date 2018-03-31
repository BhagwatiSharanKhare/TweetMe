# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-02-10 14:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tweets.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_auto_20180210_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=280, validators=[tweets.validators.validate_content]),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

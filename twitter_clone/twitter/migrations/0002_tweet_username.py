# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-29 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='username',
            field=models.CharField(default='trevor', max_length=200),
            preserve_default=False,
        ),
    ]

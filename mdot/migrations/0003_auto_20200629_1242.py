# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-29 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdot', '0002_auto_20200506_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='email',
            field=models.EmailField(default='None', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sponsor',
            name='email',
            field=models.EmailField(default='None', max_length=256),
            preserve_default=False,
        ),
    ]

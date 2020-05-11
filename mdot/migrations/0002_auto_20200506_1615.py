# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-06 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='requestor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

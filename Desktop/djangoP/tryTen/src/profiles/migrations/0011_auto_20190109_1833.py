# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-09 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_profile_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='stock',
            field=models.CharField(blank=True, default='0', max_length=120, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 08:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdata', '0003_auto_20160209_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock_current',
            old_name='hanme',
            new_name='hname',
        ),
    ]

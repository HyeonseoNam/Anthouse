# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('image_file', models.ImageField(upload_to='%Y/%m/%d')),
                ('filtered_image_file', models.ImageField(upload_to='static_files/uploaded/%Y/%m/%d')),
                ('description', models.TextField(max_length=500, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

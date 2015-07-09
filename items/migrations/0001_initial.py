# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemref', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(unique=True, max_length=4)),
                ('name', models.CharField(max_length=60)),
                ('cost', models.PositiveIntegerField()),
                ('secret_shop', models.PositiveSmallIntegerField()),
                ('side_shop', models.PositiveSmallIntegerField()),
                ('recipe', models.PositiveSmallIntegerField()),
                ('localized_name', models.CharField(max_length=60)),
            ],
        ),
    ]

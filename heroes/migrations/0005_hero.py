# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0004_delete_hero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('heroref', models.AutoField(serialize=False, primary_key=True)),
                ('id', models.CharField(unique=True, max_length=3)),
                ('name', models.CharField(max_length=50)),
                ('localized_name', models.CharField(max_length=30)),
            ],
        ),
    ]
